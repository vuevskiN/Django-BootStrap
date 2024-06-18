from django.contrib import admin
from .models import Book, Author


# Register your models here.

class BookInline(admin.TabularInline):
    model = Book.authors.through
    extra = 1


class AuthorAdmin(admin.ModelAdmin):
    inlines = [BookInline]

    def has_add_permission(self, request):
        if request.user.is_superuser:
            return True
        return False


class BookAdmin(admin.ModelAdmin):
    exclude = ['authors', 'user', ]
    search_fields = ['description', ]

    def save_model(self, request, obj, form, change):
        obj.user = request.user
        return super(BookAdmin, self).save_model(request, obj, form, change)

    def has_change_permission(self, request, obj=None):
        if obj and obj.user == request.user:
            return True
        return False


admin.site.register(Book, BookAdmin)
admin.site.register(Author, AuthorAdmin)
