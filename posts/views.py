from turtle import title
from django.shortcuts import render
from .models import Experiment, MaterialsList, Procedure


def index(request):
    experiments = Experiment.objects.all()
    return render(request, 'index.html', {'experiments': experiments})


def post(request, name):
    experiment = Experiment.objects.get(title=name)
    materials = MaterialsList.objects.filter(experiment_id=experiment.id)
    procedures = Procedure.objects.filter(experiment_id=experiment.id)
    return render(request, 'post.html',
                  {'experiment': experiment,
                   'materials': list(materials.values()),
                   'procedures': list(procedures.values()),
                   }
                  )
