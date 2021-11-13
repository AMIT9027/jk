

# Register your models here.
from django.contrib import admin
from .models import *
# Register your models here.



@admin.register(ad_section)
class ad_sectionAdmin(admin.ModelAdmin):
    list_display = ['section_name',]

@admin.register(ad)
class adAdmin(admin.ModelAdmin):
    list_display = ['ad_section','image_link','img_width','img_height','video_link','promo_text','call_to_action_text','call_to_action_link']


@admin.register(Subscriber)
class SubscriberAdmin(admin.ModelAdmin):
    list_display=['id','name','company_name','gst_no','area_pin_code','email','phone','username','password']


@admin.register(magazine)
class magazineAdmin(admin.ModelAdmin):
    list_display = ['name','thumb_firstpage']


@admin.register(mag_edition)
class magazineAdmin(admin.ModelAdmin):
    list_display = ['magazine','thumb_firstpage','thumb_secondthird','summary_title','summary_para','pdf_path','latest_section_title','previous_section_title','edition','edition_description']


class mag_image_add(admin.StackedInline):
   model = mag_book_img


@admin.register(mag_edit_page)
class mag_edit_pageAdmin(admin.ModelAdmin):
    inlines = (mag_image_add,)
    list_display = ['mag_edition','page_number','image'] 



@admin.register(activity_type)
class activity_typeAdmin(admin.ModelAdmin):
    list_display = ['name']

@admin.register(sub_mag_activity)
class sub_mag_activityAdmin(admin.ModelAdmin):
    list_display = ['sma_subscriber','sma_magazine','sma_activity_type','sma_time']

@admin.register(sub_mag_activity_count)
class sub_mag_activity_countAdmin(admin.ModelAdmin):
    list_display = ['smac_subscriber','smac_magazine','smac_activity_type','smac_count']

@admin.register(mag_activity_count)
class mag_activity_countAdmin(admin.ModelAdmin):
    list_display = ['mac_magazine','mac_activity_type','mac_count']