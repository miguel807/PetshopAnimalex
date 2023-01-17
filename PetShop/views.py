from django.shortcuts import render
from PetShopApp.models import ProductosOfertas,ProductosMasVendidos,ProductosPerrosGatos,ProductosPeces,ProductosAves,ProductosHansterArdillas
from django.core.paginator import Paginator
# Create your views here.

def Home(request):

    datosProductosOfertas = ProductosOfertas.objects.all()
    datosProductosMasVentas = ProductosMasVendidos.objects.all()


    return render(request,'index.html',{"datosProductosOfertas":datosProductosOfertas,"datosProductosMasVentas":datosProductosMasVentas})

def PerrosGatos(request):

    listado_post = ProductosPerrosGatos.objects.all()
    paginator = Paginator(listado_post,15)
    pagina = request.GET.get('page') or 1
    post = paginator.get_page(pagina)
    paginaActual = int(pagina)
    paginas = range(1, post.paginator.num_pages + 1)


    return render(request,'tienda-PG.html',{"posts":post,"paginas":paginas,"paginaActual":paginaActual})


def Peces (request):
    listado_post =ProductosPeces.objects.all()
    paginator = Paginator(listado_post, 15) # muestra cantidad de card por paginas
    pagina = request.GET.get('page') or 1
    post = paginator.get_page(pagina)
    paginaActual = int(pagina)
    paginas = range(1, post.paginator.num_pages + 1)

    return render(request, 'tienda-PP.html', {"posts": post, "paginas": paginas, "paginaActual": paginaActual})


def Aves (request):
    listado_post =ProductosAves.objects.all()
    paginator = Paginator(listado_post, 15) # muestra cantidad de card por paginas
    pagina = request.GET.get('page') or 1
    post = paginator.get_page(pagina)
    paginaActual = int(pagina)
    paginas = range(1, post.paginator.num_pages + 1)

    return render(request, 'tienda-Aves.html', {"posts": post, "paginas": paginas, "paginaActual": paginaActual})



def HansterArdillas (request):

    listado_post =ProductosHansterArdillas.objects.all()
    paginator = Paginator(listado_post, 15) # muestra cantidad de card por paginas
    pagina = request.GET.get('page') or 1
    post = paginator.get_page(pagina)
    paginaActual = int(pagina)
    paginas = range(1, post.paginator.num_pages + 1)

    return render(request, 'tienda-hansterArdillas.html', {"posts": post, "paginas": paginas, "paginaActual": paginaActual})


def Contacto(request):
    return render(request,"contacto.html")
