import json
from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from pathlib import Path


class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


OPTIONS_PATH = Path(__file__).parent / "data" / "car_options.json"

with open(OPTIONS_PATH, "r", encoding="utf-8") as file:
    CAR_OPTIONS = json.load(file)


class CarPredictionForm(forms.Form):
    brand = forms.ChoiceField(
        label="Brand",
        choices=[("", "Select a brand")] + [
            (brand, brand) for brand in CAR_OPTIONS["brands"]
        ],
    )

    model = forms.ChoiceField(
        label="Model",
        choices=[("", "Select a brand first")],
    )

    model_year = forms.ChoiceField(
        label="Model year",
        choices=[
            ("", "Select a year")
        ] + [
            (str(year), str(year))
            for year in sorted(CAR_OPTIONS["model_years"], reverse=True)
        ],
    )

    milage = forms.IntegerField(
        label="Mileage (miles)",
        min_value=0,
    )

    fuel_type = forms.ChoiceField(
        label="Fuel type",
        choices=[("", "Select fuel type")] + [
            (fuel, fuel) for fuel in CAR_OPTIONS["fuel_types"]
        ],
    )

    horsepower = forms.FloatField(
        label="Horsepower",
        min_value=0,
        required=False,
    )

    engine_size = forms.FloatField(
        label="Engine size (liters)",
        min_value=0,
        required=False,
    )

    cylinders = forms.IntegerField(
        label="Number of cylinders",
        min_value=0,
        required=False,
    )

    transmission_type = forms.ChoiceField(
        label="Transmission",
        choices=[("", "Select transmission")] + [
            (item, item)
            for item in CAR_OPTIONS["transmission_types"]
        ],
    )

    ext_col = forms.ChoiceField(
        label="Exterior color",
        choices=[("", "Select exterior color")] + [
            (color, color)
            for color in CAR_OPTIONS["exterior_colors"]
        ],
    )

    int_col = forms.ChoiceField(
        label="Interior color",
        choices=[("", "Select interior color")] + [
            (color, color)
            for color in CAR_OPTIONS["interior_colors"]
        ],
    )

    accident = forms.ChoiceField(
        label="Accident history",
        choices=[
            ("", "Select accident history"),
            ("0", "No accident reported"),
            ("1", "Accident reported"),
        ],
    )

    clean_title = forms.ChoiceField(
        label="Clean title",
        choices=[("", "Select title status")] + [
            (title, title) for title in CAR_OPTIONS["clean_titles"]
        ],
    )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        selected_brand = self.data.get("brand", "")
        available_models = CAR_OPTIONS["models_by_brand"].get(
            selected_brand, []
        )

        self.fields["model"].choices = [
            ("", "Select a model")
        ] + [
            (model, model) for model in available_models
        ]
