from django.shortcuts import render, redirect
from .models import Category, Photo

# Create your views here.

#filtram pagina principala in functie de ce categorie e selectata
#daca nu este selectata nici o categorie atunci sunt selectate toate

def gallery(request):
    category = request.GET.get("category")
    if category == None:
        photos = Photo.objects.all()
    else:
        photos = Photo.objects.filter(category__name = category)

    categories = Category.objects.all()
    context = {"categories": categories, "photos":photos}
    return render(request, "photos/gallery.html", context)

#deschide poza +

def viewPhoto(request, pk):
    photo = Photo.objects.get(id=pk)
    return render(request, "photos/photo.html", {"photo":photo})


#adauga functionalitatea de a adauga poze
#atunci cand adaugam o poza noua este adaugata in folderul images
#impreuna cu categoria ei. se pot adauga si poze fara o categorie anume
#sau daca in lista nu se gaseste categoria potrivita atunci se creaza o categorie noua

def addPhoto(request):
    categories = Category.objects.all()
    if request.method == "POST":
        data = request.POST
        image = request.FILES.get("image")

        if data["category"] != "none":
            category = Category.objects.get(id=data["category"])
        elif data["category_new"] != "":
            category, created = Category.objects.get_or_create(name=data["category_new"])
        else:
            category = None

        photo = Photo.objects.create(
            category=category,
            description=data["description"],
            image=image,
        )

        return redirect("gallery")

    context = {"categories": categories}
    return render(request, "photos/add.html", context)

