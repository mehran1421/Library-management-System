from django.contrib import admin
from .models import Book,Category,Issue


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('position', 'title', 'slug', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')


admin.site.register(Category, CategoryAdmin)


class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'author', 'created','category_to_string', 'status')
    list_filter = (['status'])
    search_fields = ('title', 'slug')


admin.site.register(Book, BookAdmin)


class IssueAdmin(admin.ModelAdmin):
    list_display = ('slugBook', 'slugUser', 'created', 'renewCount','is_on_time')
    search_fields = ('slugBook', 'slugUser')


admin.site.register(Issue, IssueAdmin)


