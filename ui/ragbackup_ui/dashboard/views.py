from django.shortcuts import render
from django.http import HttpResponse, JsonResponse, HttpResponseBadRequest
import os
import subprocess
import shlex
import json

# Create your views here.

def index(request):
    certCommand = "restic stats latest"
    command = shlex.split(certCommand)
    process = subprocess.Popen(command, stdout = subprocess.PIPE)
    print("run ok")
    output, err = process.communicate()
    return render(request, 'main.html', { 'resticstats': output.decode('ascii')})

def resticsnap(request):
    certCommand = "restic snapshots --json"
    command = shlex.split(certCommand)
    process = subprocess.Popen(command, stdout = subprocess.PIPE)
    print("run ok")
    output, err = process.communicate()
    #output = output.replace("b'[", "[").replace("\n'", "")
    job = json.loads(output.decode("ascii").replace("\r\n", "</ br>"))
    return JsonResponse(job,safe=False)

def resticsnapfile(request):
    with open("./dashboard/data/sample.json") as dataj:
        data = json.load(dataj)
    return JsonResponse(data,safe=False)

def resticstats(request):

    #output = output.replace("b'[", "[").replace("\n'", "")
    
    render(request, 'main.html', { 'resticstats': 'hello'})
      


def resticrestore(request):
    if request.GET['sid'] and request.GET['rpath']:
        return render(request, 'restore.html', { 'restoreresult': 'Restore is completed at ' + request.GET['rpath']})
    else:
        return HttpResponseBadRequest("Parameters not found")

def resticfind(request):
    if request.GET['criteria']:
        return render(request, 'restore.html', { 'restoreresult': 'Restore is completed at ' + request.GET['rpath']})
    else:
        return HttpResponseBadRequest("Parameters not found")
