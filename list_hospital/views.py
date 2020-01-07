from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required


@login_required
def search(request):
    if request.POST:
        return redirect('list_hospitals', {'data': request.POST['data']})
    else:
        return render(request, 'list_hospitals/search.html', {})


@login_required
def list_hospitals(request, data):
    if not data:
        # Generate all kinds of Facilities
        hospitals = []
    else:
        # Generate Customised facilities
        hospitals = []
    return render(request, 'list_hospitals/index.html', {})
