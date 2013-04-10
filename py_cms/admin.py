from django.contrib import admin
from py_cms.search import models

class SearchKeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.SearchKeyword, SearchKeywordAdmin)
