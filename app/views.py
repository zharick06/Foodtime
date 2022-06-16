from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import login
from .forms import *
from .models import *
from django.db.models import Max
import random
from app.Carrito import Carrito
from random import choice
from django.contrib.auth import get_user_model


# Create your views here.

def inicio(request):
    return render(request, 'inicio.html')

def contactanos(request):
    if request.method == 'POST':
        formulario = ContactoForm(data=request.POST)
        if formulario.is_valid():
            formulario.save()
        else:
            print("Ocurrio un error")
    return render(request, 'contactanos.html')

def resgistroMesero(request):
    municipios = Municipio.objects.all()
    data = {
        "municipios": municipios,
        "form":MeseroForm
    }
    if request.method=='POST':
        formulario = MeseroForm(data=request.POST, files=request.FILES)
        usuario = request.POST.get('usuario')
        if Mesero.objects.filter(usuario=usuario).exists():
            return redirect(to="login")
        else:
            if formulario.is_valid():
                username = request.POST.get('usuario')
                email = request.POST.get('correo')
                password = request.POST.get('contraseña')
                username = username.strip()
                email = email.strip()  # Eliminar espacios y líneas nuevas
                password = password.strip()
                if User.objects.filter(username=username).exists():
                    return redirect(to="login")
                formulario.save()
                user = User.objects.create_user(username, email, password)
                user.user_permissions.add(40)
                login(request, user)
                request.session['id'] = user.id
                return redirect(to="perfilM")
                
            else:
                data = {
                    "municipios": municipios,
                    "form":MeseroForm
                }
    return render(request, 'registration/resgistrarMesero.html', data)

def clavesAleatorias():
    longitud = 8
    valores = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    clave = ""
    clave = clave.join([choice(valores) for i in range(longitud)])
    return clave

def usuariosAleatoriosCaja(nombre):
    aleatorio1 = random.randint(0, 1000)
    aleatorio2 = random.randint(0, 1000)
    usernameAleatorioCaja = str(aleatorio1)+nombre+str(aleatorio2)
    return usernameAleatorioCaja

def usuariosAleatoriosCocina(nombre):
    aleatorio1 = random.randint(0, 1000)
    aleatorio2 = random.randint(0, 1000)
    usernameAleatorioCocina = nombre+str(aleatorio2)+str(aleatorio1)
    return usernameAleatorioCocina

def resgistroRestaurante(request):
    municipios = Municipio.objects.all()
    data = {
        "municipios": municipios,
        "form":RestauranteForm
    }
    if request.method=='POST':
        formulario = RestauranteForm(data=request.POST, files=request.FILES)
        nit = request.POST.get('nit')
        if Restaurante.objects.filter(nit=nit).exists():
            return redirect(to="login")
        else:
            if formulario.is_valid():
                username = request.POST.get('nit')
                email = request.POST.get('correo')
                password = request.POST.get('contraseña')
                nombre = request.POST.get('nombre')
                username = username.strip()
                email = email.strip()  # Eliminar espacios y líneas nuevas
                password = password.strip()
                nombre = nombre.strip()
                if User.objects.filter(username=username).exists():
                    return redirect(to="login")
                else:
                    formulario.save()
                    user = User.objects.create_user(username, email, password)
                    user.user_permissions.add(36)
                    login(request, user)
                    usernameCocina=usuariosAleatoriosCocina(nombre)
                    passwordCocina=clavesAleatorias()
                    user = User.objects.create_user(usernameCocina, email, passwordCocina)
                    global user_id
                    user_id = request.user.id
                    usuarioActivo = User.objects.get(id=user_id)
                    restaurante = Restaurante.objects.get(nit=usuarioActivo)
                    userCocina=Cocina()
                    userCocina.usuario=usernameCocina
                    userCocina.contraseña=passwordCocina
                    userCocina.restaurante=restaurante
                    userCocina.save()
                    usernameCaja=usuariosAleatoriosCaja(nombre)
                    passwordCaja=clavesAleatorias()
                    user = User.objects.create_user(usernameCaja, email, passwordCaja)
                    userCaja=Caja()
                    userCaja.usuario=usernameCaja
                    userCaja.contraseña=passwordCaja
                    userCaja.restaurante=restaurante
                    userCaja.save()
                    request.session['id'] = user.id
                    return redirect(to="perfilR")
                
            else:
                data = {
                    "municipios": municipios,
                    "form":RestauranteForm
                }
    return render(request, 'registration/resgistrarRestaurante.html', data)

