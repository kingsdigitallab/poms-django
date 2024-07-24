"""
Migrate the old wordpress pages into wagtail django models.
Based on Geoffroy Noel's KdlWp2Wt command from Culture Case

@author Elliott HAll
"""
from kdl_wordpress2wagtail.management.commands.kdlwp2wt import (
    Command as KdlWp2Wt)
from pomsapp_wagtail.models import HomePage, IndexPage, RichTextPage
from wagtail.images.models import Image
from willow import Image as WillowImage
import re
from django.conf import settings
import os
import operator
from django.utils.text import slugify
from django.core.exceptions import ObjectDoesNotExist


class Command(KdlWp2Wt):
    help = 'Import wordpress xml dump into wagtail'
    # caching pages to rebuild tree structure at the end
    pages = {}
    inheritance_map = {}
    home_page = None

    def initialise_registry(self):
        super(Command, self).initialise_registry()
        # create our home page
        """
         delete from pomsapp_wagtail_homepage;
         delete from pomsapp_wagtail_indexpage;
         delete from pomsapp_wagtail_richtextpage;
         delete from wagtailcore_page where id>2;
        """

        if HomePage.objects.all().count() == 0:
            hp = HomePage(
                title='Home',
                body='test',
                slug='th1'
            )
        else:
            hp = HomePage.objects.all()[0]
        # clean rich text pages
        site_root = self.registry.get("item_page:0")
        site_root.add_child(instance=hp)
        self.home_page = hp

    def convert_item_page(self, info):
        node = info['kdlnode']
        slug = node['wp:post_name']

        if not slug:
            print('WARNING: item without a post_name / slug')
            slug = slugify(node['title'])

        ret = {
            'model': RichTextPage,
            # Mapping between django model fields and wordpress node
            # content
            'data': {
                'title': node['title'],
                'slug': slug,
                'live': self.is_object_live(node),
                'depth': 2,
                'path': '/{}'.format(node['wp:post_name'])
            }
        }

        parent_id = node['wp:post_parent']
        page_id = node['wp:post_id']
        order = int(node['wp:menu_order'])
        if parent_id not in self.inheritance_map:
            self.inheritance_map[parent_id] = {}
        self.inheritance_map[parent_id][page_id] = order

        # use home page
        if node and 'Home' in node['title']:
            ret['data']['body'] = self.convert_body(node['content:encoded'])
            ret['model'] = HomePage
            ret['data']['depth'] = 1

        else:
            ret['data']['content'] = self.convert_body(node['content:encoded'])

        return ret

    def convert_item_nav_menu_item(self, info):
        ''' a wordpress object for a menu entry that references another object
        e.g. item_page
        We don't create a wagtail object for it, we just mark
        the referenced object as show_in_menus and reset it's sort order
        '''
        ret = None

        node = info['kdlnode']
        metas = node.get_wp_metas()

        # parent_id = node['wp:post_parent']
        # page_id = metas['_menu_item_object_id']
        # order = int(node['wp:menu_order'])
        # if parent_id not in self.inheritance_map:
        #     self.inheritance_map[parent_id] = {}
        # self.inheritance_map[parent_id][page_id] = order

        # get the wordpress object it refers to

        target_type = metas['_menu_item_object'].replace('-', '_')

        # menu link to a page
        if target_type == 'page':
            target_type = 'item_' + target_type

        targetid = target_type + ':' + metas['_menu_item_object_id']

        info['slug'] = node['title']

        # retrieve the corresponding wagtail object
        target = self.registry.get(targetid)
        if target:
            self.registry.set(info['wordpressid'], target, protected=True)

            ret = {
                'model': type(target),
                'data': {
                    'show_in_menus': True,
                    'short_title': node['title'],
                }
            }

            self._set_page_location(
                target,
                sort_order=node['wp:menu_order']
            )

        return ret

    def convert_item_attachment(self, info):
        '''Download wordpress image attachment and import them into Wagtail'''
        node = info['kdlnode']

        # we don't need a parent page; images are out of the page tree
        info['wordpress_parentid'] = None

        url = node['wp:attachment_url']
        filename = re.sub(r'^.*/', '', url.rstrip('/'))

        # /home/project/static/media/original_images/XXX.jpg
        relative_path = Image().get_upload_to(filename)

        # Prepare the structure that allows teh import to update/create
        # a django object.
        ret = {
            'model': Image,
            # Mapping between django model fields and wordpress node content
            'data': {
                'title': node['title'],
                'file': relative_path,
            }
        }

        download_path = os.path.join(
            settings.MEDIA_ROOT, relative_path)
        if not os.path.exists(download_path):
            # download the file
            import requests
            res = requests.get(url)
            with open(download_path, 'wb') as f:
                f.write(res.content)

        import willow
        try:
            with open(download_path, 'rb') as f:
                image = WillowImage.open(f)
                ret['data']['width'], ret['data']['height'] = image.get_size()
        except willow.image.UnrecognisedImageFormatError:
            ret = None

        return ret

    def import_object(self, info):
        '''
        Import a single Wordpress object into Django:
        - convert the WP object into Django data
        - create or update the django object in the database
        - attach to parent object if needed
        - add WP -> Django Object link to the registry
        - updates info['obj'] = django_object
        - returns an operation code (C|U|E|?)
        '''

        ret = '?'

        # node = info['kdlnode']

        model_info = info['converter'](info)
        if model_info is None:
            return '0'

        django_object = self.registry.get(info['wordpressid'])

        if not django_object:
            ret = 'C'
            # django object doesn't exist yet
            parent = None

            if info['type'] != 'item_page' and info['wordpress_parentid']:
                parent = self.registry.get(info['wordpress_parentid'])

                # needs a parent
                if not parent:
                    print(
                        'WARNING: could not find parent {}'.format(
                            info['wordpress_parentid']
                        )
                    )
                    return 'E'

            # create new django object under parent
            AModel = model_info['model']
            # create new instance
            django_object = AModel(**model_info['data'])

            if info['type'] == 'item_page':
                # cache pages so we can built inheritance properly
                # at the end
                # parent_id = info[
                #     'wordpress_parentid'].replace("item_page:", "")
                # info['pa'] = list()
                self.pages[info['wordpressid']] = info

            else:
                if parent:
                    # add it under the parent

                    parent.add_child(instance=django_object)

                django_object.save()

                # add to registry
                self.registry.set(info['wordpressid'], django_object)

                wordpressid_alias = info.get('wordpressid_alias')
                if wordpressid_alias:
                    self.registry.set(wordpressid_alias, django_object)
        else:
            ret = 'U'

            # update the django object
            for k, v in model_info['data'].items():
                setattr(django_object, k, v)

            django_object.save()

        # caller need to know about this object
        info['obj'] = django_object

        if info['post_converter']:
            info['post_converter'](info)

        return ret

    def _post_import(self):
        """ Sort out page inheritance structure """
        for wordpressid, info in self.pages.items():
            # First pass, convert objects to IndexPages as necessary
            obj = info['obj']
            if (info['type'] == 'item_page' and
                    'Home' in obj.title):
                # this is the home page
                self.home_page.title = obj.title
                self.home_page.slug = obj.slug
                self.home_page.body = obj.body
                self.home_page.show_in_menus = True
                self.home_page.save()

            # Does page have parent?
            elif info['wordpress_parentid']:
                if info['wordpress_parentid'] != 'item_page:0':
                    parent = self.pages[info['wordpress_parentid']]
                    if parent:
                        parent_obj = parent['obj']
                        # Is the parent an index page?
                        if isinstance(parent_obj, RichTextPage):
                            # Remake as index and replace
                            new_parent = IndexPage(title=parent_obj.title,
                                                   content=parent_obj.content,
                                                   slug=parent_obj.slug
                                                   )

                            # new_parent.save()
                            # new_parent.show_in_menus
                            # parent_obj.get_parent().add_child
                            self.pages[info['wordpress_parentid']]['obj'] \
                                = new_parent
                        # Attach
                        # obj.save()
                        # parent_obj.add_child(instance=obj)
                    else:
                        print("Parent not found! {}".format(
                            info['wordpress_parentid']
                        ))
        # now that we've got the right objects, rebuild the tree
        # home page always zero
        self.rebuild_tree('0')

    def rebuild_tree(self, parent_id):
        parent = None
        if parent_id == '0':
            parent = self.home_page
        else:
            try:
                # todo parent_id is wordpress get form info
                parent = self.pages["item_page:{}".format(parent_id)]['obj']
                # IndexPage.objects.get(id=int(parent_id))
            except ObjectDoesNotExist:
                print("parent_id does not exist {}".format(parent_id))
        if parent_id in self.inheritance_map:
            children = self.inheritance_map[parent_id]
            if len(children) > 0:
                sorted_children = sorted(
                    children.items(), key=operator.itemgetter(1))
                for sorted_child in sorted_children:
                    page_id = sorted_child[0]
                    try:
                        child = self.pages["item_page:{}".format(
                            page_id)]['obj']
                    except ObjectDoesNotExist:
                        child = IndexPage(id=int(page_id))
                    if parent and child:
                        # refresh object
                        if parent_id == '0':
                            parent = HomePage.objects.get(pk=self.home_page.pk)
                        else:
                            parent = IndexPage.objects.get(pk=parent.pk)
                        child.show_in_menus = True
                        if child.slug and len(child.slug) > 0:
                            parent.add_child(instance=child)
                            print("{} -> {}".format(parent, child))

                        if page_id in self.inheritance_map:
                            self.rebuild_tree(page_id)
        return True
