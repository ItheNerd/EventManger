from django.views.generic import ListView, DetailView
from .models import Event
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .serializers import EventSerializer
from rest_framework.parsers import MultiPartParser, FormParser


class EventListView(ListView):
    model = Event
    template_name = "event_list.html"
    context_object_name = "events"


class EventDetailView(DetailView):
    model = Event
    template_name = "event_detail.html"
    context_object_name = "event"


class EventCreateView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def post(self, request):
        serializer = EventSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(user_id=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class UserEventsView(APIView):
    def get(self, request):
        user_events = Event.objects.filter(user_id=request.user)
        serializer = EventSerializer(user_events, many=True)
        return Response(serializer.data)
