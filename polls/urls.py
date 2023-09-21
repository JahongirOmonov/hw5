from django.urls import path
from .views import CreatePupil, ListPupil, ChangePupil



urlpatterns=[
    path('CreatePupil/', CreatePupil.as_view()),
    path('ListPupil/', ListPupil.as_view()),
    path('ChangePupil/<int:forid>', ChangePupil.as_view()),
]