from django.core.management.base import BaseCommand
from django_seed import Seed
from rooms import models as room_models
from users import models as user_models
import random


class Command(BaseCommand):
    
    help = "This command create Facilities."

    def add_arguments(self, parser):
        parser.add_argument ("--number", default=2, type=int, help="How many users do you want to create? ",)
 

    def handle(self, *args, **options):
        number = options.get("number",)
        seeder = Seed.seeder()
        users = user_models.User.objects.all()
        room_type = room_models.RoomType.objects.all()
        print(room_type, users)
        seeder.add_entity(room_models.Room, number, {
            "host" : lambda x : random.choice(users),
            "room_type" : lambda x : random.choice(room_type),
        },)
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} Rooms Create!"))