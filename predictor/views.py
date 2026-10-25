import json

from django.shortcuts import render, redirect
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.views import LoginView
from .forms import CAR_OPTIONS, RegisterForm, CarPredictionForm


def register_view(request):
    if request.user.is_authenticated:
        return redirect('predictor:dashboard')

    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
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


@login_required
def dashboard_view(request):
    form = CarPredictionForm(request.POST or None)

    return render(
        request,
        "predictor/dashboard.html",
        {
            "form": form,
            "models_by_brand_json": json.dumps(
                CAR_OPTIONS["models_by_brand"]
            ),
        },
    )