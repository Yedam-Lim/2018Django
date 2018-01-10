from rest_framework import generics
from rcapp.models import Recordings
from rcapp.models import User
from . import serializers

class UserList(generics.ListCreateAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    name = 'user-list'

class UserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    name = 'user-detail'

class RecordingList(generics.ListCreateAPIView):
    queryset = Recordings.objects.all()
    serializer_class = serializers.RecordingSerializer
    name = 'recording-list'

class RecordingDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Recordings.objects.all()
    serializer_class = serializers.RecordingSerializer
    name = 'recording-detail'
