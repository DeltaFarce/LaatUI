from .models import Meminfo
from rest_framework.serializers import ModelSerializer


class MenifoModelSerializer(ModelSerializer):
    class Meta:
        model = Meminfo
        fields = '__all__'
