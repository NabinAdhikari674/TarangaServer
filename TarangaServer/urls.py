from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('stockInfo/', views.stockInfo, name = "stockInfo"),
    path('marketStatus/', views.marketStatus, name = "marketStatus"),
    path('notice/',views.notice, name = "notice"),
    path('disclosure/',views.disclosure, name = "disclosure"),
    path('nepseIndex/',views.nepseIndex, name = "nepseIndex"),
    path('marketSummary/',views.marketSummary, name = "marketSummary"),
    path('topGainers/',views.topGainers, name = "topGainers"),
    path('topTurnovers/',views.topTurnovers, name = "topTurnovers"),
    path('supplyDemand/',views.supplyDemand, name = "supplyDemand")
]
