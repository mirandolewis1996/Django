from django.urls import path
from member import views


urlpatterns = [
    path("",views.home,name = "home_link"),
    path("list-view/",views.listview,name ="list_link"),
    path("del_view/<int:pk>",views.delpage,name="del_lis_link"),
    path("delete/<int:pk>",views.delmember,name="del_link"),
    path("edit_member/<int:pk>",views.editmember,name="edit_link")
 ]