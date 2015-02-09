from django.shortcuts import render

# Create your views here.


def home(request):
    print("in home")

    if request.method == 'POST':
        print("Posting address {} and plan {}".format(request.POST['address'], request.POST['plan']))

    return render(request, 'home.html')