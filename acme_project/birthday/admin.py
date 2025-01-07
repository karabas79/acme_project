from django.contrib import admin

from .models import Birthday, Tag


class TagAdmin(admin.ModelAdmin):
    list_display = ('tag',)


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_editable = (
        'last_name',
    )
    list_display_links = ('first_name',)


admin.site.register(Birthday, BirthdayAdmin)
admin.site.register(Tag, TagAdmin)

admin.site.empty_value_display = 'Не задано'
