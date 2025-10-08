from django.shortcuts import render

# Create your views here.
# dashboard/views.py

from django.shortcuts import render
from .models import Project
from django.db.models import Count
import json

def dashboard_view(request):
    projects = Project.objects.all()
    
    # Data for the bar chart (progress)
    names = [p.name for p in projects]
    progress = [p.progress for p in projects]

    # Data for the optional pie chart (status distribution)
    status_counts = Project.objects.values('status').annotate(count=Count('status'))
    labels_pie = [item['status'] for item in status_counts]
    data_pie = [item['count'] for item in status_counts]
    
    return render(request, 'dashboard.html', {
        'projects': projects,
        'names_json': json.dumps(names),
        'progress_json': json.dumps(progress),
        'labels_pie_json': json.dumps(labels_pie),
        'data_pie_json': json.dumps(data_pie),
    })


from django.shortcuts import render
from .models import Project
from django.db.models import Count
from django.contrib.auth.decorators import login_required
import json

@login_required
def dashboard_view(request):
    projects = Project.objects.all()
    
    # Data for the bar chart (progress)
    names = [p.name for p in projects]
    progress = [p.progress for p in projects]

    # Data for the optional pie chart (status distribution)
    status_counts = Project.objects.values('status').annotate(count=Count('status'))
    labels_pie = [item['status'] for item in status_counts]
    data_pie = [item['count'] for item in status_counts]
    
    return render(request, 'dashboard.html', {
        'projects': projects,
        'names_json': json.dumps(names),
        'progress_json': json.dumps(progress),
        'labels_pie_json': json.dumps(labels_pie),
        'data_pie_json': json.dumps(data_pie),
    })