def perfil(request):
    global user_id
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    if Restaurante.objects.filter(nit=usuarioActivo).exists()==True:
        return redirect(to="perfilR")
    if Mesero.objects.filter(usuario=usuarioActivo).exists()==True:
        return redirect(to="perfilM")

def perfilRestaurante(request):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    datosR = Restaurante.objects.filter(nit=usuarioActivo)

    data = {
        'datosR':datosR,
        'mesero':True
    }
    return render(request, 'perfiles/perfilRestaurante.html', data)

def perfilMesero(request):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    datosM = Mesero.objects.filter(usuario=usuarioActivo)
    data = {
        'datosM':datosM
    }
    return render(request, 'perfiles/perfilMesero.html', data)

def menuMesero(request):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    mesero = Mesero.objects.get(usuario=usuarioActivo)
    restaurante = Estado.objects.get(mesero=mesero, estado="AC").restaurante
    menu = Menu.objects.filter(restaurante=restaurante)
    categorias = Categoria.objects.all()
    mesas = Mesas.objects.filter(restaurante=restaurante)
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    data = {
        'menu':menu,
        'categorias':categorias,
        'mesas':mesas,
        'total_carrito': total
    }
    return render(request, 'menuMesero/menu.html', data)

def categoriasM(request, id):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    mesero = Mesero.objects.get(usuario=usuarioActivo)
    restaurante = Estado.objects.get(mesero=mesero, estado="AC").restaurante
    menu = Menu.objects.filter(categoria=id).filter(restaurante=restaurante)
    categorias = Categoria.objects.all()
    mesas = Mesas.objects.filter(restaurante=restaurante)
    total = 0
    if request.user.is_authenticated:
        if "carrito" in request.session.keys():
            for key, value in request.session["carrito"].items():
                total += int(value["acumulado"])
    data = {
        'menu':menu,
        'categorias':categorias,
        'mesas':mesas,
        'total_carrito': total
    }
    return render(request, 'menuMesero/categoria.html', data)

def detalleItem(request, id):
    item = Menu.objects.filter(id= id)
    data = {
        'item':item,
    }
    return render(request, 'menuMesero/detalle.html', data)

def agregar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Menu.objects.get(id=producto_id)
    carrito.agregar(producto)
    return redirect("menuM")

def eliminar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Menu.objects.get(id=producto_id)
    carrito.eliminar(producto)
    return redirect("menuM")

def restar_producto(request, producto_id):
    carrito = Carrito(request)
    producto = Menu.objects.get(id=producto_id)
    carrito.restar(producto)
    return redirect("menuM")

def limpiar_carrito(request):
    carrito = Carrito(request)
    carrito.limpiar()
    return redirect("menuM")

def orden(request, mesa):
    pedido = Pedido()
    pedido.mesa = Mesas.objects.get(id=mesa)
    pedido.estado = "AC"
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    mesero = Mesero.objects.get(usuario=usuarioActivo)
    pedido.mesero = mesero
    restaurante = Estado.objects.get(mesero=mesero, estado="AC").restaurante
    pedido.restaurante = restaurante
    pedido.save()

    carrito = Carrito(request).carrito
    for key, value in carrito.items():
        detalle = DestallePedido()
        maxPedido = Pedido.objects.latest('id').id
        detalle.pedido = Pedido.objects.get(id=maxPedido)
        detalle.articulo = Menu.objects.get(id=value.get("producto_id"))
        detalle.cantidad = value.get("cantidad")
        precio = Menu.objects.get(id=value.get("producto_id")).valor
        detalle.valor_unitario = precio
        detalle.save()

    limpiar_carrito(request)
    return redirect("menuM")

def menuRestaurante(request):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    restaurante = Restaurante.objects.get(nit=usuarioActivo)
    menu = Menu.objects.filter(restaurante=restaurante)
    categorias = Categoria.objects.all()
    data = {
        'menu':menu,
        'categorias':categorias
    }
    return render(request, 'menuRestaurante/menu.html', data)

def categoriasR(request, id):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    restaurante = Restaurante.objects.get(nit=usuarioActivo)
    menu = Menu.objects.filter(categoria=id).filter(restaurante=restaurante)
    categorias = Categoria.objects.all()
    data = {
        'menu':menu,
        'categorias':categorias
    }
    return render(request, 'menuRestaurante/categoria.html', data)

