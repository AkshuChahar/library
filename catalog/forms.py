from django import forms
from catalog.models import Book

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ('book_name', 'author', 'isbn')