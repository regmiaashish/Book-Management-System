from django.shortcuts import render,redirect
from book.models import Book,Publication,Genre
from book.forms import BookForm,Genreform,PublicationForm
# Create your views here.
def book_list(request):
  content= {'data':Book.objects.filter(is_published=True)}
  return render(request,'book/index.html',content)

def book_create(request):
    # print(request.POST)
    form = BookForm()
    if request.method == "POST":
        form = BookForm(request.POST,request.FILES or None)
        if form.is_valid():
            form.save()
            return redirect("/book/booklist")
        else:
            return form.errors

    info = {"data": "Form FillUp", "form": form}
    return render(request, "book/create.html", info)

def edit_book(request, id):
    book_publish = Book.objects.get(id=id)
    form = BookForm(instance=book_publish)
    if request.method == "POST":
        form = BookForm(
            request.POST, request.FILES or None, instance=book_publish
        )
        if form.is_valid():
            form.save()
            return redirect("/book/booklist")
        else:
            return form.errors
    
    context = {"data": book_publish, "form": form}
    return render(request, "book/edit.html", context)

def view_book(request,id):
    reader = Book.objects.get(id=id)

    context={
        'data':reader
    }
    return render(request,'book/view.html',context)
  
  
def delete_book(request,id):
    delete = Book.objects.get(id=id).delete()
    return redirect("/book/booklist")

#views for the Genre models

def genre_list(request):
    data={'info':Genre.objects.all()}
    return render(request,'genre/list.html',data)


def create_genre(request):
    form = Genreform()
    if request.method == "POST":
        form = Genreform(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/book/genre/list")
        else:
            return form.errors

    info = {"data": "Form FillUp", "form": form}
    return render(request, "genre/create.html", info)


def edit_genre(request,id):
    formdata=Genre.objects.get(id=id)
    form = Genreform(instance=formdata)
    if request.method == "POST":
        form = Genreform(request.POST,request.FILES or None,instance=formdata)
        if form.is_valid():
            form.save()
            return redirect("/book/genre/list")
        else:
            return form.errors

    info = {"data":formdata, "form": form}
    return render(request, "genre/edit.html", info)

def delete_genre(request,id):
    Genre.objects.get(id=id).delete()
    return redirect("/book/genre/list")




##views for publication

def list_publication(request):
    publication = Publication.objects.filter(is_active=True)
    context = {
        "publication":publication
    }
    return render(request,'publication/index.html',context)


def create_publication(request):
    form = PublicationForm()
    if request.method == 'POST':
        form = PublicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/book/publication/list')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request,'publication/create.html',context)

def edit_publication(request,id):
    data = Publication.objects.get(id=id)
    form = PublicationForm(instance=data)
    if request.method == 'POST':
        form = PublicationForm(request.POST,instance=data)
        if form.is_valid():
            form.save()
            return redirect('/book/publication/list')
        else:
            print(form.errors)
        
    context = {'form':form}
    return render(request,'publication/edit.html',context)

def delete_publication(request,id):
    Publication.objects.get(id=id).delete()
    return redirect('/book/publication/list')






