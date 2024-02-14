from django.urls import path
from myusers import views

urlpatterns = [
  path("home/",views.home,name="home_link"),
  path("",views.loginuser,name="login_link"),
  path("logout_user",views.logoutuser,name="logout_link"),
  path("register_user",views.reguser,name="register_link"),
]