from django.contrib import admin
from view.models import ExampleModel, IndexPageModel, ServiceModel
from core.settings import NAME_SITE


admin.site.site_header = NAME_SITE
admin.site.site_title = NAME_SITE
admin.site.index_title = NAME_SITE



# Register your models here.
admin.site.register(ServiceModel)
admin.site.register(IndexPageModel)
admin.site.register(ExampleModel)
