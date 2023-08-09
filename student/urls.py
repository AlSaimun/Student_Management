from django.urls import path,include
from . import views
urlpatterns = [
    path('',views.home,name = 'home'),
    path('add/',views.addStudent,name = 'add'),
    path('delete/<int:id>',views.delete_student,name = 'delete'),
    path('edit/<int:id>',views.update_info,name = 'edit'),
]