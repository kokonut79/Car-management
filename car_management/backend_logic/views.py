from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Car, Garage
from .serializers import CarSerializer, CarCreateUpdateSerializer

@api_view(["GET"])
def read_cars(request):
    cars = Car.objects.prefetch_related("garages").all()
    serializer = CarSerializer(cars, many=True)
    return Response(serializer.data)

@api_view(["POST"])
def create_car(request):
    serializer = CarCreateUpdateSerializer(data=request.data)
    if serializer.is_valid():
        car = serializer.save()
        return Response(CarSerializer(car).data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(["DELETE"])
def delete_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
        car.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except Car.DoesNotExist:
        return Response({"detail": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

@api_view(["PUT"])
def update_car(request, car_id):
    try:
        car = Car.objects.get(id=car_id)
    except Car.DoesNotExist:
        return Response({"detail": "Car not found"}, status=status.HTTP_404_NOT_FOUND)

    serializer = CarCreateUpdateSerializer(car, data=request.data, partial=True)
    if serializer.is_valid():
        car = serializer.save()
        return Response(CarSerializer(car).data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
