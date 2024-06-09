from django.shortcuts import render
from land import models, serializers, helpers_vuelos
from rest_framework.generics import get_object_or_404
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.pagination import LimitOffsetPagination
import requests
from django.db.models import Max, Min
from django.utils import timezone
from datetime import datetime
from django.db.models import Count
import json
from django.http import JsonResponse


def index(request):
    return render(request, "land/index.html")


# ==========================================================================================================================
# Vistas CRUD APP-Vuelos
# ==========================================================================================================================


#################### Vista List Para Modelo Aerolinea ###################
class AerolineaList(APIView):
    """
    GET = Returns a List of all objects with estatus_sistema = TRUE
    POST = Creates a new object in DB
    """

    def get(self, request):
        objects = models.Aerolinea.objects.filter(estatus_sistema=True)
        serializer = serializers.GetAerolineaSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SetAerolineaSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################### Vista Detail Para Modelo Aerolinea ##################
class AerolineaDetail(APIView):
    """
    GET = Returns one object selected by the given primary key
    PUT = Updates one object selected by the given primary key
    DELETE = Changes the estatus_sistema attribute to False (item will no longer be listed)
    """

    def get_object(self, pk):
        model_object = get_object_or_404(models.Aerolinea, pk=pk)
        return model_object

    def get(self, request, pk):
        model_object = self.get_object(pk)
        serializer = serializers.GetAerolineaSerializer(model_object)
        return Response(serializer.data)

    def put(self, request, pk):
        model_object = self.get_object(pk)
        serializer = serializers.SetAerolineaSerializer(model_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        model_object = self.get_object(pk)
        model_object.estatus_sistema = False
        model_object.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################### Vista List Para Modelo Aeropuerto ###################
class AeropuertoList(APIView):
    """
    GET = Returns a List of all objects with estatus_sistema = TRUE
    POST = Creates a new object in DB
    """

    def get(self, request):
        objects = models.Aeropuerto.objects.filter(estatus_sistema=True)
        serializer = serializers.GetAeropuertoSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SetAeropuertoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################### Vista Detail Para Modelo Aeropuerto ##################
class AeropuertoDetail(APIView):
    """
    GET = Returns one object selected by the given primary key
    PUT = Updates one object selected by the given primary key
    DELETE = Changes the estatus_sistema attribute to False (item will no longer be listed)
    """

    def get_object(self, pk):
        model_object = get_object_or_404(models.Aeropuerto, pk=pk)
        return model_object

    def get(self, request, pk):
        model_object = self.get_object(pk)
        serializer = serializers.GetAeropuertoSerializer(model_object)
        return Response(serializer.data)

    def put(self, request, pk):
        model_object = self.get_object(pk)
        serializer = serializers.SetAeropuertoSerializer(
            model_object, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        model_object = self.get_object(pk)
        model_object.estatus_sistema = False
        model_object.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################### Vista List Para Modelo Movimiento ###################
class MovimientoList(APIView):
    """
    GET = Returns a List of all objects with estatus_sistema = TRUE
    POST = Creates a new object in DB
    """

    def get(self, request):
        objects = models.Movimiento.objects.filter(estatus_sistema=True)
        serializer = serializers.GetMovimientoSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SetMovimientoSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################### Vista Detail Para Modelo Movimiento ##################
class MovimientoDetail(APIView):
    """
    GET = Returns one object selected by the given primary key
    PUT = Updates one object selected by the given primary key
    DELETE = Changes the estatus_sistema attribute to False (item will no longer be listed)
    """

    def get_object(self, pk):
        model_object = get_object_or_404(models.Movimiento, pk=pk)
        return model_object

    def get(self, request, pk):
        model_object = self.get_object(pk)
        serializer = serializers.GetMovimientoSerializer(model_object)
        return Response(serializer.data)

    def put(self, request, pk):
        model_object = self.get_object(pk)
        serializer = serializers.SetMovimientoSerializer(
            model_object, data=request.data
        )
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        model_object = self.get_object(pk)
        model_object.estatus_sistema = False
        model_object.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


#################### Vista List Para Modelo Vuelo ###################
class VueloList(APIView):
    """
    GET = Returns a List of all objects with estatus_sistema = TRUE
    POST = Creates a new object in DB
    """

    def get(self, request):
        objects = models.Vuelo.objects.filter(estatus_sistema=True)
        serializer = serializers.GetVueloSerializer(objects, many=True)
        return Response(serializer.data)

    def post(self, request):
        serializer = serializers.SetVueloSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


################### Vista Detail Para Modelo Vuelo ##################
class VueloDetail(APIView):
    """
    GET = Returns one object selected by the given primary key
    PUT = Updates one object selected by the given primary key
    DELETE = Changes the estatus_sistema attribute to False (item will no longer be listed)
    """

    def get_object(self, pk):
        model_object = get_object_or_404(models.Vuelo, pk=pk)
        return model_object

    def get(self, request, pk):
        model_object = self.get_object(pk)
        serializer = serializers.GetVueloSerializer(model_object)
        return Response(serializer.data)

    def put(self, request, pk):
        model_object = self.get_object(pk)
        serializer = serializers.SetVueloSerializer(model_object, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        model_object = self.get_object(pk)
        model_object.estatus_sistema = False
        model_object.save()
        return Response(status=status.HTTP_204_NO_CONTENT)


# ==========================================================================================================================
# Vistas Helpers API Question
# ==========================================================================================================================


class ObtenerRespuestasContestadasNoContestadas(APIView):
    def get(self, request):
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
        resultados = helpers_vuelos.obtener_respuestas_contestadas_no_contestadas(url)
        return Response(resultados)


class ObtenerRespuestaMayorReputacion(APIView):
    def get(self, request):
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
        resultados = helpers_vuelos.obtener_respuesta_mayor_reputacion(url)
        return Response(resultados)


class ObtenerRespuestaMenorVista(APIView):
    def get(self, request):
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
        resultados = helpers_vuelos.obtener_respuesta_menor_vistas(url)
        return Response(resultados)


class ObtenerRespuestasMasViejaMasActual(APIView):
    def get(self, request):
        url = "https://api.stackexchange.com/2.2/search?order=desc&sort=activity&intitle=perl&site=stackoverflow"
        resultados = helpers_vuelos.obtener_respuestas_mas_vieja_mas_actual(url)
        return Response(resultados)


# ==========================================================================================================================
# Vistas Helpers Vuelos
# ==========================================================================================================================


class AerolineaMasVuelos(APIView):

    def get(self, request):
        try:
            aeropuertos_mas_movimiento = helpers_vuelos.aeropuertos_mas_movimientos()
            return JsonResponse(
                {"aeropuertos_mas_movimiento": aeropuertos_mas_movimiento}
            )
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)})


class AerolineaMayorMovimientoAnio(APIView):

    def get(self, request):
        try:
            aerolinea_mayor_movimiento_anio = (
                helpers_vuelos.aerolinea_mayor_movimiento_anio()
            )
            return JsonResponse(
                {"aerolinea_mayor_movimiento_año": aerolinea_mayor_movimiento_anio}
            )
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)})


class DiaMayorNumeroVuelos(APIView):

    def get(self, request):
        try:
            dia_mayor_numero_vuelos = helpers_vuelos.dia_mayor_numero_vuelos()
            return JsonResponse({"dia_mayor_numero_vuelos": dia_mayor_numero_vuelos})
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)})


class AerolineasMasDosVuelosPorDia(APIView):

    def get(self, request):
        try:
            aerolineas_mas_dos_vuelos_por_dia = (
                helpers_vuelos.aerolineas_mas_dos_vuelos_por_dia()
            )
            return JsonResponse(
                {"aerolineas_mas_dos_vuelos_por_dia": aerolineas_mas_dos_vuelos_por_dia}
            )
        except Exception as e:
            print(e)
            return JsonResponse({"error": str(e)})
