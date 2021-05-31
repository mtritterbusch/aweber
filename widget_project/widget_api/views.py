from .models import Widget
from .serializers import WidgetSerializer
from rest_framework import generics


class WidgetList(generics.ListCreateAPIView):
    queryset = Widget.objects.all().order_by('-created_date')
    serializer_class = WidgetSerializer


class WidgetDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Widget.objects.all().order_by('-created_date')
    serializer_class = WidgetSerializer
