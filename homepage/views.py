from django.shortcuts import render
from homepage.models import MooText
from homepage.forms import MooForm
import subprocess

def index_view(request):
    moo = ""
    if request.method == "POST":
        form = MooForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cows_data = data.get('text')
            MooText.objects.create(text=cows_data)
            moo = subprocess.check_output(["cowsay", cows_data], text=True)


    form = MooForm()
    return render(request, 'index.html', {"form": form, "moo":moo})



def history_view(request):
    all_moos = MooText.objects.all().order_by('-id')[:10]
    context = {'all_moos':all_moos}
    return render(request, 'history.html', context)
