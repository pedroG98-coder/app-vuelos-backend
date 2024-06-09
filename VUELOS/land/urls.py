from django.urls import path
from land import views

urlpatterns = [
    path('', views.index, name='index'),

    # ========================================================================================================================
    # Rutas URLS Modelos CRUD ((POST-GET-ID-PUT-DELETE-GET-ALL)) App Vuelos
    # ========================================================================================================================


    # Url Modelo Aerolinea Lista App Vuelos
    path(
        "aerolinea",
        views.AerolineaList.as_view(),
        name="aerolinea-list",
    ),
    # Url Modelo Aerolinea Detalle App Vuelos
    path(
        "aerolinea/<int:pk>",
        views.AerolineaDetail.as_view(),
        name="aerolinea-detail",
    ),


    # Url Modelo Aeropuerto Lista App Vuelos
    path(
        "aeropuerto",
        views.AeropuertoList.as_view(),
        name="aeropuerto-list",
    ),
    # Url Modelo Aeropuerto Detalle App Vuelos
    path(
        "aeropuerto/<int:pk>",
        views.AerolineaDetail.as_view(),
        name="aeropuerto-detail",
    ),


    # Url Modelo Movimiento Lista App Vuelos
    path(
        "movimiento",
        views.MovimientoList.as_view(),
        name="movimiento-list",
    ),
    # Url Modelo Movimiento Detalle App Vuelos
    path(
        "movimiento/<int:pk>",
        views.MovimientoDetail.as_view(),
        name="movimiento-detail",
    ),


    # Url Modelo Vuelo Lista App Vuelos
    path(
        "vuelo",
        views.VueloList.as_view(),
        name="aerolinea-list",
    ),
    # Url Modelo Vuelo Detalle App Vuelos
    path(
        "vuelo/<int:pk>",
        views.VueloDetail.as_view(),
        name="vuelo-detail",
    ),


    # ==========================================================================================================================
    # Endpoints Helpers API Question
    # ==========================================================================================================================


    path(
        "helpers/obtener-respuestas-contestadas-no-contestadas",
        views.ObtenerRespuestasContestadasNoContestadas.as_view(),
        name="helpers/obtener-respuestas-contestadas-no-contestadas",
    ),

    path(
        "helpers/obtener-respuesta-mayor-reputacion",
        views.ObtenerRespuestaMayorReputacion.as_view(),
        name="helpers/obtener-respuesta-mayor-reputacion",
    ),


    path(
        "helpers/obtener-respuesta-menor-vista",
        views.ObtenerRespuestaMenorVista.as_view(),
        name="helpers/obtener-respuesta-menor-vista",
    ),


    path(
        "helpers/obtener-respuestas-mas-vieja-mas-actual",
        views.ObtenerRespuestasMasViejaMasActual.as_view(),
        name="helpers/obtener-respuestas-mas-vieja-mas-actual",
    ),


    # ==========================================================================================================================
    # Endpoints Helpers Vuelos
    # ==========================================================================================================================


    path(
        "helpers/aerolinea-mas-vuelos",
        views.AerolineaMasVuelos.as_view(),
        name="helpers/aerolinea-mas-vuelos",
    ),


    path(
        "helpers/aerolinea-mayor-movimiento-anio",
        views.AerolineaMayorMovimientoAnio.as_view(),
        name="helpers/aerolinea-mayor-movimiento-anio",
    ),


    path(
        "helpers/dia-mayor-numero-vuelos",
        views.DiaMayorNumeroVuelos.as_view(),
        name="helpers/dia-mayor-numero-vuelos",
    ),


    path(
        "helpers/aerolineas-mas-dos-vuelos-por-dia",
        views.AerolineasMasDosVuelosPorDia.as_view(),
        name="helpers/aerolineas-mas-dos-vuelos-por-dia",
    ),
]
