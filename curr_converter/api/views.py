from django.http.request import HttpRequest
from rest_framework import status, generics
from rest_framework.response import Response
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from api.models import Converter


class ConverterView(generics.GenericAPIView):
    """View implementation for The Currency Converter API."""

    # Variable used for swagger decorator to describe a parameter of API method
    from_param = openapi.Parameter(
        name="from",
        in_=openapi.IN_QUERY,
        description="Origin currency",
        type=openapi.TYPE_STRING,
        required=True
    )

    # Variable used for swagger decorator to describe a parameter of API method
    to_param = openapi.Parameter(
        name="to",
        in_=openapi.IN_QUERY,
        description="Target currency",
        type=openapi.TYPE_STRING,
        required=True
    )

    # Variable used for swagger decorator to describe a parameter of API method
    amount_param = openapi.Parameter(
        name="amount",
        in_=openapi.IN_QUERY,
        description="Amount to convert",
        type=openapi.TYPE_NUMBER,
        required=True
    )

    # Variable used for swagger decorator to describe a response of API method
    default_response = openapi.Response(
        description="Success",
        schema=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                "message": openapi.Schema(type=openapi.TYPE_STRING),
                "result": openapi.Schema(type=openapi.TYPE_NUMBER)
            }
        ),
        examples={
            "application/json": {
                "message": "success",
                "result": 5.12
            }
        }
    )

    # Swagger decorator used for generate the API documentation
    @swagger_auto_schema(
        operation_description="Converts an amount of a currency into another currency.",
        operation_id="convertsAnAmount",
        manual_parameters=[from_param, to_param, amount_param],
        responses={200: default_response},
        tags=["Convert an amount"]
    )
    def get(self, request: HttpRequest):
        """Returns a response with amount converted for the target currency.
        
        Parameters
        ----------
            - request (HttpRequest): The Django Request Object.
        
        Returns
        -------
            - response (Response): Response with the message of success or failed,
            the amount converted in case of success and the request's status code.
        """

        try:
            # Getting parameters of the request
            from_curr = request.GET.get("from", "")
            to_curr = request.GET.get("to", "")
            amount = float(request.GET.get("amount", 0.0))
            
            # Converting the amount
            converter = Converter(from_curr, to_curr, amount)
            result = converter.convert_amount()
            
            # Returning the result
            if result != 0.0:
                data = {
                    "message": "success",
                    "result": result
                }
                return Response(data, status=status.HTTP_200_OK)
            else:
                msg = "An unexpected error occurred! " \
                    "Check currencies symbols and the amount or try again later..."
                return Response({"message": msg}, status=status.HTTP_503_SERVICE_UNAVAILABLE)
        except Exception as e:
            return Response({"message": e}, status=status.HTTP_400_BAD_REQUEST)
