# -*- coding: utf-8 -*-
from mezzanine.conf import register_setting

register_setting(
    name='AA_EMAIL',
    label='Электронная почта',
    description='Адреса электронной почты через запятую',
    editable=True,
    translatable=False,
    default='amurauto@example.com',
)

register_setting(
    name='AA_PHONE',
    label='Основной телефон',
    description='',
    editable=True,
    translatable=False,
    default='(4212) 64-15-64',
)

register_setting(
    name='AATOP_SLOGAN',
    label='Слоган',
    description='Слоган в начале страницы',
    editable=True,
    translatable=True,
    default='Слоган в начале страницы',
)

register_setting(
    name='AATOP_TEXT',
    label='Текст',
    description='Мелкий текст под слоганом в начале страницы',
    editable=True,
    translatable=True,
    default='Мелкий текст под слоганом в начале страницы',
)

register_setting(
    name='AATOP_BUTTON',
    label='Кнопка',
    description='Кнопка',
    editable=True,
    translatable=True,
    default='Поехали дальше!',
)

register_setting(
    name='AASECOND_CAPTION',
    label='Заголовок',
    description='Заголовок на втором поле',
    editable=True,
    translatable=True,
    default='Заголовок',
)

register_setting(
    name='AASECOND_TEXT',
    label='Текст',
    description='Мелкий текст на втором поле',
    editable=True,
    translatable=True,
    default='Мелкий текст',
)

register_setting(
    name='AASECOND_BUTTON',
    label='Кнопка',
    description='Кнопка',
    editable=True,
    translatable=True,
    default='Мы предлагаем',
)

register_setting(
    name='AA_BENEFITS_CAPTION',
    label='Заголовок для преимуществ',
    description='Заголовок для раздела о преимуществах',
    editable=True,
    translatable=True,
    default='Наши преимущества',
)

register_setting(
    name='AA_BENEFITS_BUTTON',
    label='Кнопка в преимуществах',
    description='Кнопка в конце преимуществ',
    editable=True,
    translatable=True,
    default='Предлагаем качественный сервис',
)

register_setting(
    name='AA_SERVICES_CAPTION',
    label='Заголовок для услуг',
    description='Заголовок для раздела об услугах',
    editable=True,
    translatable=True,
    default='Наши услуги',
)

register_setting(
    name='AA_BUS_CAPTION',
    label='Заголовок для автобусов',
    description='',
    editable=True,
    translatable=True,
    default='Наши автобусы',
)

register_setting(
    name='AA_REVIEWS_CAPTION',
    label='Заголовок для отзывов',
    description='',
    editable=True,
    translatable=True,
    default='Что говорят о нас клиенты:',
)

register_setting(
    name='AA_DOCS_CAPTION',
    label='Текст для документов',
    description='',
    editable=True,
    translatable=True,
    default='Имеем полный пакет документов на оказание услуг',
)

register_setting(
    name='AA_DOCS_BUTTON',
    label='Текст кнопки для документов',
    description='',
    editable=True,
    translatable=True,
    default='Просмотреть документы',
)

register_setting(
    name='AA_DOCS_BLANC',
    label='Текст кнопки для скачивания бланка договора',
    description='',
    editable=True,
    translatable=True,
    default='Бланк договора',
)

register_setting(
    name='AA_DOCS_BLANC_FILE',
    label='Имя файла бланка договора',
    description='',
    editable=True,
    translatable=True,
    default='',
)

register_setting(
    name='AA_CONTACT_CAPTION',
    label='Заголовок для контактов',
    description='',
    editable=True,
    translatable=True,
    default='Как с нами связаться',
)

register_setting(
    name='AA_CONTACT_TEXT',
    label='Текст для контактов',
    description='',
    editable=True,
    translatable=True,
    default="Мы находимся в Хабаровске.<br>Хотите заказать автобус? "
            "Позвоните нам или напишите в What's App.",
)

register_setting(
    name='AA_CONTACT_PHONE',
    label='Телефоны для контактов',
    description='Телефоны для контактов',
    editable=True,
    translatable=False,
    default='64-15-64',
)

register_setting(
    name='AA_CONTACT_WHATSAPP_1',
    label="Телефоны для What's App (1)",
    description="What's App для контактов",
    editable=True,
    translatable=False,
    default='+7(962) 220-06-46',
)

register_setting(
    name='AA_CONTACT_WHATSAPP_2',
    label="Телефоны для What's App (2)",
    description="What's App для контактов",
    editable=True,
    translatable=False,
    default='+7(914) 770-87-66',
)

register_setting(
    name='AA_CONTACT_EMAIL',
    label='Электропочта для контактов',
    description='Электронная почта для контактов',
    editable=True,
    translatable=False,
    default='abmorgunov@mail.ru',
)

register_setting(
    name='AA_ABOUT_CODE',
    label='Код текста для раздела "О компании"',
    description='Код текста для раздела "О компании"',
    editable=True,
    translatable=True,
    default='',
)

register_setting(
    name='TEMPLATE_ACCESSIBLE_SETTINGS',
    description='Sequence of setting names available within templates.',
    editable=False,
    default=(
        # Значения по умолчанию
        'ACCOUNTS_APPROVAL_REQUIRED', 'ACCOUNTS_VERIFICATION_REQUIRED',
        'ADMIN_MENU_COLLAPSED', 'BITLY_ACCESS_TOKEN',
        'BLOG_USE_FEATURED_IMAGE',
        'COMMENTS_DISQUS_SHORTNAME', 'COMMENTS_NUM_LATEST',
        'COMMENTS_DISQUS_API_PUBLIC_KEY', 'COMMENTS_DISQUS_API_SECRET_KEY',
        'COMMENTS_USE_RATINGS', 'DEV_SERVER', 'FORMS_USE_HTML5',
        'GRAPPELLI_INSTALLED', 'GOOGLE_ANALYTICS_ID',
        'JQUERY_FILENAME', 'JQUERY_UI_FILENAME', 'LOGIN_URL', 'LOGOUT_URL',
        'SITE_TITLE', 'SITE_TAGLINE', 'USE_L10N', 'USE_MODELTRANSLATION',
        # Дополнительные настройки
        'AA_EMAIL', 'AA_PHONE',
        'AATOP_SLOGAN', 'AATOP_TEXT', 'AATOP_BUTTON',
        'AASECOND_CAPTION', 'AASECOND_TEXT', 'AASECOND_BUTTON',
        'AA_BENEFITS_CAPTION', 'AA_BENEFITS_BUTTON', 'AA_SERVICES_CAPTION',
        'AA_BUS_CAPTION', 'AA_REVIEWS_CAPTION',
        'AA_DOCS_CAPTION', 'AA_DOCS_BUTTON',
        'AA_DOCS_BLANC', 'AA_DOCS_BLANC_FILE',
        'AA_CONTACT_CAPTION', 'AA_CONTACT_TEXT',
        'AA_CONTACT_PHONE', 'AA_CONTACT_WHATSAPP_1', 'AA_CONTACT_WHATSAPP_2',
        'AA_CONTACT_EMAIL', 'AA_ABOUT_CODE',
    ),
)
