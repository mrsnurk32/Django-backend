from rest_framework import serializers


class SuccessfulResponseSerializer(serializers.Serializer):
    detail = serializers.CharField(max_length=128)


class BadRequestResponseSerialzer(serializers.Serializer):
    detail = serializers.CharField(max_length=128)
    

class BadRequestDetailedResponseSerialzer(serializers.Serializer):
    detail = serializers.CharField(max_length=128)
    errors = serializers.DictField()