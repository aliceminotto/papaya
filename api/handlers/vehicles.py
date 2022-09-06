from papaya.models import Vehicles
import json
from django.http import HttpResponse

def get_all(request):
    list_vehicles = Vehicles.objects.all()
    temp = []
    for obj in list_vehicles:
        temp.append({"name": obj.name})
    return HttpResponse(json.dumps(temp), content_type="application/json")
