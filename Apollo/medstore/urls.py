from django.urls import path
from medstore import views

urlpatterns =[
    path("home/",views.med_home,name="home_link"),
    path("create_medic/",views.med_create,name="Add_link"),
    path("med_list/",views.medlist,name="medlis_link"),
    path("med_detail/<int:pk>",views.medet,name="med_detail_link"),
    path("med_edit/<int:pk>",views.editmed,name="med_edit_link"),
    path("med_delmed/<int:pk>",views.delpage,name="del_page"),
    path("med_del/<int:pk>",views.delmed,name="meddel_link"),
    path("",views.userlogin,name="login_link"),
    path("user_logout/",views.userlogout,name="logout_link"),
    path("user_req/",views.userreg,name="reg_link")
 
]