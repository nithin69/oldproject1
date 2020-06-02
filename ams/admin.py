from django.contrib import admin
from .models import *

class MembersAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'designation',
        'membership',
        'description',
        'phone',
        'image',
        'application',
        'sms',
    )


admin.site.register(Events)
admin.site.register(News)
admin.site.register(Members, MembersAdmin)
admin.site.register(Carosuel)
admin.site.register(Youtube)
admin.site.register(Activites)
admin.site.register(library)
admin.site.register(Image)
admin.site.register(Video)
admin.site.register(Audio)
admin.site.register(Scolarship)
admin.site.register(Jobs)
admin.site.register(Contact)
admin.site.register(Secretery)
admin.site.register(Marquee)



# Register your models here.
