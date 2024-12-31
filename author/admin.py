from django.contrib import admin
from author.models import Author
# Register your models here.
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
  list_display=['id','name','address','phone','department']
  search_fields=['id','name'] 