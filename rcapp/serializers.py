from rest_framework import serializers
from rcapp.models import Recordings
from rcapp.models import User

class UserSerializer(serializers.HyperlinkedModelSerializer):
    def create(self, validated_data):
        recordings = serializers.HyperlinkedRelatedField(
            many=True,
            read_only=True,
            view_name='recording-detail'
        )
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)
        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance

class RecordingSerializer(serializers.ModelSerializer):
    owner = serializers.SlugRelatedField(queryset=User.objects.all(),slug_field='name')
    class Meta:
        model = Recordings
        fields = ('url', 'owner', 'created', 'datafile', 'result')
