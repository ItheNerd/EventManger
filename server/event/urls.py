from django.urls import path
from .views import UserEventsView, EventCreateView
from . import views

app_name = "event"

urlpatterns = [
    path("create/", EventCreateView.as_view(), name="event-create"),
    path("user-events/", UserEventsView.as_view(), name="user-events"),
    path("", views.EventListView.as_view(), name="event-list"),
    path("<int:pk>/", views.EventDetailView.as_view(), name="event-detail"),
]
