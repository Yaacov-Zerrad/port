from django.contrib import admin
from .settings import NAME_SITE


admin.site.site_header(NAME_SITE)
admin.site.site_title(NAME_SITE)
