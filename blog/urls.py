from django.urls import path
from . import views

urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('post/<int:pk>/', views.post_detail, name='post_detail'),
]

# the post/,int pkk sepecifies a url patter
# post means that teh url shoul begin with the word {Post}
#
