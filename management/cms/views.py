from django.shortcuts import render_to_response
from models import Student, Profesor

def index(request):
    lista = []
    profesori = Profesor.objects.all()
    for prof in profesori:
        record = []
        sir_clase = ''
        clase_prof = prof.clasa.all()
        for clasa in clase_prof:
            sir_clase += clasa.nume+" "

        row = 'Nume: '+prof.nume+' | Adresa: '+prof.adresa_domiciliu+\
                ' | Rol: profesor'+' | Clase: '+sir_clase
        record.append(row)

        lista_stud = []
        for clasa in clase_prof:
            studenti = clasa.student_set.all()
            for s in studenti:
                lista_stud.append(s.nume+" - Clasa "+clasa.nume)

        record.append(lista_stud)
        lista.append(record)

    return render_to_response('index.html', {
                                "lista" : lista,
                                })
