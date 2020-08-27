from django.core.management.base import BaseCommand
from django_seed import Seed
from users.models import User


class Command(BaseCommand):

    help = "This command creates amenities"

    def add_arguments(self, parser):
        # 기본적으로 2명의 유저를 생성하고 tpye=int를 통해서 str에서 정수형으로 만들어 줍니다.
        parser.add_argument(
            "--number", default=2, type=int, help="How many users you want to create"
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()  # 인스턴스를 생성합니다.
        # 권한이 없는 일반 유저를 생성하고 싶으므로 스태프나 슈퍼유저가 아니도록 합니다.
        seeder.add_entity(User, number, {"is_staff": False, "is_superuser": False})
        seeder.execute()
        self.stdout.write(self.style.SUCCESS(f"{number} users created!"))
