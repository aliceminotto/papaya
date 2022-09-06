from django.core.management.base import BaseCommand
from papaya.models import Brands, Vehicles, Models
import random
from datetime import datetime

class Command(BaseCommand):
    help = "test unique name"

    def handle(self, *args, **options):
        create_vehicle()


def create_vehicle():
    vehicle_obj = Vehicles(
        name="Vehicle #4",
        legal_identifier="100",
        frame_size=random.randint(0,100),
        status=random.choice([0, 1, 2]),
        model_id=random.choice(Models.objects.all()),
        created_at=datetime.now(),
        updated_at=datetime.now()
    )
    vehicle_obj.save()