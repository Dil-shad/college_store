from django.urls import path
from . import views

urlpatterns = [
    path('',views.index,name="index"),
    path('profile',views.profile,name="profile"),
    #ajax_url
    path('get_courses/', views.get_courses, name='get_courses'),

    
    path('login/',views.login,name="login"),
    path('logout/',views.logout,name="logout"),
    path('signup/',views.register,name="signup"),
]
