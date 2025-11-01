from blog import views
from django.urls import path

app_name = 'blog'

# blog/
urlpatterns = [
    path('post/<int:post_id>/', views.post, name='post'),
    path('', views.blog, name='blog'),
    path('exemplo/', views.exemplo, name='exemplo'),
]
