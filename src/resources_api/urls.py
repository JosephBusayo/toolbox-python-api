from django.urls import path
from .views import ResourceList, ResourceDetail

app_name = 'blog_api'

urlpatterns = [
    path('', ResourceList.as_view(), name='resourcelist'),
    path('<int:pk>/', ResourceDetail.as_view(), name='resourcedetail'),
]
