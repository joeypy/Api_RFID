from django.db import models
 
# Create your models here.

class Student(models.Model):
    CAREAR_CHOICES = (
        ('informatica', 'Informática'),
        ('comercio', 'Comercio'),
        ('civil', 'Civil'),
    )
    STATUS_CHOICES = (
        (True, 'Solvente'),
        (False, 'Moroso'),
    )
    student_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50, verbose_name="Estudiante")
    code = models.CharField(max_length=12, verbose_name="Codigo")
    carear = models.CharField(max_length=12, choices=CAREAR_CHOICES, verbose_name="Carrera")
    status = models.BooleanField(choices=STATUS_CHOICES, verbose_name="Estado")

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'estudiantes'
        ordering = ['student_id']
    
    def __str__(self):
        return self.name