from rest_framework import serializers
from .models import TeamMember

class MemberSerialiser(serializers.ModelSerializer):

    class Meta:
        model = TeamMember
        # fields = ('user','FirstName','LastName','ProfilePicture','Authorised','BirthDate','Mail','created_date')
        fields = '__all__'