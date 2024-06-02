from datetime import timezone
from faker import Faker

from crm.models import AppUser, Address, CustomerRelationship


def run():
    fake = Faker()
    for _ in range(3_000_000):
        address = Address.objects.create(
            street=fake.street_name(),
            street_number=fake.random_number(digits=5),
            city_code=fake.postalcode(),
            city=fake.city(),
            country=fake.country(),
        )

        appuser = AppUser.objects.create(
            address=address,
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            gender=fake.passport_gender(),
            customer_id=fake.random_number(digits=10),
            phone_number=fake.phone_number(),
            birthday=fake.date_of_birth(),
        )

        _ = CustomerRelationship.objects.create(
            appuser=appuser,
            points=fake.random_number(digits=4),
            last_activity=fake.date_time_this_year(before_now=True, tzinfo=timezone.utc),
        )
