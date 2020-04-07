import statistics

from django.http import HttpResponse
from django.template import loader
from .models import CPUData


def index(request):
    obj = CPUData.objects.all()
    obj_100 = obj.order_by("-id")[:100]
    template = loader.get_template('core/index.html')
    cpu = [x.cpu for x in obj]
    cpu_100 = cpu[-100:]
    avg = statistics.mean(cpu)
    avg_100 = statistics.mean(cpu_100)
    cpu_min = min(cpu)
    cpu_min_100 = min(cpu_100)
    cpu_max = max(cpu)
    cpu_max_100 = max(cpu_100)
    context = {'obj': obj_100, 'avg': avg, 'avg_100': avg_100,
               'cpu_min': cpu_min, 'cpu_max': cpu_max, 
               'cpu_min_100': cpu_min_100, 'cpu_max_100': cpu_max_100
               }
    return HttpResponse(template.render(context, request))


def add(request):
    if request.method == "POST":
        data = request.POST
        date = data['date']
        cpu_data = data['cpu']
        cpu = CPUData(date=date, cpu=cpu_data)
        cpu.save()

    return HttpResponse(201)
