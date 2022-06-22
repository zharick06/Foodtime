from pyexpat import model
from weakref import proxy
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Contacto(models.Model):
    nombre = models.CharField(max_length=100)
    correo = models.CharField(max_length=50)
    mensaje = models.TextField()

class Departamento(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Municipio(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

opciones_genero = [
    ["F", "Femenino"],
    ["M", "Masculino"],
    ["O", "Otro"]
]

opciones_documento = [
    ["TI", "Tarjeta de Identidad"],
    ["CC", "Cedula de Ciudadania"],
    ["O", "Otro"]
]

class Mesero(models.Model):
    documento = models.CharField(primary_key=True, max_length=12, null=False)
    tipodoc = models.CharField(choices=opciones_documento, max_length=2)
    nombres = models.CharField(max_length=20)
    apellidos = models.CharField(max_length=20)
    correo = models.CharField(max_length=50)
    telefono = models.CharField(max_length=12)
    genero = models.CharField(choices=opciones_genero, max_length=1)
    direccion = models.CharField(max_length=30)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)
    foto = models.ImageField(upload_to="meseros", blank=True, null=True)
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=100)

    def __str__(self):
        return self.documento

class Restaurante(models.Model):
    nit = models.CharField(primary_key=True, null=False, max_length=20)
    nombre = models.CharField(max_length=70)
    correo = models.CharField(max_length=50)
    logo = models.ImageField(upload_to="logos", blank=True, null=True)
    municipio = models.ForeignKey(Municipio, on_delete=models.SET_NULL, blank=True, null=True)
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    celular = models.CharField(max_length=15)
    contraseña = models.CharField(max_length=100)    

    def __str__(self):
        return self.nit

class Cocina(models.Model):
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=100)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.usuario

class Caja(models.Model):
    usuario = models.CharField(max_length=20)
    contraseña = models.CharField(max_length=100)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.usuario

class Oferta(models.Model):
    descripcion = models.TextField()
    vacantes = models.IntegerField()
    pago = models.IntegerField()
    direccion = models.CharField(max_length=50)
    telefono = models.CharField(max_length=15)
    fecha_publicacion = models.DateField(auto_now_add=True ,blank=True, null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, blank=True, null=True)

opciones_estado_mesas = [
    ["I", "Inactivo"],
    ["A", "Activo"],
]

class Mesas(models.Model):
    nombre = models.CharField(max_length=50)
    estado = models.CharField(choices=opciones_estado_mesas, max_length=1)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self):
        return self.nombre

class Categoria(models.Model):
    nombre = models.CharField(max_length=20)

    def __str__(self):
        return self.nombre

class Menu(models.Model):
    nombre = models.TextField()
    foto =  models.ImageField(upload_to="menu", blank=True, null=True)
    descripcion = models.TextField(max_length=100)
    valor = models.IntegerField()
    categoria = models.ForeignKey(Categoria, on_delete=models.SET_NULL, blank=True, null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, blank=True, null=True)

opciones_estado_pedido = [
    ["IN", "Inactivo"],
    ["AC", "Activo"],
]

class Pedido(models.Model):
    mesa = models.ForeignKey(Mesas, on_delete=models.SET_NULL, blank=True, null=True)
    estado = models.CharField(choices=opciones_estado_pedido, max_length=2)
    fecha = models.DateField(auto_now_add=True ,blank=True, null=True)
    mesero = models.ForeignKey(Mesero, on_delete=models.SET_NULL, blank=True, null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, blank=True, null=True)

class DestallePedido(models.Model):
    pedido = models.ForeignKey(Pedido, on_delete=models.SET_NULL, blank=True, null=True)
    articulo = models.ForeignKey(Menu, on_delete=models.SET_NULL, blank=True, null=True)
    cantidad = models.IntegerField()
    valor_unitario = models.IntegerField()
    estado = models.CharField(choices=opciones_estado_pedido, max_length=2, default='PE')


opciones_estado = [
    ["IN", "Inactivo"],
    ["AC", "Activo"],
]

class Estado(models.Model):
    mesero = models.ForeignKey(Mesero, on_delete=models.SET_NULL, blank=True, null=True)
    restaurante = models.ForeignKey(Restaurante, on_delete=models.SET_NULL, blank=True, null=True)
    hora_entrada = models.TimeField(auto_now_add=True ,blank=True, null=True)
    hora_salida = models.TimeField(auto_now_add=True ,blank=True, null=True)
    estado = models.CharField(choices=opciones_estado, max_length=2)

class Postulados(models.Model):
    oferta = models.ForeignKey(Oferta, on_delete=models.SET_NULL, blank=True, null=True)
    fecha = models.DateField(auto_now_add=True ,blank=True, null=True)
    mesero = models.ForeignKey(Mesero, on_delete=models.SET_NULL, blank=True, null=True)

