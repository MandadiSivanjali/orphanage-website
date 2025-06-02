from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MealBooking, GeneralRequirement, Child, Sponsorship
from .forms import GeneralRequirementForm
import json

# Static Pages
def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def donation(request):
    return render(request, 'donation.html')

# General Requirements Page
def requirements(request):
    requirements = GeneralRequirement.objects.all()
    return render(request, 'requirements.html', {'requirements': requirements})

def add_general_requirement(request):
    if request.method == 'POST':
        form = GeneralRequirementForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('requirements')
    else:
        form = GeneralRequirementForm()
    return render(request, 'add_general_requirement.html', {'form': form})

# Meal Booking APIs
@csrf_exempt
def check_and_save_booking(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        date = request.POST.get('date')
        slot = request.POST.get('slot')

        if MealBooking.objects.filter(date=date, slot=slot).exists():
            return JsonResponse({'available': False, 'message': 'Slot already booked'})

        MealBooking.objects.create(name=name, date=date, slot=slot)
        return JsonResponse({'available': True, 'message': 'Booking confirmed'})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def check_slot(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        date = data.get('date')
        meal_type = data.get('mealType')

        exists = MealBooking.objects.filter(date=date, slot=meal_type).exists()
        return JsonResponse({'available': not exists})
    return JsonResponse({'error': 'Invalid request method'}, status=400)

@csrf_exempt
def confirm_booking(request):
    if request.method == "POST":
        try:
            data = json.loads(request.body)
            date = data.get("date")
            slot = data.get("slot")
            MealBooking.objects.create(date=date, slot=slot)
            return JsonResponse({"message": "Booking confirmed and saved!"})
        except Exception as e:
            print("Error saving booking:", e)
            return JsonResponse({"message": "Failed to save booking."}, status=500)
    return JsonResponse({'error': 'Invalid request method'}, status=400)

# Sponsorship Views
def sponsorship(request):
    children = Child.objects.all()
    return render(request, 'sponsorship.html', {'children': children})

@csrf_exempt
def sponsor_child(request, child_id):
    if request.method == 'POST':
        child = get_object_or_404(Child, id=child_id)
        sponsor_name = request.POST.get('sponsor_name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')

        Sponsorship.objects.create(
            child=child,
            sponsor_name=sponsor_name,
            email=email,
            phone=phone
        )

        child.has_sponsor = True
        child.save()

        return redirect('sponsorship')

    return redirect('sponsorship')