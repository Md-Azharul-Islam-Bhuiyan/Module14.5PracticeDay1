from django import forms
from first_app.models import modelFormExercise

class ExerciseForm(forms.ModelForm):
    class Meta:
        model = modelFormExercise
        # fields = '__all__'
        exclude = ['image_field']
        widgets = {
            'date_field': forms.DateInput(attrs={'type':'date'}),
            'date_time_field': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
            
        }