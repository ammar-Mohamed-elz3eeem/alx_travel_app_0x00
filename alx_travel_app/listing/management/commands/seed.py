from django.core.management import BaseCommand
from django.contrib.auth.models import User
from listing.models import Listing, Booking, Review
from faker import Faker
from random import randint
fake = Faker()


class Command(BaseCommand):
    help = """Run seed followed by the number of instances you need from
    this the listing class, you can also pass an optional parameter represents
    the class you want to create (listing, review, booking)"""

    def add_arguments(self, parser):
        parser.add_argument("num_classes", type=int)
        parser.add_argument("--class", type=str, default='listing')

    def handle(self, *args, **options):
        for i in range(options['num_classes']):
            obj = None
            if options['class'] == 'listing':
                user = User.objects.get(pk=1)
                obj = Listing.objects.create(**{
                    'host_id': user,
                    'name': f'{fake.first_name().capitalize()}\'s \{fake.random_element(elements=[
                            'Villa',
                            'Cottage',
                            'Retreat',
                            'Hoven',
                            'Lodge'
                        ])}',
                    'description': fake.text(max_nb_chars=300),
                    'location': fake.address(),
                    'pricepernight': randint(50, 1000)
                })
                self.stdout.write(self.style.SUCCESS(f"Succuessfully created Listing {obj.name}"))
