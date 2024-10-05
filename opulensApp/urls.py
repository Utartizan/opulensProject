from django.urls import path # type: ignore
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login', views.login, name='login'),
    path('opulens/', views.opulens, name='opulens'),
    path('reportsinsights/', views.reportsinsights, name='reportsinsights'),
    path('signin/', views.signin, name='signin'),
    path('userinput/', views.userinput, name='userinput'),
    path('datavisualisation/', views.datavisualisation, name='datavisualisation'),
    path('budgetracking/', views.budgetracking, name='budgetracking'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
]