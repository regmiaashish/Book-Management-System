from django.urls import path
from author.views import (
    list_author,
    create_author,
    edit_author,
    delete_author

)

urlpatterns=[
    path("list", list_author, name="list-author"),
    path("create_author", create_author, name="create-author"),
    path("edit_author/<id>", edit_author, name="edit-author"),
    path("delete_author/<id>", delete_author, name="delete-author"),
]