from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator


class MyModel(models.Model):
    class Meta:
        abstract = True

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Employer(MyModel):
    class Meta:
        db_table = 'employers'

    name = models.CharField(max_length=255, unique=True, null=False)
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, null=False, default=1)
    employees = models.ManyToManyField(settings.AUTH_USER_MODEL, through='Employee', related_name='employees')

    def __str__(self):
        return f'{self.name}'


class Employee(MyModel):
    class Meta:
        db_table = 'employees'

    employer = models.ForeignKey(Employer, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    wage = models.DecimalField(
        max_digits=5,
        decimal_places=2,
        default=100.00,
        null=False,
        validators=[MinValueValidator(0.00)]
    )

    def __str__(self):
        return f'{self.id}'
