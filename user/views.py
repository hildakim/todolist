from django.shortcuts import render
from django.contrib import messages
from .forms import CustomUserChangeForm
# Create your views here.

def user_profile(request):
    if request.method == 'GET':
        return render(request, 'u_profile.html')

def user_profile_update(request):
    if request.method == 'POST':
        user_change_form = CustomCsUserChangeForm(request.POST, instance = request.user)

        if user_change_form.is_valid():
            user_change_form.save()
            messages.success(request, '회원정보가 수정되었습니다.')
            return render(request, 'u_profile.html')
    else:
        user_change_form = CustomCsUserChangeForm(instance = request.user)
        return render(request, 'u_update.html', {'user_change_form':user_change_form})

def user_profile_delete(request):
    if request.method == 'POST':
        request.user.delete()
        return redirect('/user/profile')
    return render(request, 'u_delete.html')
