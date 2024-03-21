from django.contrib import admin
from .models import Phrase


class PhraseAdmin(admin.ModelAdmin):
    list_display = ['id', 'phrase', 'is_used']
    list_filter = ['is_used']


admin.site.register(Phrase, PhraseAdmin)
