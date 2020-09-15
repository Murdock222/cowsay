from django.shortcuts import render
from homepage.models import MooText
from homepage.forms import MooForm
import subprocess

def index_view(request):
    form = MooForm
    if request.method == "POST":
        form = MooForm(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            cows_data = data.get('MooText')
            sub_process = subprocess.run(['cowsay', cows_data],capture_output=True, text=True)
            print(sub_process.stdout)
            MooText.objects.create(MooText= data.get('MooText'))
            context= {'form':form, 'sub_process_data':sub_process.stdout}

    context = {'form': form}
    return render(request, 'index.html', context)


def history_view(request):
    all_moos = MooText.objects.all().order_by('-id')[:10]
    context = {'all_moos':all_moos}
    return render(request, 'history.html', context)
