#from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import UserUpdateForm

@login_required
def profile(request):
    if request.method == 'POST':
        u_form = UserUpdateForm(request.POST, request.FILES, instance=request.user.profile)
        if u_form.is_valid():
            u_form.save()
            return redirect('profile')
    else:
        u_form = UserUpdateForm(instance=request.user.profile)

    context = {
        'u_form': u_form
    }

    return render(request, 'accounts/profile.html', context)