def agregar_item(request):
    categorias = Categoria.objects.all()
    data = {
        "form":MenuItemForm,
        'categorias':categorias
    }

    if request.method=='POST':
        formulario = MenuItemForm(data=request.POST, files=request.FILES)
        categoria = request.POST.get('categoria')
        if categoria != "categoria":
            if formulario.is_valid():
                nombre = request.POST.get('nombre')
                foto=request.FILES.get('foto')
                descripcion = request.POST.get('descripcion')
                valor = request.POST.get('valor')
                categoria = request.POST.get('categoria')
                nombre = nombre.strip()
                descripcion = descripcion.strip()
                valor = valor.strip()
                categoria = categoria.strip()
                item = Menu()
                item.nombre = nombre
                item.foto = foto
                item.descripcion = descripcion
                item.valor = valor
                categoria = Categoria.objects.get(id=categoria)
                item.categoria = categoria = categoria
                global user_id
                user_id = request.user.id
                user = User.objects.get(id=user_id)
                restaurante = Restaurante.objects.get(nit=user)
                item.restaurante = restaurante
                item.save()
                return redirect(to="menuR")
            else:
                data["form"] = formulario
        else:
            # anuncio de elegir categoria
            print("\n\n\n","Elige categoria","\n\n\n")
            data["form"] = formulario

    return render(request, 'menuRestaurante/agregar.html', data)

def editar_item(request, id):
    item = get_object_or_404(Menu, id=id)
    if Menu.objects.get(id=id).foto:      
        ruta = Menu.objects.get(id=id).foto.url
    else:
        ruta = ""
    data = {
        'form': MenuItemForm(instance=item),
        'url' : ruta
    }
    if request.method=='POST':
        formulario = MenuItemForm(data=request.POST, instance=item, files=request.FILES)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="menuR")
        else:
            data["form"] = formulario
    return render(request, 'menuRestaurante/editar.html', data)

def eliminar_item(request, id):
    item = get_object_or_404(Menu, id=id)
    item.delete()
    return redirect(to="menuR")

def mesasMesero(request):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    mesero = Mesero.objects.get(usuario=usuarioActivo)
    restaurante = Estado.objects.get(mesero=mesero, estado="AC").restaurante
    mesas = Mesas.objects.filter(restaurante=restaurante)
    data = {
        'mesas':mesas
    }
    return render(request, 'mesasMesero/mesas.html', data)

def mesasRestaurante(request):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    restaurante = Restaurante.objects.get(nit=usuarioActivo)
    mesas = Mesas.objects.filter(restaurante=restaurante)
    data = {
        'mesas':mesas
    }
    return render(request, 'mesasRestaurante/mesas.html', data)

def agregar_mesa(request):
    data = {
        "form":MesasForm
    }

    if request.method=='POST':
        formulario = MesasForm(data=request.POST)
        if formulario.is_valid():
            nombre = request.POST.get('nombre')
            nombre = nombre.strip()
            mesa = Mesas()
            mesa.nombre = nombre
            mesa.estado = "A"
            global user_id
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            restaurante = Restaurante.objects.get(nit=user)
            mesa.restaurante = restaurante
            mesa.save()
            return redirect(to="mesasR")
        else:
            data["form"] = formulario

    return render(request, 'mesasRestaurante/agregar.html', data)

def editar_mesa(request, id):
    mesa = get_object_or_404(Mesas, id=id)
    data = {
        'form': MesasForm(instance=mesa),
    }
    if request.method=='POST':
        formulario = MesasForm(data=request.POST, instance=mesa)
        if formulario.is_valid():
            formulario.save()
            return redirect(to="mesasR")
        else:
            data["form"] = formulario
    return render(request, 'mesasRestaurante/editar.html', data)

def eliminar_mesa(request, id):
    mesa = get_object_or_404(Mesas, id=id)
    mesa.delete()
    return redirect(to="mesasR")

def activar_mesa(request, id):
    Mesas.objects.filter(id=id).update(estado="A")
    global user_id
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    if Restaurante.objects.filter(nit=usuarioActivo).exists()==True:
        return redirect(to="mesasR")
    if Mesero.objects.filter(usuario=usuarioActivo).exists()==True:
        return redirect(to="mesasM")

def desactivar_mesa(request, id):
    Mesas.objects.filter(id=id).update(estado="I")
    global user_id
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    if Restaurante.objects.filter(nit=usuarioActivo).exists()==True:
        return redirect(to="mesasR")
    if Mesero.objects.filter(usuario=usuarioActivo).exists()==True:
        return redirect(to="mesasM")

