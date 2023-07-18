from django.contrib import admin
from .models import Activity, Partner

class ActivityAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'display_image']

    def display_image(self, obj):
        if obj.picture:
            return f'<img src="{obj.picture.url}" width="200"/>'
        else:
            return 'No image'

    display_image.allow_tags = True

class PartnerAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'display_image']

    def display_image(self, obj):
        if obj.picture:
            return f'<img src="{obj.picture.url}" width="200"/>'
        else:
            return 'No image'

    display_image.allow_tags = True

admin.site.register(Activity, ActivityAdmin)
admin.site.register(Partner, PartnerAdmin)
