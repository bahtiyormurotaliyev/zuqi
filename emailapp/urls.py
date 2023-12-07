from . import views
from django.urls import path

urlpatterns =[
    path('avtomobiles',views.avtomobiles,name='avtomobiles_list.'),
    path('avtomobiles/<string:id>', methods=['GET'], name='book-create'),
    path('avtomobiles/<string:id>/delete', methods=['GET'], name='avtomobile_detail'),
    path('/avtomobiles/new', methods=['GET'], name='create_automobile'),
    path('avtomobiles/create', methods=['POST'])
]