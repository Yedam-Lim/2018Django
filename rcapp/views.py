from rest_framework import generics
from rest_framework import mixins
from rcapp.models import Recordings
from rcapp.models import User
from rest_framework import Response
from . import serializers

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    name = 'user-detail'

class RecordingList(mixins.ListModelMixin,
                    mixins.CreateModelMixin,
                    generics.GenericAPIView):

    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        response = self.create(request, *args, **kwargs)

        return

    queryset = Recordings.objects.all()
    serializer_class = serializers.RecordingSerializer
    name = 'recording-list'

class RecordingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recordings.objects.all()
    serializer_class = serializers.RecordingSerializer
    name = 'recording-detail'

class ApiRoot(generics.GenericAPIView):
    name = 'api-root'
    def get(self, request, *args, **kwargs):
        return Response({
            'users': reverse(UserList.name, request=request),
            'recordings': reverse(RecordingList.name, request=request),
        })