def ofertas(request):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    restaurante = Restaurante.objects.get(nit=usuarioActivo)
    oferta = Oferta.objects.filter(restaurante=restaurante)
    data = {
        'oferta': oferta
    }
    return render(request, 'ofertas/ofertas.html', data)

def detalleOferta(request, id):
    oferta = Oferta.objects.filter(id= id)
    data = {
        'oferta':oferta,
    }
    return render(request, 'ofertas/detalle.html', data)

def publicar_oferta(request):
    data = {
        "form":OfertaForm
    }

    if request.method=='POST':
        formulario = OfertaForm(data=request.POST)
        if formulario.is_valid():
            descripcion = request.POST.get('descripcion')
            pago = request.POST.get('pago')
            vacantes = request.POST.get('vacantes')
            descripcion = descripcion.strip()
            pago = pago.strip()
            vacantes = vacantes.strip()
            oferta = Oferta()
            oferta.descripcion = descripcion
            oferta.pago = pago
            oferta.vacantes = vacantes
            global user_id
            user_id = request.user.id
            user = User.objects.get(id=user_id)
            restaurante = Restaurante.objects.get(nit=user)
            oferta.restaurante = restaurante
            direccion = Restaurante.objects.get(nit=user).direccion
            oferta.direccion= direccion
            telefono = Restaurante.objects.get(nit=user).telefono
            oferta.telefono= telefono
            oferta.save()
            return redirect(to="ofertas")
        else:
            data["form"] = formulario

    return render(request, 'ofertas/agregar.html', data)

def eliminar_oferta(request, id):
    postulaciones=Postulados.objects.filter(oferta=id)
    postulaciones.delete()
    oferta = get_object_or_404(Oferta, id=id)
    oferta.delete()
    return redirect(to="ofertas")

def meseros(request):
    global user_id
    user_id = request.user.id
    user = User.objects.get(id=user_id)
    restaurante = Restaurante.objects.get(nit=user)
    estados = Estado.objects.filter(restaurante=restaurante).filter(estado="AC")
    docs = set()
    for e in estados:
        document = Mesero.objects.get(documento=e.mesero)
        docs.add(document)
    meseros = Mesero.objects.filter(documento__in=docs)
    data = {
        'meseros':meseros
    }
    return render(request, 'meseros/meseros.html', data)

def activar_mesero(request):
    if request.method=='POST':
        global user_id
        user_id = request.user.id
        user = User.objects.get(id=user_id)
        mesero = request.POST.get('mesero')
        mesero = mesero.strip()
        if Mesero.objects.filter(documento=mesero).exists():
            if Estado.objects.filter(mesero=mesero).exists():
                for t in Estado.objects.filter(mesero=mesero):
                    print(t)
                    if t.estado!="AC":
                        permiso = Estado()
                        docMesero = Mesero.objects.get(documento=mesero)
                        permiso.mesero = docMesero
                        restaurante = Restaurante.objects.get(nit=user)
                        permiso.restaurante = restaurante
                        permiso.estado = 'AC'
                        permiso.save()
                        userMesero = Mesero.objects.get(documento=mesero).usuario
                        u = User.objects.get(username=userMesero)
                        u.user_permissions.add(44)
                        return redirect(to="meseros")
                    else:
                        print("Este mesero esta activo, no puede ser activado hasta ser desactivado")
                        break
            else:
                permiso = Estado()
                docMesero = Mesero.objects.get(documento=mesero)
                permiso.mesero = docMesero
                restaurante = Restaurante.objects.get(nit=user)
                permiso.restaurante = restaurante
                permiso.estado = 'AC'
                permiso.save()
                userMesero = Mesero.objects.get(documento=mesero).usuario
                u = User.objects.get(username=userMesero)
                u.user_permissions.add(44)
                return redirect(to="meseros")
        else:
            print("No existe este mesero")

    return render(request, 'meseros/activar.html')

def desactivar_mesero(request, documento):
    id=Estado.objects.get(mesero=documento, estado="AC").id
    Estado.objects.filter(id=id).update(estado="IN")
    userMesero = Mesero.objects.get(documento=documento).usuario
    u = User.objects.get(username=userMesero)
    u.user_permissions.remove(44)
    return redirect(to="meseros")

