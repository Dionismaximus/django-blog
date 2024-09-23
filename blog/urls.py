from . import views
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path("about/", include("about.urls"), name="about-urls"),
    path('', views.PostList.as_view(), name='home'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
]