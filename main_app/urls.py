from django.urls import path
from . import views

urlpatterns = [ 
	path('', views.home, name='home'),
	path('about/', views.about, name='about'),
	path('contactus/', views.contact, name='contactus'),
	path('location/', views.location, name='location'),
	path('products/', views.products_index, name="index"),
	
	path('products/<int:product_id>/', views.products_detail, name="detail"),
	path('products/create/', views.ProductCreate.as_view(), name='product_create'),
	path('products/<int:pk>/update/', views.ProductUpdate.as_view(), name='products_update'),
	path('products/<int:pk>/delete/', views.ProductDelete.as_view(), name='products_delete'),

	path('account/signup/', views.signup, name='signup')
]