from django.urls import path
from . import views

app_name = 'blog'  # creates a namespace for this app

# define what will be viewed
urlpatterns = [
   # display home page
   path('', views.index, name='index'), # calls for index.html through views.py
   # display a specific blog
   path('<int:blog_id>/', views.post, name='post') # will call for post.html through views.py
]
