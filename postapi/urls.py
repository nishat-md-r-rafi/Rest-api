from django.urls import path
from . import views
from .views import PostListCreateView

urlpatterns = [path('', PostListCreateView.as_view(),
                    name="pizzeria_list"),
               path('signup/', views.signup),
               path('login/', views.login), ]
