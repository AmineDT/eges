from django.shortcuts import render
from .models import Activity, Partner

def index(request):
    activities = Activity.objects.all()
    return render(request, 'index.html', {'activities': activities})
    
def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'activity_list.html', {'activities': activities})

def partner_list(request):
    partners = Partner.objects.all()
    return render(request, 'partner_list.html', {'partners': partners})
