from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .services import get_garages, create_garage, delete_garage, update_garage

class GarageListView(APIView):
    """Handle GET and POST requests for garages."""

    def get(self, request):
        """Retrieve all garages."""
        garages = get_garages()
        return Response(garages, status=status.HTTP_200_OK)

    def post(self, request):
        """Create a new garage."""
        garage_data = request.data
        result = create_garage(garage_data)
        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        return Response(result, status=status.HTTP_201_CREATED)


class GarageDetailView(APIView):
    """Handle GET, PUT, and DELETE requests for a specific garage."""

    def put(self, request, garage_id):
        """Update a specific garage."""
        garage_data = request.data
        result = update_garage(garage_id, garage_data)
        if "error" in result:
            return Response(result, status=status.HTTP_400_BAD_REQUEST)
        return Response(result, status=status.HTTP_200_OK)

    def delete(self, request, garage_id):
        """Delete a specific garage."""
        result = delete_garage(garage_id)
        if "error" in result:
            return Response(result, status=status.HTTP_404_NOT_FOUND)
        return Response(result, status=status.HTTP_204_NO_CONTENT)
