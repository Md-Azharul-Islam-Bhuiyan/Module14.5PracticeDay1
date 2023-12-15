from django.db import models
import datetime

class modelFormExercise(models.Model):
    name = models.CharField(max_length=255)
    roll = models.AutoField(primary_key=True)
    # big_auto_field = models.BigAutoField(primary_key=True)
    big_integer_field = models.BigIntegerField()
    binary_field = models.BinaryField()
    boolean_field = models.BooleanField()
    date_field = models.DateField()
    date_time_field = models.DateTimeField()
    decimal_field = models.DecimalField(max_digits=5, decimal_places=2)
    duration_field = models.DurationField()
    duration_field = models.DurationField()
    time_field = models.TimeField()
    url_field = models.URLField()
    uuid_field = models.UUIDField()
    small_integer_field = models.SmallIntegerField()
    slug_field = models.SlugField()
    positive_integer_field = models.PositiveIntegerField()
    positive_small_integer_field = models.PositiveSmallIntegerField()
    json_field = models.JSONField()
    generic_ip_address_field = models.GenericIPAddressField()
    image_field = models.ImageField()
    float_field = models.FloatField()
    