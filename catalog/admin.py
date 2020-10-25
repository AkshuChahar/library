from django.contrib import admin
from .models import  Book, BookInstance, Student

# Register your models here.

# admin.site.register(Book)
# admin.site.register(BookInstance)

class BookAdmin(admin.ModelAdmin):
    list_display = ('book_name', 'author', 'isbn')
    fields = ['book_name', 'author', 'isbn']

admin.site.register(Book, BookAdmin)

class BookInstanceInline(admin.TabularInline):
    model = BookInstance

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('book', 'status', 'borrower', 'issued', 'returned', 'id')
    list_filter = ('status', 'issued')

    fieldsets = (
        (None, {'fields':('book', 'imprint', 'id')}),
        ('Availablility', {'fields':('status', 'issued', 'borrower')}),
    )

class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'mobile', 'join_date')
    fields = ['first_name', 'last_name', 'mobile', 'join_date']

admin.site.register(Student, StudentAdmin)
