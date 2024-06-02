from datetime import timezone
from faker import Faker

from crm.models import AppUser, Address, CustomerRelationship


def run():
    fake = Faker()
    
    addresses = []
    appusers = []
    crs = []
    for _ in range(3_000_000):
        address = Address(
            street=fake.street_name(),
            street_number=fake.random_number(digits=5),
            city_code=fake.postalcode(),
            city=fake.city(),
            country=fake.country(),
        )

        appuser = AppUser(
            first_name=fake.first_name(),
            last_name=fake.last_name(),
            gender=fake.passport_gender(),
            customer_id=fake.random_number(digits=10),
            phone_number=fake.phone_number(),
            birthday=fake.date_of_birth(),
        )

        cr = CustomerRelationship(
            points=fake.random_number(digits=4),
            last_activity=fake.date_time_this_year(before_now=True, tzinfo=timezone.utc),
        )
        addresses.append(address)
        appusers.append(appuser)
        crs.append(cr)
    
    addresses = Address.objects.bulk_create(addresses)
    for c, appuser in enumerate(appusers):
        appuser.address = addresses[c]
    appusers = AppUser.objects.bulk_create(appusers)
    for c, cr in enumerate(crs):
        cr.appuser = appusers[c]
    CustomerRelationship.objects.bulk_create(crs)
