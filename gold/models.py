from django.db import models

# Create your models here.

class ad_section(models.Model):
    section_name = models.CharField(max_length=200)

class ad(models.Model):
    ad_section= models.ForeignKey(ad_section,on_delete=models.CASCADE)
    image_link = models.CharField(max_length=200)
    img_width = models.CharField(max_length=250)
    img_height = models.CharField(max_length=250)
    video_link = models.CharField(max_length=200)
    promo_text= models.CharField(max_length=150)
    call_to_action_text = models.CharField(max_length=250)
    call_to_action_link = models.CharField(max_length=300)

class magazine(models.Model):
    name =models.CharField(max_length=200)
    thumb_firstpage = models.ImageField(upload_to='magazine')

    def __str__(self):
        return self.name

class mag_edition(models.Model):
    magazine =models.ForeignKey(magazine,on_delete=models.CASCADE)
    thumb_firstpage = models.ImageField(upload_to='magazine')
    thumb_secondthird = models.ImageField(upload_to='magazine')
    summary_title = models.CharField(max_length=200)
    summary_para = models.TextField()
    pdf_path= models.CharField(max_length=200)
    latest_section_title =models.CharField(max_length=150)
    previous_section_title = models.CharField(max_length=150)
    edition = models.CharField(max_length=300)
    edition_description = models.CharField(max_length=300)

    def __str__(self):
        return self.edition

class mag_edit_page(models.Model):
    mag_edition = models.ForeignKey(mag_edition,on_delete=models.CASCADE)
    page_number = models.CharField(max_length=100)
    image = models.ImageField(upload_to='magazine')
    

class mag_book_img(models.Model):
#    #mag_book_img.objects.filter(mag = mag__1).mag_images.limit(limit = 10)
    mag= models.ForeignKey(mag_edit_page,related_name='mag_images',on_delete=models.CASCADE)
    Images = models.ImageField("Magazine_Pages", default=" ")


class Subscriber(models.Model):
    name = models.CharField(max_length=250)
    company_name =models.CharField(max_length=200)
    gst_no = models.CharField(max_length=120)
    area_pin_code = models.CharField(max_length=150)
    email = models.EmailField(max_length=140)
    phone = models.CharField(max_length=20)
    username = models.CharField(max_length=200)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username

class subscription(models.Model):
    subscriber = models.ForeignKey(Subscriber, on_delete=models.CASCADE)
    magazine= models.ForeignKey(magazine,on_delete=models.CASCADE)


class activity_type(models.Model):
    name = models.CharField(max_length=250)


class sub_mag_activity(models.Model):
    sma_subscriber = models.ForeignKey(Subscriber,on_delete=models.CASCADE)
    sma_magazine = models.ForeignKey(magazine,on_delete=models.CASCADE)
    sma_activity_type = models.ForeignKey(activity_type,on_delete=models.CASCADE)
    sma_time=models.DateTimeField(auto_now_add=True)



class sub_mag_activity_count(models.Model):
    smac_subscriber = models.ForeignKey(Subscriber,on_delete=models.CASCADE)
    smac_magazine = models.ForeignKey(magazine,on_delete=models.CASCADE)
    smac_activity_type = models.ForeignKey(activity_type,on_delete=models.CASCADE)
    smac_count = models.CharField(max_length=200)



class mag_activity_count(models.Model):
    mac_magazine = models.ForeignKey(magazine,on_delete=models.CASCADE)
    mac_activity_type = models.ForeignKey(activity_type,on_delete=models.CASCADE)
    mac_count = models.CharField(max_length=200)