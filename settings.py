import os
import os.path as op
import sys

from django.conf.global_settings import *  # @UnusedWildImport
from django.utils.translation import ugettext_lazy as _

try:
    VIRTUALENV_DIR = os.environ['VIRTUAL_ENV']
except KeyError:
    sys.stderr.write('Error: virtualenv is not activated.\n')
    sys.exit(1)

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

sys.path.insert(0, os.path.join(BASE_DIR, 'apps'))

MEDIA_URL = '/media/'

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)

SECRET_KEY = '{{ secret_key }}'

SITE_ID = 1
SITE_TITLE = _('Пассажирские перевозки')

USE_I18N = True
USE_L10N = False
USE_TZ = True
TIME_ZONE = 'Asia/Vladivostok'

# Форматы даты/времени для шаблонов Django.
DATE_FORMAT = 'd.m.Y'
TIME_FORMAT = 'G:i'
DATETIME_FORMAT = ' '.join((DATE_FORMAT, TIME_FORMAT))

LANGUAGE_CODE = 'ru'

LANGUAGES = (
    ('ru', _('Russian')),
    # ('en', _('English')),
    # ('zh-cn', _('Simplified Chinese')),
)

USE_MODELTRANSLATION = True
MODELTRANSLATION_DEFAULT_LANGUAGE = 'ru'

ROSETTA_MESSAGES_SOURCE_LANGUAGE_CODE = 'ru'
ROSETTA_MESSAGES_SOURCE_LANGUAGE_NAME = 'Russian'

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale'),
)

ROOT_URLCONF = 'urls'

INSTALLED_APPS = [
    # Указывается перед всеми остальными приложениями
    'modeltranslation',
    # Django apps
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.redirects',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.sitemaps',
    'django.contrib.staticfiles',
    'django.contrib.postgres',
    # Mezzanine apps
    'mezzanine.boot',
    'mezzanine.conf',
    'mezzanine.core',
    'mezzanine.generic',
    'mezzanine.pages',
    'mezzanine.forms',
    # Other apps
    'compressor',
    # 'pytils',
    # 'grappelli',
    'rosetta-grappelli',
    'rosetta',
    # 'widget_tweaks',
    'sorl.thumbnail',
    # Projects apps
    'benefits',
    'bus',
    'common',
    'documents',
    'services',
    'reviews',
]

MIDDLEWARE = [
    # Django middleware
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',
    'common.middleware.AdminLocaleMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # Mezzanine middleware
    'mezzanine.core.middleware.UpdateCacheMiddleware',
    'mezzanine.core.request.CurrentRequestMiddleware',
    'mezzanine.core.middleware.RedirectFallbackMiddleware',
    'mezzanine.core.middleware.AdminLoginInterfaceSelectorMiddleware',
    'mezzanine.core.middleware.SitePermissionMiddleware',
    'mezzanine.pages.middleware.PageMiddleware',
    'mezzanine.core.middleware.FetchFromCacheMiddleware',
]

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.debug',
                'django.template.context_processors.i18n',
                'django.template.context_processors.static',
                'django.template.context_processors.media',
                'django.template.context_processors.request',
                'django.template.context_processors.tz',
                'mezzanine.conf.context_processors.settings',
                'mezzanine.pages.context_processors.page',
            ],
            'builtins': [
                'mezzanine.template.loader_tags',
            ],
        },
    },
]

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.'
                'NumericPasswordValidator',
    },
]

# Настройки Mezzanine
PACKAGE_NAME_FILEBROWSER = 'filebrowser_safe'
PACKAGE_NAME_GRAPPELLI = 'grappelli_safe'

OPTIONAL_APPS = (
    PACKAGE_NAME_FILEBROWSER,
    PACKAGE_NAME_GRAPPELLI,
)

FILEBROWSER_ESCAPED_EXTENSIONS = ('html',)

BLOG_USE_FEATURED_IMAGE = True

AUTHENTICATION_BACKENDS = ('mezzanine.core.auth_backends.MezzanineBackend',)

PAGE_MENU_TEMPLATES = (
    (1, 'Главное меню', 'pages/menus/main_menu.html'),
    (2, 'Нижнее меню', 'pages/menus/footer_menu.html'),
)

SLUGIFY = 'pytils.translit.slugify'

