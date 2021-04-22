from django.test import TestCase
from .models import Item


class TestModels(TestCase):

    def test_done_defaults_to_faults(self):
        item = Item.objects.create(name='Test ToDo Item')
        self.assertFalse(item.done) 