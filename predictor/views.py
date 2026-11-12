
import json

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.views import LoginView
from django.views import View

from .forms import CAR_OPTIONS, RegisterForm, CarPredictionForm


class RegisterView(View):

    def get(self, request):
        if request.user.is_authenticated:
            return redirect('predictor:dashboard')

        form = RegisterForm()

        return render(
            request,
            'predictor/register.html',
            {'form': form}
        )

    def post(self, request):
        if request.user.is_authenticated:
            return redirect('predictor:dashboard')

        form = RegisterForm(request.POST)

        if form.is_valid():
            user = form.save()
            login(request, user)

            return redirect('predictor:dashboard')

        return render(
            request,
            'predictor/register.html',
            {'form': form}
        )


class CustomLoginView(LoginView):
    template_name = 'predictor/login.html'
    redirect_authenticated_user = True


class DashboardView(LoginRequiredMixin, View):

    def get(self, request):
        form = CarPredictionForm()

        return render(
            request,
            'predictor/dashboard.html',
            {
                'form': form,
                'models_by_brand_json': json.dumps(
                    CAR_OPTIONS["models_by_brand"]
                ),
            },
        )

    def post(self, request):
        form = CarPredictionForm(request.POST)

        return render(
            request,
            'predictor/dashboard.html',
            {
                'form': form,
                'models_by_brand_json': json.dumps(
                    CAR_OPTIONS["models_by_brand"]
                ),
            },
        )
