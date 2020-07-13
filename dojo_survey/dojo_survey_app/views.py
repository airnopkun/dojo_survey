from django.shortcuts import render, redirect


def index(request):
    return render(request, "index.html")


def create_user(request):
    name_from_form = request.POST['name']
    location_from_form = request.POST['dojo_location']
    language_from_form = request.POST['favorite_language']
    gender_from_form = request.POST['gender']
    vehicles_from_form = ''
    if 'vehicle1' in request.POST:
        vehicles_from_form += request.POST['vehicle1'] + ', '
    if 'vehicle2' in request.POST:
        vehicles_from_form += request.POST['vehicle2'] + ', '
    if 'vehicle3' in request.POST:
        vehicles_from_form += request.POST['vehicle3'] + ', '
    vehicles_from_form = vehicles_from_form[:-2]
    comment_from_form = request.POST['comment']
    context = {
        "name_on_template": name_from_form,
        "location_on_template": location_from_form,
        "language_on_template": language_from_form,
        "gender_on_template": gender_from_form,
        "vehicles_on_template": vehicles_from_form,
        "comment_on_template": comment_from_form
    }
    print(request.POST)
    print(context)
    return render(request, "show.html", context)


def success(request):
    return render(request, "success.html")




