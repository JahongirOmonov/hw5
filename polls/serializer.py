from rest_framework.serializers import ModelSerializer


from .models import PupilModel

class PupilSerializer(ModelSerializer):
    class Meta:
        model = PupilModel
        fields=('__all__')