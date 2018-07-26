"""
Migrate the old wordpress pages into wagtail django models.
Based on Geoffroy Noel's KdlWp2Wt command from Culture Case

@author Elliott HAll
"""
from kdl_wordpress2wagtail.management.commands.kdlwp2wt import (
    Command as KdlWp2Wt, SITE_ROOT)
from pomsapp_wagtail.models import HomePage, RichTextPage
from django.utils.text import slugify
from wagtail.wagtailimages.models import Image
from willow import Image as WillowImage
import re
import pdb
from django.conf import settings
import os

class Command(KdlWp2Wt):
    help = 'Import wordpress xml dump into wagtail'
    #caching pages to rebuild tree structure at the end
    pages = []

    def convert_item_page(self, info):
        node = info['kdlnode']

        ret = {
            'model': RichTextPage,
            # Mapping between django model fields and wordpress node
            # content
            'data': {
                'title': node['title'],
                'slug': node['wp:post_name'],
                'live': self.is_object_live(node)
            }
        }

        # use home page
        if node and 'Home' in node['title']:
            ret['data']['body'] = self.convert_body(node['content:encoded'])
            ret['model'] = HomePage
            pdb.set_trace()
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

        # get the wordpress object it refers to
        metas = node.get_wp_metas()

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

            if info['wordpress_parentid']:
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
                self.pages.append(info)
                django_object.save()
            else:
                if parent:
                    # add it under the parent
                    # pdb.set_trace()
                    parent.add_child(instance=django_object)
                else:
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
        for page in self.pages:
            print(page)
