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
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),
]


urlpatterns += form_html
