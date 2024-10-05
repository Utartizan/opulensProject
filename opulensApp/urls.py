from django.urls import path # type: ignore
from . import views
from django.contrib.auth import views as auth_views # type: ignore

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login, name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='login'), name='Logout'),
    path('opulens/', views.opulens, name='opulens'),
    path('', views.opulens, name='opulens'),
    path('reportsinsights/', views.reportsinsights, name='reportsinsights'),
    path('signin/', views.signin, name='signin'),
    path('userinput/', views.userinput, name='userinput'),
    path('datavisualisation/', views.datavisualisation, name='datavisualisation'),
    path('budgetracking/', views.budgetracking, name='budgetracking'),
    path('budgetTracking/', views.budgetTracking, name='budgetTracking'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('privacy/', views.privacy, name='privacy'),
    path('terms/', views.terms, name='terms'),
    path('contact/', views.contact, name='contact'),
]