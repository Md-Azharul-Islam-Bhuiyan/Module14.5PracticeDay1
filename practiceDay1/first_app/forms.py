from django import forms
import datetime

class Exampleforms(forms.Form):
    name = forms.CharField(max_length=5)
    comment1 =forms.CharField(widget=forms.Textarea)
    comment2 = forms.CharField(widget=forms.Textarea(attrs={'rows':3}))
    email = forms.EmailField(required = False,label="Please enter your email address")
    agree = forms.BooleanField()
    birth_date = forms.DateField(widget=forms.NumberInput(attrs={'type': 'date'}))
    BIRTH_YEAR_CHOICES = ['1980', '1981', '1982']
    birth_year = forms.DateField(widget=forms.SelectDateWidget(years=BIRTH_YEAR_CHOICES))
    value = forms.DecimalField()
    day = forms.DateField(initial=datetime.date.today)
    FAVORITE_COLORS_CHOICES = [('blue', 'Blue'),('green', 'Green'),('black', 'Black'),]
    favorite_color = forms.ChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favoriteColor = forms.ChoiceField(widget=forms.RadioSelect, choices=FAVORITE_COLORS_CHOICES)
    favorite_colors = forms.MultipleChoiceField(choices=FAVORITE_COLORS_CHOICES)
    favorite_colors2 = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,choices=FAVORITE_COLORS_CHOICES)
    roll_number = forms.IntegerField(help_text = "Enter 6 digit roll number")  
    floatField = forms.FloatField()
    password = forms.CharField(widget = forms.PasswordInput())
    field1 = forms.DurationField()
    field2 = forms.DateTimeField(widget=forms.DateTimeInput(attrs={'type': 'datetime-local'}))
    file = forms.FileField()
    img = forms.ImageField() 