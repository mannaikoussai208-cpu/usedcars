
from django.db import models
from django.contrib.auth.models import User


class Prediction(models.Model):


    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="predictions"
    )

    brand = models.CharField(max_length=100)
    car_model = models.CharField(max_length=100)
    model_year = models.PositiveSmallIntegerField()
    mileage = models.PositiveIntegerField()

    fuel_type = models.CharField(max_length=100)
    horsepower = models.FloatField(null=True, blank=True)
    engine_size = models.FloatField(null=True, blank=True)
    cylinders = models.PositiveSmallIntegerField(null=True, blank=True)

    transmission_type = models.CharField(max_length=100)
    ext_col = models.CharField(max_length=100)
    int_col = models.CharField(max_length=100)

    accident = models.BooleanField(default=False)
    clean_title = models.CharField(max_length=100)

   
    predicted_price = models.DecimalField(
        max_digits=12,
        decimal_places=2,
        null=True,
        blank=True
    )

    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.brand} {self.car_model} - {self.user.username}"

    class Meta:
        ordering = ['-created_at']
