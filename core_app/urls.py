
from django.urls import path
from .views import sipcalculator , MilealgeCalculator, Dashboard, PositionSizeCalculator, CurrencyConverter
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('', Dashboard.as_view(), name='home'),
    path('sip/', sipcalculator.as_view(), name='sip'),
    path('mileage/', MilealgeCalculator.as_view(), name='mileage'),
    path('position/', PositionSizeCalculator.as_view(), name='position'),
    path('converter/', CurrencyConverter.as_view(), name='converter'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
