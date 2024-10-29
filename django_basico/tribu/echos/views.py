from django.shortcuts import redirect, render

from .forms import AddEchoForm

# Create your views here.
from .models import Echo


def echosList(request):
    echos = Echo.objects.all()
    return render(request, 'EchosList.html', {'echos': echos})


def addEcho(request):
    if request.method == 'POST':
        addEchoForm = AddEchoForm(request.POST)
        if addEchoForm.is_valid():
            content = addEchoForm.cleaned_data['content']

            echo = Echo(
                content=content,
                user=request.user,
            )

            echo.save()
            return redirect('echos:echos-list')
    else:
        addEchoForm = AddEchoForm()
        return render(request, 'Forms.html', {'form': addEchoForm, 'object_name': 'Echo'})


def echoDetail(request, echoId):
    echo = Echo.objects.get(id=echoId)
    return render(request, 'EchoDetail.html', {'echo': echo})


def editEcho(request, echoId):
    echo = Echo.objects.get(id=echoId)
    if request.method == 'POST':
        editEchoForm = AddEchoForm(request.POST, instance=echo)
        if editEchoForm.is_valid():
            content = editEchoForm.cleaned_data['content']

            echo.content = content
            echo.save()
            return redirect('echos:echos-list')
    else:
        editEchoForm = AddEchoForm(instance=echo)
        return render(request, 'Forms.html', {'form': editEchoForm, 'object_name': 'Echo'})


def deleteEcho(request, echoId):
    echo = Echo.objects.get(id=echoId)
    echo.delete()
    return redirect('echos:echos-list')
