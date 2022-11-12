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
    path('calendario/', pviews.kalendar, name = 'calendario'),
    path('update_task/<str:pk>/', pviews.actualizar_calendario, name="update_task"),
    path('borrar_fecha/<str:pk>/', pviews.borrarfecha, name="borrar_fecha"),
]
