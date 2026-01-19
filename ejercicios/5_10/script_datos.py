import os
import django

# Configura Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "studentsProject.settings")
django.setup()

from studentsProjectApp.models import Student

# Añadir estudiantes
Student.objects.create(name="Carlos", degree="Biologia")
Student.objects.create(name="Lucía", degree="Matematicas")

print("Estudiantes añadidos")
