from django.urls import path
from django.views.generic import TemplateView
from .views import home, login_view, logout_view, update_cookie_status, signup_view

urlpatterns = [
    path('', home, name='home'),
    # path('connections/', TemplateView.as_view(template_name='login.html')),
    path('signup/', signup_view, name='signup'),

    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('update_cookie_status/', update_cookie_status,
         name='update_cookie_status')
]
