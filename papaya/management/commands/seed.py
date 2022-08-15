from django.core.management.base import BaseCommand
from papaya.models import Brands, Vehicles, Models
import random
from datetime import datetime


class Command(BaseCommand):
    help = "seed database"

    def handle(self, *args, **options):
        brand_names = ["Honda", "Yamaha", "Zoomo", "nothing"]
        print('creating brands')
        create_brands(brand_names)
        create_models(brand_names)
        create_vehicles()
        print('done')


def create_brands(brand_names):
    for n in brand_names:
        brand_obj = Brands(
            name=n,
            created_at= datetime.now(),
            updated_at=datetime.now()
        )
        brand_obj.save()


def create_models(brand_names):
    list_models = [{"name": 'Cx 1', "brand": random.choice(Brands.objects.all())},
                   {"name": 'PP 50', "brand": random.choice(Brands.objects.all())},
                   {"name": 'L99', "brand": random.choice(Brands.objects.all())},
                   {"name": '42', "brand": random.choice(Brands.objects.all())},
                   {"name": 'Best', "brand": random.choice(Brands.objects.all())},
                   {"name": 'Lower', "brand": random.choice(Brands.objects.all())}]
    for item in list_models:
        model_obj = Models(
            name=item.get("name", ""),
            brand_id=item.get("brand", ""),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        model_obj.save()


def create_vehicles():
    for x in range(50):
        vehicle_obj = Vehicles(
            name="Vehicle #" + str(x),
            legal_identifier=str(x),
            frame_size=random.randint(0,100),
            status=random.choice([0, 1, 2]),
            model_id=random.choice(Models.objects.all()),
            created_at=datetime.now(),
            updated_at=datetime.now()
        )
        vehicle_obj.save()
