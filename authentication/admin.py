from django.contrib import admin
from .models import Job_title, Country, City_zip_state, Roles, Users, Personal_info, User_log, User_mg, Mail_settings, Inspect_docs, Inspect_media

# Register your models here.
admin.site.register(Job_title)
admin.site.register(Country)
admin.site.register(City_zip_state)
admin.site.register(Roles)
admin.site.register(Users)
admin.site.register(Personal_info)
admin.site.register(User_log)
admin.site.register(User_mg)
admin.site.register(Mail_settings)
admin.site.register(Inspect_docs)
admin.site.register(Inspect_media)