from rest_framework import generics, status
from rest_framework.response import Response
from .models import User, SupportPerson, Ticket
from .serializers import UserSerializer, SupportPersonSerializer, TicketSerializer

class SupportPersonCreateView(generics.CreateAPIView):
    queryset = SupportPerson.objects.all()
    serializer_class = SupportPersonSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "Support person created"}, status=status.HTTP_201_CREATED)
        
class UserCreateView(generics.CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer 
    
    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "User created"}, status=status.HTTP_201_CREATED)

class TicketCreateView(generics.CreateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def create(self, request, *args, **kwargs):
        response = super().create(request, *args, **kwargs)
        return Response({"message": "Ticket created"}, status=status.HTTP_201_CREATED)
    
class TicketUpdateView(generics.UpdateAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Ticket updated with solution"}, status=status.HTTP_200_OK)

class TicketListView(generics.ListAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer

class TicketDetailsView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Ticket.objects.all()
    serializer_class = TicketSerializer