from django.urls import path
from app import views
from app.views import portfolio, form_con_api, contacto_view


urlpatterns = [
    path('', views.inicio, name='inicio'),
    path('sobre_mi/', views.sobre_mi, name='sobre_mi'),
    path('contacto/', contacto_view, name='contacto'),
    path('portfolio/', portfolio, name='portfolio'),
]

form_html = [
    path('form_con_api', views.form_con_api, name="form_con_api"),
]
urlpatterns += form_html
