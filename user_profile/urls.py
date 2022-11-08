from django.urls import path
from register import views
from . import views as pviews



urlpatterns = [
    path("", views.mainpage_request, name="homepage"),
    path("registero/", views.register_request, name="register"),
    path('nuevogasto/', pviews.NuevoGastoView, name="nuevogasto"),
    path('vergastos/', pviews.vergasto, name="vergastos"),
    path('subirgasto/', pviews.subirgasto, name="subirgasto"),
    path('vergastos/<int:pk>/',pviews.borrarlink, name="borrarlink"),
    path('<int:año>/<str:mes>', views.mainpage_request, name='homepage')
]
