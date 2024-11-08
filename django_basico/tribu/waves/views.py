from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render

from .forms import WaveForm

# Create your views here.
from .models import Wave


@login_required
def delete_wave(request, id):
    wave = Wave.objects.get(id=id)
    wave.delete()
    return redirect('echos:echo-details', echo_id=wave.echo.id)


@login_required
def edit_wave(request, id):
    wave = Wave.objects.get(id=id)
    if request.POST:
        wave_form = WaveForm(request.POST)
        if wave_form.is_valid():
            wave.content = wave_form.cleaned_data['content']
            wave.save()
            return redirect('echos:echo-details', echo_id=wave.echo.id)
    else:
        wave_form = WaveForm(instance=wave)
        return render(request, 'Forms.html', {'form': wave_form})
