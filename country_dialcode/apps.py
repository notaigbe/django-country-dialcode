from django.apps import AppConfig
from django.utils.translation import gettext_lazy as _


class CountryDialcodeConfig(AppConfig):
    name = 'country_dialcode'
    verbose_name = _('Country Dialcode')
