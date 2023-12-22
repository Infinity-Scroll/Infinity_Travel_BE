from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("accounts.urls")),
    path('companion/', include('companion.urls')),
    path("chat/", include("chat.urls")),
]
