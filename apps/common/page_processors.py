# coding=utf-8
from mezzanine.pages.page_processors import processor_for

from benefits.models import Benefit
from bus.models import Bus
from common.models import IndexPagePicture
from documents.models import Document
from reviews.models import Review
from services.models import Service


@processor_for('/')
def index(request, page):
    """
    Дополнительный контекст для главной страницы:
    main_picture: главная картинка
    benefits: список преимуществ
    services: список услуг
    bus_list: список автобусов
    reviews: список отзывов
    documents: список документов
    """
    main_picture = IndexPagePicture.objects.filter(
        position=IndexPagePicture.MAIN, file__isnull=False).first()
    benefits = Benefit.objects.order_by('title')
    services = Service.objects.order_by('title')
    bus_list = Bus.objects.published().order_by('-capacity', 'title')
    reviews = Review.objects.order_by('?')
    documents = Document.objects.order_by('caption')

    return {
        'main_picture': main_picture,
        'benefits': benefits,
        'services': services,
        'bus_list': bus_list,
        'reviews': reviews,
        'documents': documents,
    }
