from django.shortcuts import render
from .models import Activity, Partner
from django.shortcuts import render, get_object_or_404

def index(request):
    activities = Activity.objects.all()
    return render(request, 'index.html', {'activities': activities})
    
def activity_list(request):
    activities = Activity.objects.all()
    return render(request, 'activity_list.html', {'activities': activities})

def partner_list(request):
    partners = Partner.objects.all()
    return render(request, 'partner_list.html', {'partners': partners})

def activity_detail(request, pk):
    activity = get_object_or_404(Activity, pk=pk)
    return render(request, 'activity_detail.html', {'activity': activity})

def contact_view(request):
    return render(request, 'contact.html')