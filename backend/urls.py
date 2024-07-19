from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

from rest_framework import permissions


schema_view = get_schema_view(
   openapi.Info(
      title="ACB API",
      default_version='v1',
      description="API documentations",
      terms_of_service="",
      contact=openapi.Contact(email="contact@snippets.local"),
      license=openapi.License(name="No License"),
   ),
   public=True,
   permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", 
         include(
            [
               path('v1/', include("rest_api_v1.urls"))
            ]
         )
      ),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
