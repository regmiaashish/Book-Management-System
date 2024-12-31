from django.contrib import admin
from book.models import Book, Publication, Genre


# Register your models here.
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "edition", "price", "created_at"]
    search_fields = ["id", "name"]


@admin.register(Publication)
class PublicationAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "email", "created_at"]
    search_fields = ["id", "name"]


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "created_at"]
    search_fields = ["id", "name"]




from book.models import Department
@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
    list_display = ["id", "name", "is_active", "created_by", "created_at"]
    search_fields = ["name"]
