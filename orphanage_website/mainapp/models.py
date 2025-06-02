from django.db import models

class MealBooking(models.Model):
    SLOT_CHOICES = [
        ('breakfast', 'Breakfast'),
        ('lunch', 'Lunch'),
        ('dinner', 'Dinner'),
    ]
    name = models.CharField(max_length=100)
    phone = models.CharField(max_length=15)
    date = models.DateField()
    slot = models.CharField(max_length=20, choices=SLOT_CHOICES)

    def _str_(self):
        return f"{self.name} - {self.date} - {self.slot}"

class GeneralRequirement(models.Model):
    item = models.CharField(max_length=200)
    quantity = models.CharField(max_length=100)
    note = models.TextField(blank=True)

    def _str_(self):
        return self.item

class Child(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    education = models.CharField(max_length=200)
    has_sponsor = models.BooleanField(default=False)

    def _str_(self):
        return self.name

class Sponsorship(models.Model):
    child = models.ForeignKey(Child, on_delete=models.CASCADE)
    sponsor_name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)

    def _str_(self):
        return f"Sponsor: {self.sponsor_name} for {self.child.name}"