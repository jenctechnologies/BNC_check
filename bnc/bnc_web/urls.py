from django.urls import path,include
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.auth import views as auth_views



app_name = 'bnc'

urlpatterns = [
    path('home', views.index, name='index'),
    path('service', views.service_page, name='service'),
    path('sign_up', views.sign_up_page, name='sign_up'),
    path('sign_in', views.sign_in_page, name='sign_in'),
    path('team', views.meet_our_team, name='team'),
    path('mail', views.send_mail, name='mail'), 
    path('admin/', admin.site.urls),
    path('careers', views.join_our_team, name='careers'), 
    path('meet', views.meetings, name='meetings'), 
    path('meet-details', views.meeting_details, name='meet-details'), 
    path('event', views.events, name='event'), 
    path('event_gallery', views.upload_index, name='event'), 
    path('user_form/get_next_register_id/', views.get_next_register_id, name='get_next_register_id'),
    path('upload_image', views.upload_index, name = 'upload_image'),
    path('upload/', views.fileupload, name = "File_Uploads"),
    path('profile_card', views.service_details, name = "profile_card"),
    path('user_form', views.user_form, name = "user_form"),
    path('user_profile', views.user_profile, name = "user_profile"),
    path('meeting_assign', views.meeting_assignment, name = "meeting_assign"),
    path('event_assign', views.event_assignment, name = "event_assign"),
    path('logout/', views.logout_view, name='logout'),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)