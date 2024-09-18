import random
from customers.models import Customer
from celery import shared_task
from ..serializers import TrackerSerializer


def generate_tacker_number(origin, dest, customer: Customer):
    length = 16
    tracker_number = f"{origin}{dest}{random.randint(1, 9999999)}{str(customer.id)[0:5]}"
    assert len(tracker_number) == length
    return tracker_number


@shared_task
def generate_tracker(data):
    _data = TrackerSerializer(data=data)
    if _data.is_valid():
        try:
            saved = _data.save(
                tracking_number=generate_tacker_number(
                    _data.validated_data['origin_country_id'],
                    _data.validated_data['destination_country_id'],
                    _data.validated_data['customer']
                )
            )
            return saved.tracking_number, saved.created_at.isoformat()
        except AssertionError:
            return
    return


