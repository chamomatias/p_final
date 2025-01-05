from django.urls import path
from app import views
from app.views import portfolio, contacto_view


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
]

form_html = [
    path('contacto/', contacto_view, name='contacto'),
    path('portfolio/', portfolio, name='portfolio'),
]
urlpatterns += form_html
