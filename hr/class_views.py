from django.views import View
from django.views.generic import TemplateView, ListView
from . models import Book

from django.http import HttpResponse


class HelloView(View):
    def get(self, request):
        return HttpResponse("<h1>Hello from HelloView class </h1>")


class HelloView2(TemplateView):
    template_name = "hello.html"


class ListBooks(ListView):
   model = Book
   queryset =  Book.objects.order_by("price")
   template_name = "listbooks.html"  # def is  hr/book_list.html
   context_object_name = "books"
   # books = Book.objects.all()
   # keye = {'object_list' : books}
   # render(request,template_name,keys)
