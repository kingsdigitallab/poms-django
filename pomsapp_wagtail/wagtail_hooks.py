from django.conf import settings
from django.utils.html import format_html, format_html_join
from wagtail.wagtailcore import hooks


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