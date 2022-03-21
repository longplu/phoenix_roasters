from . import views
from django.urls import path

urlpatterns = [ 
	path('', views.home, name='home'),
	
	path('about/', views.about, name='about'),
	path('contactus/', views.contactus, name='contactus'),
	path('location/', views.location, name='location'),
	
	path('products/', views.products_index, name="index"),
	path('products/<int:product_id>/', views.products_detail, name="detail"),
	path('products/create/', views.ProductCreate.as_view(), name='products_create'),
	path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='products_update'),
	path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='products_delete'),

	path('shoppingcarts/', views.shoppingcarts_index, name='shoppingcarts_index'),
	path('shoppingcarts/add/<int:product_id>/', views.shoppingcarts_add, name='shoppingcarts_add'),
	path('shoppingcarts/update/<int:product_id>/', views.shoppingcarts_update, name='shoppingcarts_update'),


	path('checkouts/', views.checkouts_index, name='checkouts_index'),

	path('account/signup', views.signup, name='signup')
]