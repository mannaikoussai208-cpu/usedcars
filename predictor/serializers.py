
from rest_framework import serializers
from .models import Prediction


class PredictionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Prediction

        fields = [
            'id',
            'brand',
            'car_model',
            'model_year',
            'mileage',
            'fuel_type',
            'horsepower',
            'engine_size',
            'cylinders',
            'transmission_type',
            'ext_col',
            'int_col',
            'accident',
            'clean_title',
            'predicted_price',
            'created_at',
        ]

        read_only_fields = ['id', 'created_at']
