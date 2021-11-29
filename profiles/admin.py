from django.contrib import admin
from .models import Suggestion


class SuggestionAdmin(admin.ModelAdmin):
    """
    Admin configuration for Suggestion model
    """
    list_display = (
        'user',
        'suggestion'
    )
      
    ordering = ['user', 'suggestion']

admin.site.register(Suggestion, SuggestionAdmin)
