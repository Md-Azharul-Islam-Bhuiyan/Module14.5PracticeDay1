from django.shortcuts import render
from first_app.forms import ExerciseForm
def home(request):
    if request.method == 'POST':
        form = ExerciseForm(request.POST)
        if form.is_valid():
            form.save()
            print(form.cleaned_data)
    else:
        form = ExerciseForm()
    return render(request, 'home.html', {'form': form})
