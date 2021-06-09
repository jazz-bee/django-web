from django.shortcuts import render

from projects.models import Project

def project_index(request):
    projects = Project.objects.all() #a query to retrieve all projects
    # context :a dictionary used to send information to our template
    context = {                    
        'projects': projects
    }
    return render(request, 'project_index.html', context)
