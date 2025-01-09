from django.urls import path
from app import views
from app.views import portfolio, contacto_view

# URL patterns principales
urlpatterns = [
    path('', views.inicio, name='inicio'),  # Ruta para la página de inicio
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),  # Ruta para la página "Sobre mí"
    path('sobre_nosotros/', views.sobre_nosotros, name='sobre_nosotros'),  # Ruta para la página "Sobre mí"
]

# URL patterns adicionales relacionados con formularios
form_html = [
    path('contacto/', contacto_view, name='contacto'),  # Ruta para la vista de contacto
    path('portfolio/', portfolio, name='portfolio'),  # Ruta para la vista de portafolios
    path('buscar-form-con-api/', views.buscar_form_con_api, name="Buscar_Form_Con_Api"),  # Ruta para buscar formularios usando una API
]

# Agregar las rutas de form_html a las rutas principales
urlpatterns += form_html
