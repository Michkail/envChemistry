import uuid
from faker import Faker
from users.models import CustomUser

i = Faker()
j = []

for _ in range(1000):
    j.append(CustomUser(id=uuid.uuid4(),
                        username=i.unique.user_name(),
                        email=i.email(),
                        password="pbkdf2_sha256$260000$" + i.password(length=20),
                        first_name=i.first_name(),
                        last_name=i.last_name(),
                        is_staff=i.boolean(chance_of_getting_true=30),
                        is_active=i.boolean(chance_of_getting_true=89),
                        is_superuser=i.boolean(chance_of_getting_true=14),
                        date_joined=i.date_time_this_decade(),
                        last_login=i.date_time_this_year()))

CustomUser.objects.bulk_create(j)
