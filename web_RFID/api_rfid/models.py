from django.db import models
 
# Create your models here.

class Student(models.Model):
    CAREAR_CHOICES = (
        ('informatica', 'Ingeniería Informática'),
        ('comercio', 'Comercio Internacional'),
        ('obras', 'Ingeniería en Mantenimiento de Obras'),
    )
    SOLVENCY_STATUS_CHOICES = (
        (True, 'Solvente'),
        (False, 'Moroso'),
    )
    STATUS_CHOICES = (
        (True, 'Inscrito'),
        (False, 'No Inscrito'),
    )

    created = models.DateTimeField(auto_now_add=True, verbose_name='Fecha de registro')
    student_id = models.AutoField(primary_key=True, verbose_name="ID del Estudiante")
    cedula = models.CharField(max_length=12, verbose_name="Cédula")
    name = models.CharField(max_length=50, verbose_name="Primer Nombre")
    second_name = models.CharField(max_length=50, verbose_name="Segundo Nombre")
    last_name = models.CharField(max_length=50, verbose_name="Primer Apellido")
    second_last_name = models.CharField(max_length=50, verbose_name="Segundo Apellido")
    card_code = models.CharField(max_length=12, verbose_name="Código del Carnet")
    career = models.CharField(max_length=12, choices=CAREAR_CHOICES, verbose_name="Carreras")
    status = models.BooleanField(choices=STATUS_CHOICES, verbose_name="Estatus de inscripción")
    solvency_status = models.BooleanField(choices=SOLVENCY_STATUS_CHOICES, verbose_name="Solvencia")
    entry_time = models.DateTimeField(verbose_name='Fecha y Hora de entrada')
    

    class Meta:
        verbose_name = 'Estudiante'
        verbose_name_plural = 'estudiantes'
        ordering = ['student_id']
    
    def __str__(self):
        return self.name