from django import forms
from book.models import Book,Genre,Publication
class BookForm(forms.ModelForm):
  class Meta:
    model=Book
    fields='__all__'
    
class Genreform(forms.ModelForm):
  class Meta:
    model=Genre
    fields='__all__'
    
class PublicationForm(forms.ModelForm):
    class Meta:
        model = Publication
        fields = '__all__'