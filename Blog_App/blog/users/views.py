from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
    else:
        form = UserCreationForm()
    return render(request, 'users/register.html', {'form':form})
