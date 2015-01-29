from django.contrib import admin

from test_project.models import Province, Municipality, Zone

# Register your models here.

admin.site.register(Province)
admin.site.register(Municipality)
admin.site.register(Zone)