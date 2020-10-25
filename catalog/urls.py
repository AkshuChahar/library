from django.conf.urls import url
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls, name='admin'),
    path('', views.index, name='index'),
    path('books/', views.BookListView.as_view(), name='books'),
    path('students/', views.StudentListView.as_view(), name='student'),
    path('books/<int:pk>', views.BookDetailView.as_view(), name='book-detail'),
    path('students/<int:pk>', views.StudentDetailView.as_view(), name='student-detail'),
    path('issued/', views.LoanedBookByUserListView.as_view(), name='issued'),
]
