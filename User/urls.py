from django.urls import path
from django.views.generic import TemplateView
from rest_framework.schemas import get_schema_view

from .views import UserAPIView, SingleUserAPIView, MultipleUserAPIView

urlpatterns = [
    path('', TemplateView.as_view(
        template_name='doc.html',
        extra_context={'schema_url':'openapi-schema'}
    ), name='swagger-ui'),
    path('openapi', get_schema_view(
        title="Your Project",
        description="API for all things …",
        version="1.0.0"
    ), name='openapi-schema'),
    path('api/users/', UserAPIView.as_view(), name="user_api_view"),
    path('api/users/<int:pk>', SingleUserAPIView.as_view(), name="single_user_api_view"),
    path('api/users/multiple/', MultipleUserAPIView.as_view(), name="multiple_user_api_view"),
]