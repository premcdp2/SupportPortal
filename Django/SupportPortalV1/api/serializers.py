from .models import Activity
from rest_framework import serializers



class ActivitySerializers(serializers.ModelSerializer):

    class Meta:
        model = Activity
        fields = '__all__'

