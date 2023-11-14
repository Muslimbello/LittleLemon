from django.test import TestCase
from restaurant.models import Menu


class MenuModelTest(TestCase):
    def item1(self):
        item = Menu.objects.create(title="cake", price=45, inventory=2)
        self.assertEqual(item, "cake: 45")
