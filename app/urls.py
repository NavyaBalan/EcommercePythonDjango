from django.urls import path

from .import views

urlpatterns = [
  
  path('',views.home,name='home'),
  path('vegetables/', views.vegetable_category, name='vegetable_category'),
  path('fruits/', views.fruit_category, name='fruit_category'),
  path('product/<int:product_id>/', views.product_details, name='product_details'),
  path('addtocart/<int:prod_id>/', views.addtocart, name='addtocart'),
  path('cart/', views.showCart, name='cart'),
  path('order/', views.viewOrder, name='order'),
  path('search/', views.searchBar, name='search'),
  path('pluscart/',views.pluscart),
  path('minuscart/',views.minuscart),
  path('removecart/',views.removecart),

  path('placeorder/', views.placeorder, name='placeorder'),
  path('address/', views.address, name='address'),
  path('updateAddress/<int:pk>', views.updateAddress, name='updateAddress'),
  path('reg/',views.registers,name='register'),
  path('profile/', views.profileview, name='profileview'),
  
 
  

]