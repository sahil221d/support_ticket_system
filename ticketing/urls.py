from django.urls import path
from .views import UserCreateView, SupportPersonCreateView, TicketDetailsView, TicketCreateView, TicketListView, TicketUpdateView

urlpatterns = [
    path('add-user/', UserCreateView.as_view(), name='add-user'),
    path('add-support-person/', SupportPersonCreateView.as_view(), name='add-support-person'),
    path('raise-ticket/', TicketCreateView.as_view(), name='raise-ticket'),
    path('tickets/', TicketListView.as_view(), name='ticket-list'),
    path('tickets/<int:pk>/', TicketDetailsView.as_view(), name='ticket-details'),
    path('tickets/<int:pk>/update/', TicketUpdateView.as_view(), name='ticket-update'),

]