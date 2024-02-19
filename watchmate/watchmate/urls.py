from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path("watch/", include("watchlist_app.Api.urls")),
    path("account/", include("user_app.Api.urls")),
    # path("api-auth/", include("rest_framework.urls")),
]
