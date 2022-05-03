from distutils.command.upload import upload
from django.db import models
from django.utils.timezone import now
from django.utils import timezone
from django.utils.translation import gettext_lazy as _
from .managers import UsersManager
from django.contrib.auth.models import User, AbstractUser, AbstractBaseUser, PermissionsMixin

# Create your models here.
class Job_title(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Country(models.Model):
    USA = 0
    INDIA = 1
    TYPE_CHOICES = (
        (USA, 'USA'),
        (INDIA, 'INDIA')
    )
    id = models.PositiveSmallIntegerField(choices=TYPE_CHOICES, primary_key=True)

    def __str__(self):
        return self.get_id_display()

class City_zip_state(models.Model):
    id = models.AutoField(primary_key=True)
    zipcode = models.CharField(max_length=6, blank=True, null=True)
    city = models.CharField(max_length=50, blank=True, null=True)
    state = models.CharField(max_length=50, blank=True, null=True)
    state_abbr = models.CharField(max_length=2, blank=True, null=True)
    county_area = models.CharField(max_length=50, blank=True, null=True)
    code = models.CharField(max_length=3, blank=True, null=True)
    latitude = models.FloatField(max_length=30, blank=True, null=True)
    longitude = models.FloatField(max_length=30, blank=True, null=True)
    some_field = models.IntegerField(blank=True, null=True)
    tax_rate = models.FloatField(max_length=30, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)

    def __str__(self):
        return self.zipcode

class Roles(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100)
    page_role_column = models.CharField(max_length=100, blank=True, null=True)
    orderby = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.name

class Users(AbstractBaseUser, PermissionsMixin):
    id = models.AutoField(primary_key=True)
    title = models.IntegerField(default=1)
    fname = models.CharField(max_length=100, blank=True, null=True)
    lname = models.CharField(max_length=100, blank=True, null=True)
    cell_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField(_('email address'), unique=True)
    role = models.ForeignKey(Roles, on_delete=models.CASCADE, blank=True, null=True)
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)
    password = models.CharField(max_length=225)
    otp = models.CharField(max_length=10, blank=True, null=True)
    emp_id = models.CharField(max_length=100, blank=True, null=True)
    job_location = models.CharField(max_length=225, blank=True, null=True)
    job_title = models.ForeignKey(Job_title, on_delete=models.CASCADE, blank=True, null=True)
    spouse_name = models.CharField(max_length=225, blank=True, null=True)
    lead_id = models.IntegerField(blank=True, null=True)
    if_lead = models.IntegerField(blank=True, null=True)
    tsize = models.CharField(max_length=5 , blank=True, null=True)
    otc = models.IntegerField(blank=True, null=True)
    oti = models.IntegerField(blank=True, null=True)
    pan = models.CharField(max_length=225, blank=True, null=True)
    aadhar_number = models.CharField(max_length=20, blank=True, null=True)
    ssn = models.CharField(max_length=11, blank=True, null=True)
    driving_licence = models.CharField(max_length=20, blank=True, null=True)
    dl_expiry = models.DateField(blank=True, null=True)
    state_of_issue = models.CharField(max_length=50, blank=True, null=True)
    marital_status = models.IntegerField(blank=True, null=True)
    permanent_zip = models.ForeignKey(City_zip_state, related_name='user_perm_zip', on_delete=models.CASCADE, blank=True, null=True)
    permanent_address = models.CharField(max_length=225, blank=True, null=True)
    resident_zip = models.ForeignKey(City_zip_state, related_name='user_resi_zip', on_delete=models.CASCADE, blank=True, null=True)
    resident_address = models.TextField(blank=True, null=True)
    personal_mobile = models.CharField(max_length=20, blank=True, null=True)
    personal_email = models.EmailField(max_length=50, blank=True, null=True)
    reporting_office = models.CharField(max_length=225, blank=True, null=True)
    job_country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    emg_name = models.CharField(max_length=225, blank=True, null=True)
    emg_number = models.CharField(max_length=225, blank=True, null=True)
    emg_relation = models.IntegerField(blank=True, null=True)
    emg2_name = models.CharField(max_length=225, blank=True, null=True)
    emg2_number = models.CharField(max_length=225, blank=True, null=True)
    emg2_relation = models.IntegerField(blank=True, null=True)
    date_of_joining = models.DateField(blank=True, null=True)
    linkedin = models.TextField(blank=True, null=True)
    blog = models.TextField(blank=True, null=True)
    user_pic = models.ImageField(upload_to='user', blank=True, null=True)
    user_qr = models.ImageField(upload_to='user_qr', blank=True, null=True)
    probation_till = models.DateField(blank=True, null=True)
    resign_date = models.DateField(blank=True, null=True)
    account_number = models.CharField(max_length=20, blank=True, null=True)
    login_token = models.CharField(max_length=225, blank=True, null=True)
    secret_code = models.CharField(max_length=100, blank=True, null=True)
    added_date = models.DateField(auto_now_add=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    USERNAME_FIELD = 'email'
    REQUIRED_FIELD = []

    objects = UsersManager()

    def __str__(self):
        return self.email

class Personal_info(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    caption = models.CharField(max_length=225, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    added_date = models.DateField(auto_now_add=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.name

class User_log(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    field = models.CharField(max_length=225, blank=True, null=True)
    value = models.CharField(max_length=100, blank=True, null=True)
    added_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.field

class User_mg(models.Model):
    id = models.AutoField(primary_key=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    uan = models.CharField(max_length=225, blank=True, null=True)
    esi = models.CharField(max_length=100, blank=True, null=True)
    background = models.CharField(max_length=100, blank=True, null=True)
    pension = models.IntegerField(blank=True, null=True)
    appraisal = models.DateField(blank=True, null=True)
    medical_card = models.TextField(blank=True, null=True)
    added_date = models.DateField(auto_now_add=True)
    
    def __str__(self):
        return self.field


class Mail_settings(models.Model):
    id = models.AutoField(primary_key=True)
    protocol = models.CharField(max_length=90, blank=True, null=True)
    host = models.CharField(max_length=90, blank=True, null=True)
    port = models.CharField(max_length=90, blank=True, null=True)
    user = models.CharField(max_length=90, blank=True, null=True)
    passw = models.CharField(max_length=90, blank=True, null=True)
    from_data = models.CharField(max_length=90, blank=True, null=True)
    reply_to = models.CharField(max_length=90, blank=True, null=True)
    name = models.CharField(max_length=90, blank=True, null=True)
    priority = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return self.from_data

class Inspect_docs(models.Model):
    doc_id = models.AutoField(primary_key=True)
    doc_name = models.CharField(max_length=225, blank=True, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE, blank=True, null=True)
    
    def __str__(self):
        return self.doc_name

class Inspect_media(models.Model):
    media_id = models.AutoField(primary_key=True)
    media_name = models.CharField(max_length=225, blank=True, null=True)
    doc_id = models.ForeignKey(Inspect_docs, on_delete=models.CASCADE, blank=True, null=True)
    user_id = models.ForeignKey(Users, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateField()
    caption = models.CharField(max_length=225, blank=True, null=True)
    name = models.CharField(max_length=100, blank=True, null=True)
    added_date = models.DateField(auto_now_add=True)
    timestamp=models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.media_name