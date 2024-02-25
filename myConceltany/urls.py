from django.http import HttpResponse
from django.urls import path
from . import views
urlpatterns = [
    path("index/",views.myHomeView,name = "home page"),
    path('home/',views.showFormViews,name = "home_page_forms"),
    path('success/',views.success,name = 'success'),
]
