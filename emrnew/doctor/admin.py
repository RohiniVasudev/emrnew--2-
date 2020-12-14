from django.contrib import admin
#from django.contrib.auth.admin import UserAdmin
from .models import DoctorReg
from .models import ReportPredict
from .models import Heartreport
from .models import diabetesreport
from .models import lungreport
from .models import copd

# Register your models here.

admin.site.register(DoctorReg)
admin.site.register(ReportPredict)
admin.site.register(Heartreport)
admin.site.register(diabetesreport)
admin.site.register(lungreport)
admin.site.register(copd)

