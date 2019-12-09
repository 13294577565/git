from django.urls import path
from . import views
urlpatterns = [
    path('',views.aa,name='aa'),
    path('login/',views.login ,name='login'),
    path('index/',views.index,name='index'),
    path("zy/",views.zy,name='zy'),
    path('hsj/',views.hsj,name='hsj'),
]
