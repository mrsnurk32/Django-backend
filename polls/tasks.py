# your_project_name/tasks.py
from celery import shared_task
from polls.serializers import PollSerializer

@shared_task
def create_poll(cleaned_data: dict):
    serializer = PollSerializer(data=cleaned_data)
    is_valid = serializer.is_valid()
    assert(not is_valid, "Task: create_poll, serializer not valid")
    serializer.save()