def vacantes(request):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    mesero = Mesero.objects.get(usuario=usuarioActivo)
    listPostuladas = []
    postudados=Postulados.objects.filter(mesero=mesero)
    for p in  postudados:
        listPostuladas.append(p.oferta.id)
    oferta = Restaurante.objects.select_related('nombre').all()

    data = {
        'oferta': oferta
    }
    return render(request, 'vacantes/vacantes.html', data)

def detalleVacante(request, id):
    oferta = Oferta.objects.raw("SELECT app_oferta.*, app_restaurante.nombre FROM app_oferta LEFT JOIN app_restaurante ON app_restaurante.nit = app_oferta.restaurante_id WHERE app_oferta.id=%s"% id)
    data = {
        'oferta':oferta,
    }
    return render(request, 'vacantes/detalle.html', data)

def postular(request, id):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    mesero = Mesero.objects.get(usuario=usuarioActivo)
    oferta = Oferta.objects.get(id=id)
    postulante = Postulados()
    postulante.oferta = oferta
    postulante.mesero = mesero
    postulante.save()
    return redirect(to="vacantes")

def caja(request):
    
    return render(request, 'caja/caja.html')

def administrador(request):
    municipios = Municipio.objects.all()
    data = {
        'municipios': municipios
    }
    return render(request, 'administrador/administrador.html', data)

def restaurantes(request, id):
    restaurantes_ciudad = Restaurante.objects.filter(municipio=id)
    data = {
        'restaurantes': restaurantes_ciudad
    }
    return render(request, 'restaurantes/restaurantes.html', data)

def facturas(request, mesa):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    mesero = Mesero.objects.get(usuario=usuarioActivo)
    restaurante = Estado.objects.get(mesero=mesero, estado="AC").restaurante
    datos= Menu.objects.raw("SELECT app_menu.id, app_menu.nombre, app_menu.valor, app_destallepedido.cantidad, app_menu.valor*app_destallepedido.cantidad as precio FROM app_destallepedido RIGHT JOIN app_pedido ON app_pedido.id = app_destallepedido.pedido_id INNER JOIN app_menu ON app_menu.id = app_destallepedido.articulo_id  WHERE app_pedido.restaurante_id='{}' AND app_pedido.mesa_id='{}' AND app_pedido.estado='AC'".format(restaurante, mesa))
    mesa= Pedido.objects.raw("SELECT app_pedido.id, app_pedido.mesa_id FROM app_destallepedido RIGHT JOIN app_pedido ON app_pedido.id = app_destallepedido.pedido_id INNER JOIN app_menu ON app_menu.id = app_destallepedido.articulo_id  WHERE app_pedido.restaurante_id='{}' AND app_pedido.mesa_id='{}' AND app_pedido.estado='AC' LIMIT 1".format(restaurante, mesa))
    data = {
        'datos': datos,
        'mesa': mesa
    }
    return render(request, 'facturas/facturas.html', data)

def cocina(request):
    global user_id 
    user_id = request.user.id
    usuarioActivo = User.objects.get(id=user_id)
    mesero = Mesero.objects.get(usuario=usuarioActivo)
    restaurante = Estado.objects.get(mesero=mesero, estado="AC").restaurante
    datos= Menu.objects.raw("SELECT app_menu.id, app_destallepedido.id as id_detalle, app_menu.nombre, app_destallepedido.cantidad, app_menu.foto FROM app_destallepedido RIGHT JOIN app_pedido ON app_pedido.id = app_destallepedido.pedido_id INNER JOIN app_menu ON app_menu.id = app_destallepedido.articulo_id  WHERE app_pedido.restaurante_id='%s' AND app_destallepedido.estado='PE'"% restaurante)
    data = {
        'datos': datos
    }
    return render(request, 'cocina/cocina.html', data)

def finalizarPedido(request, id):
    DestallePedido.objects.filter(id=id).update(estado="FI")
    return redirect(to="cocina")

def cancelarPedido(request, id):
    DestallePedido.objects.filter(id=id).update(estado="CA")
    return redirect(to="cocina")

def cancelarFacturas(request, mesa):
    Pedido.objects.filter(mesa=mesa).filter(estado="AC").update(estado="CA")
    return redirect(facturas, mesa=mesa)

def pagarFacturas(request, mesa):
    Pedido.objects.filter(mesa=mesa).filter(estado="AC").update(estado="PA")
    return redirect(facturas, mesa=mesa)