from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('opulens/', views.opulens, name='opulens'),
    path('reportsinsights/', views.reportsinsights, name='reportsinsights'),
    path('signin/', views.signin, name='signin'),
    path('userinput/', views.userinput, name='userinput'),
    path('userprofile/', views.userprofile, name='userprofile'),
    path('usersettings/', views.usersettings, name='usersettings'),
    path('logout/', views.logout, name='logout'),
    path('datavisualization/', views.datavisualization, name='datavisualization'),
    path('budgetracking/', views.budgetracking, name='budgetracking'),
]