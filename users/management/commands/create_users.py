from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    def handle(self, *args, **options):
        user = User.objects.create(
            email="nataly353natali@yandex.ru",
            is_active=True,
        )
        user.set_password("Yd9+MAqjY6SEQUq")
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"Created user {user.email}")
        )
        user = User.objects.create(
            email="nataly353natali@yandex.ru",
            is_active=True,
        )
        user.set_password("Yd9+MAqjY6SEQUq")
        user.save()
        self.stdout.write(
            self.style.SUCCESS(f"Created user {user.email}")
        )
