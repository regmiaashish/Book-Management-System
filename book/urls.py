from django.urls import path
from book.views import( book_list,
                       edit_book,
                       book_create,
                       view_book,
                       delete_book,
                       genre_list,
                       create_genre,
                       edit_genre,
                       delete_genre,
                       list_publication,
                       create_publication,
                       edit_publication,
                       delete_publication,
                       
                       
)

urlpatterns=[
   path('genre/list',genre_list,name="genre list"),
   path('genre/form',create_genre,name="genre form"),
   path('genre/edit<id>',edit_genre,name="edit genre"),
   path('genre/delete<id>',delete_genre,name="delete genre"),
   path("publication/list",list_publication,name="publication list"),
   path("publication/form",create_publication,name="publication form"),
   path("publication/edit<id>",edit_publication,name="publication edit"),
   path("publication/delete<id>",delete_publication,name="publication delete"),
   path("booklist/", book_list, name="list_book"),
   path("bookform", book_create, name="create_book"),
   path("bookedit/<id>", edit_book, name="edit_book"),
   path("bookdelete/<id>", delete_book, name="delete_book"),
   path("bookview/<id>", view_book, name="view book"),
  
]