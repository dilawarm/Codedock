from django.shortcuts import render
from django.http import HttpResponse
from .forms import CodeForm
import datetime
import os
import subprocess

def homepage(request):
    if request.method == "POST":
        form = CodeForm(request.POST)
        if form.is_valid():
            code = form.cleaned_data["input_code"]
            lang = form.cleaned_data["language"]
            print(lang)
            if not os.path.exists("main/docker"):
                os.makedirs("main/docker")
                os.makedirs("main/docker/python")
                os.makedirs("main/docker/c++")
                os.makedirs("main/docker/rust")
            extension = ""
            folder = ""
            if lang == "Python 3":
                extension = ".py"
                folder = "python"
            elif lang == "C++":
                extension = ".cpp"
                folder = "c++"
            elif lang == "Rust":
                extension = ".rs"
                folder = "rust"

            filename = "test"+extension
            f = open(os.path.join("main/docker/"+folder, filename), "w+")
            f.write(code)
            f.close()

            process = subprocess.run(f"cd main/docker/{folder} && docker build -t test . && docker run test", shell=True, check=True, stdout=subprocess.PIPE, universal_newlines=True)
            output = process.stdout
            remove = ":latest"
            print(output)
            output = output[output.index(remove) + len(remove):]
            return render(request, "homepage.html", {"form": form, "output": output})

    form = CodeForm()
    return render(request, "homepage.html", {"form": form})
