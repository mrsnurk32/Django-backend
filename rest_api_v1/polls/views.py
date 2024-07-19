#REST FRAMEWORK imports
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework import authentication, permissions

#Documentation imports
from drf_yasg.utils import swagger_auto_schema

# Helpers
import rest_api_v1.responses as response_description

import polls.serializers as serializers
import polls.models as poll_models


# TO DO 
# Create Async poll request
# Create tests

class CreatePoll(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = serializers.PollSerializer

    @swagger_auto_schema(
        request_body=serializers.PollSerializer(),
        responses={
            201: response_description.response_201,
            400: response_description.response_400,
            401: response_description.response_401,
            500: response_description.response_500,
        })
    def post(self, request) -> Response:
        serializer = self.serializer_class(data=request.data)
        if not serializer.is_valid():
            return response_description.serialized_response_400(errors=serializer._errors)

        serializer.save()        
        return response_description.serialized_response_201()
    

class ReadPolls(APIView):
    serializer_class = serializers.PollListSerializer
    schema = response_description.response_200
    schema.schema = serializers.PollListSerializer()

    def query(self):
        query = poll_models.Poll.objects.all().values()
        return query

    @swagger_auto_schema(
        responses={
            200: schema,
            500: response_description.response_500,
        })
    def get(self, request) -> Response:
        query = self.query()
        serializer = self.serializer_class(data={"polls":query})
        response = response_description.any_response(status=status.HTTP_200_OK, serializer=serializer)
        return response