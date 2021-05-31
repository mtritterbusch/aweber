from .models import Widget
from rest_framework import serializers


class WidgetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Widget
        fields = [
            'id',
            'name',
            'number_of_parts',
            'created_date',
            'updated_date',
        ]
