from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse
import sqlite3
from django.views.decorators.csrf import csrf_exempt
from json import loads, dumps
import requests

# Create your views here.

# Servicio endpoint para hacer consultas a la base de datos
# que servirán para la realización de una tabla.
# Datos de entrada: {"id" :1}
# Datos de salida: {"1": 500, "2": 1000, "3": 1500, "4": 2000, "5": 2500, "6": 3000}
@csrf_exempt
def datosGrafica(request):
    body = request.body.decode('UTF-8')
    eljson = loads(body)
    id = eljson['id']

    con = sqlite3.connect("db.sqlite3")
    cur = con.cursor()
    res = cur.execute("SELECT nivel, puntaje FROM Partida WHERE estudiante=?", ([str(id)]))
    res = res.fetchall()
    res = dumps(dict(res))
    return HttpResponse(res)

# Servicio endpoint para graficar una tabla de acuerdo
# con datos obtenidos al llamar al servicio datosGrafica.
@csrf_exempt
def grafica(request):
    url = "http://127.0.0.1:8000/datosGrafica"
    header = {
    "Content-Type":"application/json"
    }
    payload = {   
    "id" : 1,
    }
    result = requests.post(url,  data = dumps(payload), headers = header)
    resultJson = result.json()

    if result.status_code == 200:
        elJSON = {'losDatos':resultJson}
        return render(request,'table.html',elJSON)
    else:
        res2 = {"estatus" : "Error"}
        res2 = dumps(res2)
        return HttpResponse(res2)