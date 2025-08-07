from django.urls import path
from django.http import HttpResponse
from django.core.management import call_command
from . import views

# def run_migrations (request):
#     try:
#         call_command('migrate')
#         return HttpResponse("Migrations successful.")
#     except Exception as e:
#         return HttpResponse(f"Migration error: {str(e)}")
    
# def collect_static (request):
#     try:
#         call_command('collectstatic',interactive=False)
#         return HttpResponse("static files collevted.")
#     except Exception as e:
#         return HttpResponse(f"Static collection error: {str(e)}")

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
    path('add_attendence/',views.mark_attendence, name='mark_attendence'),
    path('view_attendence/',views.view_attendence,name='view_attendence'),
    # path('run-migrations/',run_migrations),
    # path('collect-static/',collect_static),
]