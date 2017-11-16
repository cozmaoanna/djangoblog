from django.conf.urls import url
from .views import blogposts, viewpost, newpost, editpost

urlpatterns = [
    url(r'^posts$', blogposts, name="posts"),
    url(r'posts/(\d+)$', viewpost, name="viewpost"),
    url(r'posts/add', newpost, name="newpost"),
    url(r'posts/(\d+)/edit', editpost, name="editpost"),


]
