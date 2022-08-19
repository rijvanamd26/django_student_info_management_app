from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name='index'),
    path('<int:id>',views.view_student,name='view_student'), #<int:id> -> path convertor that allows us to use dynamic urls eg: ../5 ->django puts this 5(integer) into variable id
    path('add',views.add,name='add'),
    path('edit/<int:id>/',views.edit,name='edit'),
    path('delete/<int:id>/',views.delete,name='delete'),
]
