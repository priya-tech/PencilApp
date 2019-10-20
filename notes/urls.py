from django.urls import path
from . import views

urlpatterns=[
    path('add/', views.add_note, name='add_notes'),
    path('', views.view_note, name='view_notes'),
    path('delete/<int:id>', views.delete_note, name='delete_notes'),
    path('edit/<str:action>/<int:id>', views.edit_note, name='edit_notes')
]
