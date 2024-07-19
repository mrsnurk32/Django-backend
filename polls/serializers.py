from rest_framework import serializers
import polls.models as poll_models


class PollSerializer(serializers.ModelSerializer):
    class Meta:
        model = poll_models.Poll
        fields = '__all__'


class PollListSerializer(serializers.Serializer):
    polls = PollSerializer(many=True)
