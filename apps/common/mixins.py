from django.contrib.contenttypes.models import ContentType
from django.views.generic.edit import FormMixin

# from common.forms import SearchForm
# from common.models import PhoneNumber, EmailAddress
#
#
# class PhoneNumberMixin(object):
#     @property
#     def phones(self):
#         """
#         Получает ContentType для связной модели
#         и возвращает список телефонов для экземпляра
#         этой модели
#
#         :return: QuerySet с номерами телефонов
#         :rtype: QuerySet
#         """
#         ctype = ContentType.objects.get_for_model(self.__class__)
#         try:
#             phones = PhoneNumber.objects.filter(
#                 content_type__pk=ctype.id, object_id=self.id
#             )
#         except PhoneNumber.DoesNotExist:
#             phones = None
#         return phones
#
#
# class EmailAddressMixin(object):
#     @property
#     def emails(self):
#         """
#         Получает ContentType для связной модели
#         и возвращает список телефонов для экземпляра
#         этой модели
#
#         :return: QuerySet с номерами телефонов
#         :rtype: QuerySet
#         """
#         ctype = ContentType.objects.get_for_model(self.__class__)
#         try:
#             emails = EmailAddress.objects.filter(
#                 content_type__pk=ctype.id, object_id=self.id
#             )
#         except EmailAddress.DoesNotExist:
#             emails = None
#         return emails
#
#
# class SearchFormMixin(FormMixin):
#     """
#     Примесь для добавления формы поиска к View
#     """
#     form_class = SearchForm
#
#     def is_form_submitted(self):
#         """
#         Возвращает `True`, если форма уже отправлена. И `False` иначе.
#
#         :return: bool
#         """
#         return bool(self.request.method == 'GET' and self.request.GET)
#
#     def get_form_kwargs(self):
#         """
#         Добавляет данные GET запроса в аргументы формы,
#         если форма уже отправлена
#
#         :return: dict
#         """
#         kwargs = super(SearchFormMixin, self).get_form_kwargs()
#
#         if self.is_form_submitted():
#             kwargs.update({
#                 'data': self.request.GET,
#             })
#         return kwargs
