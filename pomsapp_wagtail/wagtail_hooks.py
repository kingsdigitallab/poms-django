from django.conf import settings
from django.utils.html import format_html, format_html_join
from wagtail.core import hooks
from wagtail.core.whitelist import attribute_rule, check_url


def whitelister_element_rules():
    return {
        'p': attribute_rule({'class': True}),
        'a': attribute_rule({'href': check_url, 'id': True, 'class': True,
                             'target': True}),
        'span': attribute_rule({'class': True,'id':True}),
        'i': attribute_rule({'class': True}),
        'iframe': attribute_rule(
            {'id': True, 'class': True, 'src': True, 'style': True,
             'frameborder': True, 'allowfullscreen': True, 'width': True,
             'height': True}),
        'small': attribute_rule({'class': True}),
        'table': attribute_rule({'class': True, 'id': True, 'style': True}),
        'tr': attribute_rule({'class': True, 'id': True, 'style': True}),
        'td': attribute_rule({'class': True, 'id': True, 'style': True}),
        'th': attribute_rule({'class': True, 'id': True, 'style': True}),
        'b': attribute_rule({'class': True}),
        'strong': attribute_rule({'class': True}),
        'h2': attribute_rule({'class': True, 'id': True}),

    }


hooks.register('construct_whitelister_element_rules',
               whitelister_element_rules)


def editor_js():
    js_files = [
        'js/hallo_source_editor.js'
    ]

    js_includes = format_html_join('\n', '<script src="{0}{1}"></script>',
                                   ((settings.STATIC_URL, filename)
                                    for filename in js_files)
                                   )

    return js_includes + format_html("""
        <script>
            registerHalloPlugin('editHtmlButton');
        </script>
        """)


hooks.register('insert_editor_js', editor_js)
