from django.contrib import admin
from .models import * # Import your actual model
from .forms import *

@admin.register(open_cat)
class OpenCatAdmin(admin.ModelAdmin):
    list_display = ('open_categories',)

@admin.register(superior_team)
class SuperiorTeamAdmin(admin.ModelAdmin):
    list_display = ('id','members_image', 'business_type', 'instagram_link', 'whatsapp_number',"position")

@admin.register(founder)
class FounderAdmin(admin.ModelAdmin):
    list_display = ('founder_name', 'founder_business_type','instagram_link', 'whatsapp_number')

@admin.register(president)
class PresidentAdmin(admin.ModelAdmin):
    list_display = ('president_name', 'president_business_type','instagram_link', 'whatsapp_number')

@admin.register(vice_president)
class VicePresidentAdmin(admin.ModelAdmin):
    list_display = ('vice_president_name', 'vice_president_business_type','instagram_link', 'whatsapp_number')

@admin.register(secretary)
class SecretaryAdmin(admin.ModelAdmin):
    list_display = ('secretary_name', 'secretary_business','instagram_link', 'whatsapp_number')

@admin.register(coordinate_team)
class coordinateTeamAdmin(admin.ModelAdmin):
    list_display = ('id','members_image', 'business_type', 'instagram_link', 'whatsapp_number',"position")


@admin.register(bnc_register_mem)
class bnc_registers(admin.ModelAdmin):
    list_display = ['id', 'name','gmail']

@admin.register(Image)
class ImageAdmin(admin.ModelAdmin):
    list_display = ('title', 'pic')
@admin.register(UserProfile)
class UserProfileAdmin(admin.ModelAdmin):
    list_display = ("id",'username', 'email_address', 'first_name', 'last_name', 'brand_name', 'service_name')
    search_fields = ('username', 'email_address', 'brand_name', 'service_name')


@admin.register(meeting_assign)
class MeetingAdmin(admin.ModelAdmin):
    form = MeetingForm
    list_display = ('Id', 'meet_date', 'meet_time', 'meeting_title')
    search_fields = ('meeting_title',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('id', 'event_name', 'event_date', 'event_time')  # Customize the displayed fields in the admin list view
    search_fields = ('event_name',)  # Enable searching by event name in the admin

