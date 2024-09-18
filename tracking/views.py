import random
from rest_framework.viewsets import ModelViewSet
from rest_framework import status
from rest_framework.response import Response
from .serializers import TrackerSerializer
from .models import Tracker
from customers.models import Customer
from .tasks import generate_tracker


def generate_tacker_number(origin, dest, customer: Customer):
    length = 16
    tracker_number = f"{origin}{dest}{random.randint(1, 9999999)}{str(customer.id)[0:5]}"
    assert len(tracker_number) == length
    return tracker_number


class TrackerViewSet(ModelViewSet):
    serializer_class = TrackerSerializer

    def get_queryset(self):
        queryset = Tracker.objects.all()

        origin_country_id = self.request.query_params.get('origin_country_id')
        destination_country_id = self.request.query_params.get('destination_country_id')
        weight = self.request.query_params.get('weight')
        created_at = self.request.query_params.get('created_at')
        customer_id = self.request.query_params.get('customer_id')
        customer_name = self.request.query_params.get('customer_name')
        customer_slug = self.request.query_params.get('customer_slug')

        if origin_country_id is not None:
            queryset = queryset.filter(origin_country_id=origin_country_id)
        
        if destination_country_id is not None:
            queryset = queryset.filter(destination_country_id=destination_country_id)
        
        if weight is not None:
            queryset = queryset.filter(weight=weight)
        
        if created_at is not None:
            queryset = queryset.filter(created_at=created_at)
        
        if customer_id is not None:
            queryset = queryset.filter(customer__id=customer_id)
        
        if customer_name is not None:
            queryset = queryset.filter(customer__name=customer_name)
        
        if customer_slug is not None:
            queryset = queryset.filter(customer__slug=customer_slug)
        return queryset

    def create(self, request, *args, **kwargs):
        tracking_number, created_at = generate_tracker.apply_async(
            [request.data]
        ).get()
        
        if tracking_number is not None and created_at is not None:
            return Response(
                status=status.HTTP_201_CREATED,
                data={
                    "tracking_number": tracking_number, 
                    "created_at": created_at
                }
            )
        else:
            return Response(
                status=status.HTTP_400_BAD_REQUEST,
                data={"message": "Error generating tracking number"}
            )



