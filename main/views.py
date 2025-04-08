from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseForbidden, HttpResponseRedirect
from .models import Message, User
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from . forms import RegisterForm
from django.contrib import messages


def signup(request):
	if request.method == 'POST':
		form = RegisterForm(request.POST)
		if form.is_valid():
			form.save()
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password1')
			user = authenticate(username=username, password=password)
			login(request, user)
			return redirect('home')
	else:
		form = RegisterForm()

	# user = authenticate(username=username, password=password1)
	# login(request, user)
	return render(request, 'main/register.html', {'form': form})

def send_message(request, username):
    user = get_object_or_404(User, username=username)
    
    if request.method == "POST":
        content = request.POST.get('content')
        if content:
            Message.objects.create(recipient=user, content=content)
            messages.success(request, f'Message sent!')
            # return HttpResponseRedirect('/message/sent/')  # Redirect after submission

    return render(request, 'main/send_message.html', {'recipient': user})


def auth(request):
    if request.user.is_authenticated:
        return redirect('home')
    return render(request, 'main/auth.html')


def user_home(request):
    if not request.user.is_authenticated:
        return redirect('auth')
    messages = request.user.messages.all()  
    return render(request, 'main/home.html', {'messages': messages})

@login_required
def message_detail(request, message_id):
    message = get_object_or_404(Message, id=message_id)

    # Only allow the owner to view the message
    if message.recipient != request.user:
        return HttpResponseForbidden("You are not allowed to view this message as it was not sent to you.")

    # Mark as read and render
    message.is_read = True
    return render(request, 'main/message_detail.html', {'message': message})