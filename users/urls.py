from django.urls import path
from users import views
from django.contrib.auth.views import LogoutView

# Definición de rutas para la aplicación "users"
urlpatterns = [
    path('login/', views.login_request, name="Login"),  # Ruta para la vista de inicio de sesión
    path('register/', views.register, name="Register"),  # Ruta para la vista de registro de usuarios
    path('logout/', LogoutView.as_view(template_name="users/logout.html"), name="Logout"),  # Ruta para la vista de cierre de sesión
]
