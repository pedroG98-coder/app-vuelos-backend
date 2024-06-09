from django.db import models
from django.contrib.auth.models import AbstractUser


# ==========================================================================================================================
# Model User
# ==========================================================================================================================


class User(AbstractUser):
    pass


# ==========================================================================================================================
# Model Aerolinea
# ==========================================================================================================================


class Aerolinea(models.Model):
    nombre_aerolinea = models.CharField(max_length=100)
    estatus_sistema = models.BooleanField(
        "Estatus en el Sistema",
        default=True,
        help_text="True si está activo, False si está eliminado.",
    )

    def __str__(self):
        return str(self.id) + str(self.nombre_aerolinea)

    class Meta:
        verbose_name = "Aerolinea"
        verbose_name_plural = "Aerolineas"


# ==========================================================================================================================
# Model Aeropuerto
# ==========================================================================================================================


class Aeropuerto(models.Model):
    nombre_aeropuerto = models.CharField(max_length=100)
    estatus_sistema = models.BooleanField(
        "Estatus en el Sistema",
        default=True,
        help_text="True si está activo, False si está eliminado.",
    )

    def __str__(self):
        return str(self.id) + str(self.nombre_aeropuerto)

    class Meta:
        verbose_name = "Aeropuerto"
        verbose_name_plural = "Aeropuertos"


# ==========================================================================================================================
# Model Movimiento
# ==========================================================================================================================


class Movimiento(models.Model):
    descripcion = models.CharField(max_length=100)
    estatus_sistema = models.BooleanField(
        "Estatus en el Sistema",
        default=True,
        help_text="True si está activo, False si está eliminado.",
    )

    def __str__(self):
        return str(self.id) + str(self.descripcion)

    class Meta:
        verbose_name = "Movimiento"
        verbose_name_plural = "Movimiento"


# ==========================================================================================================================
# Model Vuelo
# ==========================================================================================================================


class Vuelo(models.Model):
    aerolinea = models.ForeignKey(Aerolinea, on_delete=models.CASCADE)
    aeropuerto = models.ForeignKey(Aeropuerto, on_delete=models.CASCADE)
    movimiento = models.ForeignKey(Movimiento, on_delete=models.CASCADE)
    dia = models.DateField()
    estatus_sistema = models.BooleanField(
        "Estatus en el Sistema",
        default=True,
        help_text="True si está activo, False si está eliminado.",
    )

    def __str__(self):
        return str(self.id)

    class Meta:
        verbose_name = "Vuelo"
        verbose_name_plural = "Vuelos"
