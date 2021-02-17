from django.contrib import admin

from rango.models import entry,UserProfile

class EntryAdmin(admin.ModelAdmin):
    list_display = ('frd_name', 'DOB','frd_email',)

admin.site.register(entry)
admin.site.register(UserProfile)
# Register your models here.

# jr6781 zxcv
