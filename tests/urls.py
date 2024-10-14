import os

from django.urls import include, path, re_path
import django.views.static

from django.contrib import admin

admin.autodiscover()

urlpatterns = [
    re_path(r"^admin/", admin.site.urls),
    path("knowledge/", include("knowledge.urls")),
    re_path(
        r"^static/(?P<path>.*)$",
        django.views.static.serve,
        {
            "document_root": os.path.join(
                os.path.dirname(__file__), "../knowledge/static"
            ).replace("\\", "/")
        },
    ),
]
