from land import models
from django.db.models import Count
from django.db.models.functions import TruncDate
import requests
from datetime import datetime

# ==========================================================================================================================
# Métodos Helpers API Question
# ==========================================================================================================================


def obtener_respuestas_contestadas_no_contestadas(url):
    response = requests.get(url)
    data = response.json()

    # Obtener el número de respuestas contestadas y no contestadas
    contestadas = sum(item["is_answered"] for item in data["items"])
    no_contestadas = len(data["items"]) - contestadas

    return {
        "respuestas_contestadas": contestadas,
        "respuestas_no_contestadas": no_contestadas,
    }


def obtener_respuesta_mayor_reputacion(url):
    response = requests.get(url)
    data = response.json()

    # Encontrar la respuesta con mayor reputación
    max_reputacion = max(data["items"], key=lambda item: item["score"])

    return max_reputacion


def obtener_respuesta_menor_vistas(url):
    response = requests.get(url)
    data = response.json()

    # Encontrar la respuesta con menor número de vistas
    min_vistas = min(data["items"], key=lambda item: item["view_count"])

    return min_vistas


def obtener_respuestas_mas_vieja_mas_actual(url):
    response = requests.get(url)
    data = response.json()

    # Encontrar la respuesta más vieja y más actual
    mas_vieja = min(data["items"], key=lambda item: item["creation_date"])
    mas_actual = max(data["items"], key=lambda item: item["creation_date"])

    # Convertimos a fechas legibles
    mas_vieja["creation_date"] = datetime.utcfromtimestamp(
        mas_vieja["creation_date"]
    ).strftime("%Y-%m-%d %H:%M:%S")
    mas_actual["creation_date"] = datetime.utcfromtimestamp(
        mas_actual["creation_date"]
    ).strftime("%Y-%m-%d %H:%M:%S")

    return {"respuesta_mas_vieja": mas_vieja, "respuesta_mas_actual": mas_actual}


# ==========================================================================================================================
# Métodos Helpers Vuelos
# ==========================================================================================================================


def aeropuertos_mas_movimientos():
    aeropuertos_mas_movimiento = (
        models.Vuelo.objects.values("aeropuerto__nombre_aeropuerto")
        .annotate(total_movimientos=Count("movimiento"))
        .filter(total_movimientos=models.Vuelo.objects.values("aeropuerto__nombre_aeropuerto")
                .annotate(total_movimientos=Count("movimiento"))
                .order_by("-total_movimientos")
                .values("total_movimientos")[:1]
        )
        .order_by("aeropuerto__nombre_aeropuerto")
    )

    nombres_aeropuertos_mas_movimiento = [a["aeropuerto__nombre_aeropuerto"] for a in aeropuertos_mas_movimiento]

    return nombres_aeropuertos_mas_movimiento


def aerolinea_mayor_movimiento_anio():
    aerolineas_mayor_movimiento_anio = (
        models.Vuelo.objects.values("aerolinea__nombre_aerolinea")
        .annotate(total_vuelos=Count("id"))
        .filter(total_vuelos=models.Vuelo.objects.values("aerolinea__nombre_aerolinea")
                .annotate(total_vuelos=Count("id"))
                .order_by("-total_vuelos")
                .values("total_vuelos")[:1]
        )
        .order_by("aerolinea__nombre_aerolinea")
    )

    nombres_aerolineas_mayor_movimiento_anio = [a["aerolinea__nombre_aerolinea"] for a in aerolineas_mayor_movimiento_anio]

    return nombres_aerolineas_mayor_movimiento_anio


def dia_mayor_numero_vuelos():
    dia_mayor_numero_vuelos = (
        models.Vuelo.objects.values("dia")
        .annotate(total_vuelos=Count("id"))
        .order_by("-total_vuelos")
        .first()
    )
    if dia_mayor_numero_vuelos:
        dia = dia_mayor_numero_vuelos["dia"]
        total_vuelos = dia_mayor_numero_vuelos["total_vuelos"]
        return f"El día {dia} se han tenido el mayor número de vuelos: {total_vuelos}"
    else:
        return "No hay datos disponibles"


def aerolineas_mas_dos_vuelos_por_dia():
    aerolineas_mas_dos_vuelos_por_dia = (
        models.Vuelo.objects.annotate(dia_trunc=TruncDate("dia"))
        .values("aerolinea__nombre_aerolinea")
        .annotate(total_vuelos=Count("id", distinct=True))
        .filter(total_vuelos__gt=2)
        .order_by("-total_vuelos")
    )
    if aerolineas_mas_dos_vuelos_por_dia:
        aerolineas = [
            aero["aerolinea__nombre_aerolinea"]
            for aero in aerolineas_mas_dos_vuelos_por_dia
        ]
        return aerolineas
    else:
        return "No hay aerolíneas con más de 2 vuelos por día"
