from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

urlpatterns = [
    path('widgets/', views.WidgetList.as_view()),
    path('widgets/<int:pk>/', views.WidgetDetail.as_view()),
]

urlpatterns = format_suffix_patterns(urlpatterns)
