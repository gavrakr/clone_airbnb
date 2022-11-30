from django.core.management.base import BaseCommand
from rooms.models import Amenity

class Command(BaseCommand):
    
    help = "This command create Amenities."
     
    """def add_arguments(self, parser):
        parser.add_argument ("--times", help = "Do you know that?",)
        times = int(options.get("times"))
        for t in range(0, times):
            self.stdout.write(self.style.SUCCESS("It is Test Line."))
            #self.stdout.write(self.style.ERROR("It is Test Line."))
            #self.stdout.write(self.style.WARNING("It is Test Line."))"""

    #def handle(self, *args, **options):
    #    times = int(options.get("times"))
    #    for t in range(0, times):
    #        print("It is Test Line.")

    def handle(self, *args, **options):

        amenities = [
            "Wifi",
            "Kitchen",
            "Washer",
            "Dryer",
            "Air conditioning",
            "Heating",
            "Dedicated workspace",
            "TV",
            "Hair dryer",
            "Iron",
            "Pool",
            "Hot tub",
            "Free parking on premises",
            "EV charger",
            "Crib",
            "Gym",
            "BBQ grill",
            "Breakfast",
            "Indoor fireplace",
            "Smoking allowed",
            "Beachfront",
            "Waterfront",
            "Ski-in/ski-out",
            "Smoke alarm",
            "Carbon monoxide alarm",
        ]

        for a in amenities:
            Amenity.objects.create(name=a)
        self.stdout.write(self.style.SUCCESS(f"{len(amenities)} Amenity Create!"))