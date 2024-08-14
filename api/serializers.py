from rest_framework.serializers import ModelSerializer
from main.models import Contact,ChooseItem, TeamMember, Partner, RoadmapItem


class ContactSerializer(ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class ChooseItemSerializer(ModelSerializer):
    class Meta:
        model = ChooseItem
        fields = '__all__'


class TeamMemberSerializer(ModelSerializer):
    class Meta:
        model = TeamMember
        fields = '__all__'


class PartnerSerializer(ModelSerializer):
    class Meta:
        model = Partner
        fields = '__all__'


class RoadmapItemSerializer(ModelSerializer):
    class Meta:
        model = RoadmapItem
        fields = '__all__'