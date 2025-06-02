from django.contrib import admin
from .models import MealBooking, GeneralRequirement, Child, Sponsorship

admin.site.register(MealBooking)
admin.site.register(GeneralRequirement)
admin.site.register(Child)
admin.site.register(Sponsorship)