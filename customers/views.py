import uuid
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from django.utils.text import slugify
from .serializers import CustomerSerializer
from .models import Customer


class CustomerViewSet(ModelViewSet):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer

    def create(self, request, *args, **kwargs):
        data = CustomerSerializer(data=request.data)
        if data.is_valid():
            data.save(
                id=uuid.uuid4(),
                slug=slugify(data.validated_data['name'])
            )
        return Response(
            status=status.HTTP_201_CREATED,
            data={
                "description": "Customer was created successfully"
            }
        )


