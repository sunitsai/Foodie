from django.urls import path,include
from . import views
urlpatterns = [

    # Page Url
    path("",views.IndexPage,name="index"),
    path("loginpage/",views.LoginPage,name="loginpage"),
    path("signuppage/",views.SingupPage,name="signuppage"),
    path("signuppagechef/",views.SingupChefPage,name="signupchefpage"),
    path("insert/",views.Insertdata,name="insert"),
    path("login/",views.LoginUser,name="login"),
    path("loginchef/",views.LoginChefPage,name="loginchef"),
    path("show/",views.Showpage,name="show"),
    path("display/<int:pk>",views.DisplayData,name="display"),
    path("edit/<int:pk>",views.EditPage,name="edit"),
    path("update/<int:pk>",views.UpdateData,name="update"),
    path("chefedit/<int:pk>",views.ChefAlldata,name="chefedit"),
    path("chefeditprofile/",views.ChefEditProfilePage,name="chefeditprofile"),
    path("ChefProductadd/",views.ChefProduct_add,name="ChefProductadd"),
    path("add/<int:pk>",views.Addproduct,name="add"),
    path("shoppage/",views.CustomerShop_page,name="shoppage"),
    path("showallproduct/",views.ShowProduct,name="showproduct"),
    path("productdes/<int:pk>",views.ProductDescription,name="productdes"),
    path("shopsinglepage/",views.ShopSinglePage,name="shopsinglepage"),
    path("chefproductpage/",views.Product_Page,name="chefproductpage"),
    path("chefshowproductpage/<int:pk>",views.ChefShowProduct_Page,name="chefshowproductpage"),
    path("editproduct/<int:pk>",views.EditProduct,name="editproduct"),
    path("updateproduct/<int:pk>",views.UpdateProduct,name="updateproduct"),

    
    
]



