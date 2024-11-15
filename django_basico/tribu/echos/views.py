from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.shortcuts import redirect, render

from waves.forms import WaveAddForm
from waves.models import Wave

from .forms import AddEchoForm

# Create your views here.
from .models import Echo


@login_required
def echos_list(request):
    echos = Echo.objects.all()
    return render(request, 'EchosList.html', {'echos': echos})


@login_required
def add_echo(request):
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


@login_required
def echo_detail(request, id):
    echo = Echo.objects.get(id=id)

    return render(
        request,
        'EchoDetail.html',
        {
            'echo': echo,
            'waves': echo.waves.all()[:5],
            'form': WaveAddForm(),
        },
    )


@login_required
def echo_all_waves(request, id):
    echo = Echo.objects.get(id=id)

    return render(
        request,
        'EchoDetail.html',
        {
            'echo': echo,
            'waves': echo.waves.all(),
            'form': WaveAddForm(),
        },
    )


@login_required
def add_wave_to_echo(request, id):
    echo = Echo.objects.get(id=id)

    wave = Wave(
        echo=echo,
        user=request.user,
        content=request.POST.get('content'),
    )
    wave.save()

    return render(request, 'EchoDetail.html', {'echo': echo, 'form': WaveAddForm()})


@login_required
def edit_echo(request, id):
    echo = Echo.objects.get(id=id)
    if request.user != echo.user:
        return HttpResponseForbidden()

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


@login_required
def delete_echo(request, id):
    echo = Echo.objects.get(id=id)
    if request.user != echo.user:
        return HttpResponseForbidden()

    echo.delete()
    return redirect('echos:echos-list')


@login_required
def echoWaves(request, id):
    echo = Echo.objects.get(id=id)
    return render(request, 'EchoDetail.html', {'echo': echo})
