from rest_framework import serializers
from land import models


# ==========================================================================================================================
# Serializers Modelos App Vuelos Depth = 0
# ==========================================================================================================================


# Serializador SET Tipo Usuario
class SetAerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
        model = models.Aerolinea
        fields = "__all__"
        depth = 0


class SetAeropuertoSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
        model = models.Aeropuerto
        fields = "__all__"
        depth = 0


class SetMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
        model = models.Movimiento
        fields = "__all__"
        depth = 0


class SetVueloSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
        model = models.Vuelo
        fields = "__all__"
        depth = 0


# ==========================================================================================================================
# Serializers Modelos App Vuelos Depth = 1
# ==========================================================================================================================


# Serializador GET
class GetAerolineaSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
        model = models.Aerolinea
        fields = "__all__"
        depth = 1


class GetAeropuertoSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
        model = models.Aeropuerto
        fields = "__all__"
        depth = 1


class GetMovimientoSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
        model = models.Movimiento
        fields = "__all__"
        depth = 1


class GetVueloSerializer(serializers.ModelSerializer):
    class Meta:
        ordering = ["id"]
        model = models.Vuelo
        fields = "__all__"
        depth = 1
