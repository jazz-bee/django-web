from django.shortcuts import render

from projects.models import Project

def project_index(request):
    projects = Project.objects.all() # a Django ORM query to retrieve all projects
    # context:a dictionary used to send information to our template
    context = {                    
        'projects': projects
    }
    return render(request, 'project_index.html', context)

def project_detail(request, pk):
    # retrieves the project with primary key 'pk', equal to the one in the function argument
    project = Project.objects.get(pk=pk)
    context = {
        'project': project
    }
    return render(request, 'project_detail.html', context)