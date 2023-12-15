from django.shortcuts import render
from first_app.forms import Exampleforms

def home(request):
    if request.method == 'POST':
        form = Exampleforms(request.POST, request.FILES)
        if form.is_valid():
            
            file = form.cleaned_data['file']
            with open('./first_app/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)

            img = form.cleaned_data['img']
            with open('./first_app/upload/' + img.name, 'wb+') as destination:
                for chunk in img.chunks():
                    destination.write(chunk)
            # print(form.cleaned_data)
    else:
        form = Exampleforms()
    return render(request, 'home.html', {'form': form})
