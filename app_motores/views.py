from django.shortcuts import render, redirect, get_object_or_404
from .models import Motor

# Listar motores
def index(request):
    motores = Motor.objects.all()
    return render(request, 'listar_motores.html', {'motores': motores})

# Ver motor (opcional, puedes usarlo si quieres detalle)
def ver_motor(request, id):
    motor = get_object_or_404(Motor, id=id)
    return render(request, 'ver_motor.html', {'motor': motor})

# Agregar motor
def agregar_motor(request):
    if request.method == 'POST':
        marca = request.POST['marca']
        modelo = request.POST['modelo']
        Motor.objects.create(marca=marca, modelo=modelo)
        return redirect('inicio')
    return render(request, 'agregar_motor.html')

# Editar motor
def editar_motor(request, id):
    motor = get_object_or_404(Motor, id=id)
    if request.method == 'POST':
        motor.marca = request.POST['marca']
        motor.modelo = request.POST['modelo']
        motor.save()
        return redirect('inicio')
    return render(request, 'editar_motor.html', {'motor': motor})

# Borrar motor
def borrar_motor(request, id):
    motor = get_object_or_404(Motor, id=id)
    if request.method == 'POST':
        motor.delete()
        return redirect('inicio')
    return render(request, 'borrar_motor.html', {'motor': motor})
