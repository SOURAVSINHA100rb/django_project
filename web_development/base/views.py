from django.shortcuts import render
from .modules.job_handler import JobsHandler
from django.http import JsonResponse
from django.core.serializers import serialize


def home(request):
    data = JobsHandler().fetch_all_jobs()
    print('data', data)
    data_to_return=[]
    for record in data:
        data_to_return.append({
            'id': record.id,
            'title': record.title,
            'location': record.location

        })
    print('data_to_return', data_to_return)
    # jobs = serialize("json", data)
    # print('jobs', jobs)
    return render(request, 'home.html', context={'context':data_to_return})
