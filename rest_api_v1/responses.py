from drf_yasg import openapi
import rest_api_v1.serializers as response_serializers
from rest_framework.response import Response
from rest_framework import status
from rest_framework import serializers


# Response description provided for swagger schema

#Reponse consts
SUCCESS_200_DESCRIPTION = "Ok"
SUCCESS_201_DESCRIPTION = "Created"
BAD_REQUEST_400_DESCRIPTION = "Some fields were missing or were not accepted by validator.'"
UNAUTHORIZED_401_DESCRIPTION = "Check auth token"
NOT_FOUND_404_DESCRIPTION = "Not found"
SERVER_ERROR_500_DESCRIPTION = "Serverside error"


#Response helpers
def validate_response(func) -> Response:
    def wrapper(*args, **kwargs):
        status_, serializer = func(*args, **kwargs)
        is_valid = serializer.is_valid()
        assert(not is_valid, "Response serializer was not valid")
        return Response(status=status_, data=serializer.data)
    return wrapper


@validate_response
def serialized_response_200() -> dict:
    data=dict(detail=SUCCESS_200_DESCRIPTION)
    serializer = response_serializers.SuccessfulResponseSerializer(data=data)
    return status.HTTP_200_OK, serializer


@validate_response
def serialized_response_201() -> dict:
    data=dict(detail=SUCCESS_201_DESCRIPTION)
    serializer = response_serializers.SuccessfulResponseSerializer(data=data)
    return status.HTTP_201_CREATED, serializer


@validate_response
def serialized_response_400(errors:list[str]) -> dict:
    data=dict(detail=BAD_REQUEST_400_DESCRIPTION, errors=errors)
    serializer = response_serializers.BadRequestDetailedResponseSerialzer(data=data)
    return status.HTTP_400_BAD_REQUEST, serializer


@validate_response
def any_response(status: status, serializer: serializers) -> dict:
    return status, serializer


#Schema deatails
response_200 = openapi.Response(
    description=SUCCESS_200_DESCRIPTION,
    schema=response_serializers.SuccessfulResponseSerializer()
)

response_201 = openapi.Response(
    description=SUCCESS_201_DESCRIPTION,
    schema=response_serializers.SuccessfulResponseSerializer()
)

response_400 = openapi.Response(
    description=BAD_REQUEST_400_DESCRIPTION,
    schema=response_serializers.BadRequestDetailedResponseSerialzer()
)

response_401 = openapi.Response(
    description=UNAUTHORIZED_401_DESCRIPTION,
    schema=response_serializers.BadRequestResponseSerialzer()
)

response_404 = openapi.Response(
    description=NOT_FOUND_404_DESCRIPTION,
    schema=response_serializers.BadRequestResponseSerialzer()
)

response_500 = openapi.Response(
    description=SERVER_ERROR_500_DESCRIPTION,
    schema=response_serializers.BadRequestResponseSerialzer()
)