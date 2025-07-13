from django.views import View
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib import messages
from django.contrib.auth.models import User

class SignInView(View):
    def get(self, request):
        return render(request, "sign_in.html")

    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')

        if not email or password:
            messages.error(request, "Email and Password can not be empty.")
            return render(request, "sign_in.html", {"email": email})

        # Check if user with email exists
        try:
            user_obj = User.objects.get(email=email)
        except User.DoesNotExist:
            messages.error(request, "No account found with this email.")
            return render(request, "sign_in.html", {"email": email})

        # Use username to authenticate since Django uses `username` not `email`
        user = authenticate(request, username=user_obj.username, password=password)

        if user is not None:
            login(request, user)
            messages.success(request, f"Welcome back, {user.username}!")
            return redirect("core:index")
        else:
            messages.error(request, "Incorrect password. Please try again.")
            return render(request, "sign_in.html", {"email": email})