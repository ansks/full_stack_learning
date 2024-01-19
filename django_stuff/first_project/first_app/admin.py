from django.contrib import admin
from first_app.models import Topic, Webpage, AccessRecord

# Register your models here.

admin.site.register(Topic)  # Topic Table
admin.site.register(Webpage) # Webpage Table 
admin.site.register(AccessRecord) # AccessReordTable