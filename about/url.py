from . import views
from about import views as about_views

urlpatterns = [
    path('', views.about_me, name='about'),
]
