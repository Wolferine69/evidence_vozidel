from django.urls import path
from .views import VozidlaListView, VozidloDetailView, AddUkon, EditVozidlo

urlpatterns = [
    path('', VozidlaListView.as_view(), name='seznam_vozidel'),
    path('vozidlo/<int:pk>/', VozidloDetailView.as_view(), name='detail_vozidla'),
    path('vozidlo/<int:pk>/pridat-servisni-ukon/', AddUkon.as_view(), name='pridat_servisni_ukon'),
    path('vozidlo/<int:pk>/edit/', EditVozidlo.as_view(), name='edit_vozidlo'),
]