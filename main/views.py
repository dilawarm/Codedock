from django.shortcuts import render
from django.http import HttpResponse
from .forms import CodeForm
import datetime
import os
import docker

def homepage(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["input_code"]
            if not os.path.exists("main/codefiles"):
                os.makedirs("main/codefiles")
            filename = f"code-{datetime.datetime.now()}.py"
            f = open(os.path.join("main/codefiles", filename), "w+")
            f.write(code)
            f.close()
            client = docker.from_env()
            client.containers.run("ubuntu:latest", "echo hello world")

    form = CodeForm()
    return render(request, "homepage.html", {"form": form})