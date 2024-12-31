from django.shortcuts import render, redirect
from author.models import Author
from author.forms import AuthorForm

# Create your views here.


def list_author(request):
    author = Author.objects.filter(is_active=True)
    context = {"author": author}
    return render(request, "author/index.html", context)


def create_author(request):
    form = AuthorForm()
    if request.method == "POST":
        form = AuthorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("/author/list")
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "author/create.html", context)


def edit_author(request, id):
    data = Author.objects.get(id=id)
    form = AuthorForm(instance=data)
    if request.method == "POST":
        form = AuthorForm(request.POST, instance=data)
        if form.is_valid():
            form.save()
            return redirect("/author/list")
        else:
            print(form.errors)

    context = {"form": form}
    return render(request, "author/edit.html", context)


def delete_author(request, id):
    Author.objects.get(id=id).delete()
    return redirect("/author/list")
