from django.contrib import admin

from .models import Birthday


# class IceCreamInline(admin.StackedInline):
#     model = IceCream
#     extra = 0


# class CategoryAdmin(admin.ModelAdmin):
#     inlines = (
#         IceCreamInline,
#     )
#     list_display = (
#         'title',
#     )


class BirthdayAdmin(admin.ModelAdmin):
    list_display = (
        'first_name',
        'last_name',
        'birthday',
    )
    list_editable = (
        'first_name',
        'last_name',
        'birthday',
    )
    # search_fields = ('title',)
    # list_filter = ('category',)
    # list_display_links = ('title',)
    # filter_horizontal = ('toppings',)


# admin.site.register(Category, CategoryAdmin)
admin.site.register(Birthday)
# admin.site.register(Wrapper)
# admin.site.register(IceCream, IceCreamAdmin)

admin.site.empty_value_display = 'Не задано'
