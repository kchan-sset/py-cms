from django.contrib import admin
from search import models

class SearchKeywordAdmin(admin.ModelAdmin):
    pass

admin.site.register(models.SearchKeyword, SearchKeywordAdmin)
