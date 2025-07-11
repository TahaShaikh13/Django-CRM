from django.urls import path
from . import views

urlpatterns = [
    path('',views.homepage, name='homepage'),
    # path('login/',views.li, name='login'),
    path('logout/',views.lo, name='logout'),
    path('register/',views.register, name='register'),
    path('register/',views.register, name='register'),
    path('data/<int:pk>',views.customer_data, name='data'),
    path('delete_data/<int:pk>',views.delete_data, name='delete_data'),
    path('add_data/',views.add_data, name='add_data'),
    path('update_data/<int:pk>',views.update_data, name='update_data'),
]