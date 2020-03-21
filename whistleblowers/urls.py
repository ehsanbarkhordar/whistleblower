"""whistleblowers URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path, re_path
from django.views.static import serve
from rest_framework import routers

from reports import views
from reports.views import home, thanks

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'reports', views.ReportViewSet, "ssss")
# router.register(r'rep', views.SendReport)

urlpatterns = [
    path('api/', include(router.urls)),
    # path('home/', HomeView.as_view()),
    path('', home),
    path('thanks/', thanks),
    # path('list/', ListReportsView.as_view(), name="reports-all"),
    # path('add/', AddReportView.as_view(), name="report-add"),
    # path('rr/', RReportViewSet.as_view({'get': 'list'}), name="report-add"),
    # path('rr/', RReportViewSet.as_view({'post': 'list'}), name="report-add"),

    # re_path('api/(?P<version>(v1|v2))/reports/', include('reports.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),
    re_path(r'^static/(?P<path>.*)$', serve, {
        'document_root': settings.STATIC_ROOT,
    }),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
