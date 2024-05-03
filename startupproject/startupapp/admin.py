from django.contrib import admin
from startupapp.models import Courses,Trainer,Register,Payments,Attendace
# Register your models here.
admin.site.register(Courses)
admin.site.register(Trainer)
admin.site.register(Register)
admin.site.register(Payments)
admin.site.register(Attendace)


# Freelancing__________

from .models import Freelancer, ClientOpportunity

admin.site.register(Freelancer)
admin.site.register(ClientOpportunity)
