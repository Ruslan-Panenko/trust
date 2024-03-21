from django.urls import path
from .views import FirstUnusedPhraseView, UpdatePhraseIsUsedView

urlpatterns = [
    path('phrase/', FirstUnusedPhraseView.as_view()),
    path('phrase/<int:pk>', UpdatePhraseIsUsedView.as_view()),
]
