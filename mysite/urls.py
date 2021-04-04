from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static

from mysite.core import views


urlpatterns = [
    path('', views.Home.as_view(), name='home'),
    path('upload/', views.upload, name='upload'),
    path('reports/', views.report_list, name='report_list'),
    path('reports/upload/', views.upload_report, name='upload_report'),
    path('reports/<int:pk>/', views.delete_report, name='delete_report'),

    path('class/reports/search/', views.SearchResultsView.as_view(), name='search_results'),
    path('class/reports/', views.ReportListView.as_view(), name='class_report_list'),
    path('class/reports/upload/', views.UploadReportView.as_view(), name='class_upload_report'),

    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