RICHTEXT_ALLOWED_TAGS = (
    'a', 'abbr', 'acronym', 'address', 'area', 'b', 'bdo', 'big',
    'blockquote', 'br', 'button', 'caption', 'center', 'cite', 'code',
    'col', 'colgroup', 'dd', 'del', 'dfn', 'dir', 'div', 'dl', 'dt',
    'em', 'fieldset', 'font', 'form', 'figure', 'h1', 'h2', 'h3', 'h4', 'h5',
    'h6', 'hr', 'i', 'img', 'input', 'ins', 'iframe', 'kbd', 'label', 'legend',
    'li', 'map', 'menu', 'ol', 'optgroup', 'option', 'p', 'pre', 'q',
    's', 'section', 'script', 'samp', 'select', 'small', 'span', 'strike',
    'strong', 'sub', 'sup', 'table', 'tbody', 'td', 'textarea', 'tfoot', 'th',
    'thead', 'tr', 'tt', 'u', 'ul', 'var', 'wbr'
)

RICHTEXT_ALLOWED_ATTRIBUTES = (
    'abbr', 'accept', 'accept-charset', 'accesskey', 'action',
    'align', 'alt', 'axis', 'border', 'cellpadding', 'cellspacing',
    'char', 'charoff', 'charset', 'checked', 'cite', 'class', 'clear',
    'cols', 'colspan', 'color', 'compact', 'coords', 'data-tab', 'datetime',
    'dir', 'disabled', 'enctype', 'for', 'frame', 'headers', 'height', 'href',
    'hreflang', 'hspace', 'id', 'ismap', 'label', 'lang', 'longdesc',
    'maxlength', 'media', 'method', 'multiple', 'name', 'nohref',
    'noshade', 'nowrap', 'prompt', 'readonly', 'rel', 'rev', 'rows',
    'rowspan', 'rules', 'scope', 'selected', 'shape', 'size', 'span',
    'src', 'start', 'style', 'summary', 'tabindex', 'target', 'title',
    'type', 'usemap', 'valign', 'value', 'vspace', 'width', 'xml:lang'
)

TINYMCE_SETUP_JS = 'js/mezzanine/tinymce_setup.js'

TINYMCE_DEFAULT_CONFIG = {
    'theme': 'advanced',
    'relative_urls': False,
    'language': 'ru',
}

THUMBNAIL_COLORSPACE = None
THUMBNAIL_PRESERVE_FORMAT = True

ADMIN_MENU_ORDER = (
    ('Основные данные', (
        'pages.Page',
        ('Картинки на главной', 'common.IndexPagePicture'),
        ('Преимущества', 'benefits.Benefit'),
        ('Услуги', 'services.Service'),
        ('Автобусы', 'bus.Bus'),
        ('Отзывы', 'reviews.Review'),
        ('Документы', 'documents.Document'),
    )),
    ('Материалы сайта', (
        ('Медиа-библиотека', 'fb_browse'),
        ('Перевод текста', 'rosetta-file-list-redirect'),
    )),
    ('Дополнительно', (
        'conf.Setting',
        'sites.Site',
        'auth.User',
        'auth.Group',
        'redirects.Redirect',
    )),
)

ADMIN_REMOVAL = [
    'mezzanine.generic.models.ThreadedComment',
]

# Не показывать настройки:
ADMIN_REMOVAL_SETTINGS = [
    'ADMIN_MENU_COLLAPSED', 'AKISMET_API_KEY', 'BITLY_ACCESS_TOKEN',
    'COMMENTS_ACCOUNT_REQUIRED', 'COMMENTS_DEFAULT_APPROVED',
    'COMMENTS_DISQUS_API_PUBLIC_KEY', 'COMMENTS_DISQUS_API_SECRET_KEY',
    'COMMENTS_DISQUS_SHORTNAME', 'COMMENTS_NOTIFICATION_EMAILS',
    'COMMENTS_NUM_LATEST', 'COMMENTS_REMOVED_VISIBLE',
    'COMMENTS_UNAPPROVED_VISIBLE',
    'GOOGLE_ANALYTICS_ID',
    # 'MAX_PAGING_LINKS',
    'RATINGS_ACCOUNT_REQUIRED',
    'RICHTEXT_FILTER_LEVEL', 'SEARCH_PER_PAGE',
    'TAG_CLOUD_SIZES',
]

try:
    from mezzanine.utils.conf import set_dynamic_settings
except ImportError:
    pass
else:
    set_dynamic_settings(globals())
