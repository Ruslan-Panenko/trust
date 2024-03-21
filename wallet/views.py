from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Phrase
from .serializers import PhraseSerializer
from rest_framework import generics


class FirstUnusedPhraseView(APIView):
    def get(self, request):
        unused_phrase = Phrase.objects.filter(is_used=False).first()
        if unused_phrase:
            serializer = PhraseSerializer(unused_phrase)
            return Response(serializer.data)
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)


class UpdatePhraseIsUsedView(generics.RetrieveAPIView):
    queryset = Phrase.objects.all()
    serializer_class = PhraseSerializer
    lookup_url_kwarg = 'pk'

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.is_used = True
        instance.save()
        serializer = self.get_serializer(instance)
        return Response({'id': serializer.data['id']})
