from django.shortcuts import render


# Create your views here.
def index(request):
    return render(request, "application/index.html")


def sect1(request):
    return render(request, 'application/spa_01.html')

def sect2(request):
    return render(request, 'application/spa_02.html')

def sect3(request):
    return render(request, 'application/spa_03.html')

def accueil(request):
    return render(request, 'application/accueil.html')



# def spa(request, nom_page):
#     if nom_page in ["01", "02", "03"]:
#         return render(request, f"application/spa_{nom_page}.html")
#     return render(request, "application/page_not_found.html")

