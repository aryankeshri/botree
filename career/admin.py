from django.contrib import admin

# Register your models here.
from .models import Profile

class ProfileModelAdmin(admin.ModelAdmin):
    list_display = ['doc_name', 'name', 'mobile', 'email', 'skills', 'ctc', ]
    list_filter = ['skills', 'current_location', 'work_exp']
    search_fields = ['skills', 'current_location', 'work_exp']

    class Meta:
        model = Profile


admin.site.register(Profile, ProfileModelAdmin)
