from django.test import TestCase

# Create your tests here.
from django.test import TestCase
from celery import shared_task
from .tasks import add

class CeleryTasksTest(TestCase):

    def test_add_task(self):
        # Run the task directly
        result = add(4, 6)
        self.assertEqual(result, 10)

        # Alternatively, you can apply the task to test it asynchronously
        result = add.apply(args=[4, 6]).get()
        self.assertEqual(result, 10)
