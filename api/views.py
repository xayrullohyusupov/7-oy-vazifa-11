from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .serializers import ContactSerializer,ChooseItemSerializer,TeamMemberSerializer,PartnerSerializer,RoadmapItemSerializer
from main.models import Contact,ChooseItem, TeamMember, Partner, RoadmapItem, ContactMessage
#---------------------------------------------------------------- 1
@api_view(['GET'])
def contact_list(request):
    if request.method == 'GET':
        contacts = Contact.objects.all()
        serializer = ContactSerializer(contacts, many=True)
        return Response(serializer.data)

@api_view(['POST'])    
def contact_detail(request,id):
    contacts = Contact.objects.get(id=id)
    serializer = ContactSerializer(contacts).data
    return Response(serializer)

@api_view(['POST'])
def contact_create(request):
    seria_lizer = ContactSerializer(data=request.data)
    if seria_lizer.is_valid():
        seria_lizer.save()
        return Response(seria_lizer.data, status=status.HTTP_201_CREATED)
    return Response(seria_lizer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def contact_update(request, id):
    try:
        contacts = Contact.objects.get(id=id)
    except Contact.DoesNotExist:
        return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ContactSerializer(contacts, data=request.data)
    
    if serializer.is_valid():
        serializer.save()
        return Response({'status': 'Contact updated successfully'}, status=status.HTTP_200_OK)
    
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def contact_delete(request, id):
    try:
        contacts = Contact.objects.get(id=id)
    except Contact.DoesNotExist:
        return Response({'error': 'Contact not found'}, status=status.HTTP_404_NOT_FOUND)
    
    contacts.delete()
    return Response({'status': 'Contact deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

#---------------------------------------------------------------- 2
@api_view(['GET'])
def chooseitem_list(request):
    items = ChooseItem.objects.all()
    serializer = ChooseItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def chooseitem_detail(request, id):
    try:
        item = ChooseItem.objects.get(id=id)
    except ChooseItem.DoesNotExist:
        return Response({'error': 'ChooseItem not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = ChooseItemSerializer(item)
    return Response(serializer.data)

@api_view(['POST'])
def chooseitem_create(request):
    serializer = ChooseItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def chooseitem_update(request, id):
    try:
        item = ChooseItem.objects.get(id=id)
    except ChooseItem.DoesNotExist:
        return Response({'error': 'ChooseItem not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = ChooseItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def chooseitem_delete(request, id):
    try:
        item = ChooseItem.objects.get(id=id)
    except ChooseItem.DoesNotExist:
        return Response({'error': 'ChooseItem not found'}, status=status.HTTP_404_NOT_FOUND)
    
    item.delete()
    return Response({'status': 'ChooseItem deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------- 3
@api_view(['GET'])
def teammember_list(request):
    members = TeamMember.objects.all()
    serializer = TeamMemberSerializer(members, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def teammember_detail(request, id):
    try:
        member = TeamMember.objects.get(id=id)
    except TeamMember.DoesNotExist:
        return Response({'error': 'TeamMember not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = TeamMemberSerializer(member)
    return Response(serializer.data)

@api_view(['POST'])
def teammember_create(request):
    serializer = TeamMemberSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def teammember_update(request, id):
    try:
        member = TeamMember.objects.get(id=id)
    except TeamMember.DoesNotExist:
        return Response({'error': 'TeamMember not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = TeamMemberSerializer(member, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def teammember_delete(request, id):
    try:
        member = TeamMember.objects.get(id=id)
    except TeamMember.DoesNotExist:
        return Response({'error': 'TeamMember not found'}, status=status.HTTP_404_NOT_FOUND)
    
    member.delete()
    return Response({'status': 'TeamMember deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------- 4
@api_view(['GET'])
def partner_list(request):
    partners = Partner.objects.all()
    serializer = PartnerSerializer(partners, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def partner_detail(request, id):
    try:
        partner = Partner.objects.get(id=id)
    except Partner.DoesNotExist:
        return Response({'error': 'Partner not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = PartnerSerializer(partner)
    return Response(serializer.data)

@api_view(['POST'])
def partner_create(request):
    serializer = PartnerSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def partner_update(request, id):
    try:
        partner = Partner.objects.get(id=id)
    except Partner.DoesNotExist:
        return Response({'error': 'Partner not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = PartnerSerializer(partner, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def partner_delete(request, id):
    try:
        partner = Partner.objects.get(id=id)
    except Partner.DoesNotExist:
        return Response({'error': 'Partner not found'}, status=status.HTTP_404_NOT_FOUND)
    
    partner.delete()
    return Response({'status': 'Partner deleted successfully'}, status=status.HTTP_204_NO_CONTENT)

# ---------------------------------------------------------------- 5
@api_view(['GET'])
def roadmapitem_list(request):
    items = RoadmapItem.objects.all()
    serializer = RoadmapItemSerializer(items, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def roadmapitem_detail(request, id):
    try:
        item = RoadmapItem.objects.get(id=id)
    except RoadmapItem.DoesNotExist:
        return Response({'error': 'RoadmapItem not found'}, status=status.HTTP_404_NOT_FOUND)
    serializer = RoadmapItemSerializer(item)
    return Response(serializer.data)

@api_view(['POST'])
def roadmapitem_create(request):
    serializer = RoadmapItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['PUT'])
def roadmapitem_update(request, id):
    try:
        item = RoadmapItem.objects.get(id=id)
    except RoadmapItem.DoesNotExist:
        return Response({'error': 'RoadmapItem not found'}, status=status.HTTP_404_NOT_FOUND)
    
    serializer = RoadmapItemSerializer(item, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
def roadmapitem_delete(request, id):
    try:
        item = RoadmapItem.objects.get(id=id)
    except RoadmapItem.DoesNotExist:
        return Response({'error': 'RoadmapItem not found'}, status=status.HTTP_404_NOT_FOUND)
    
    item.delete()
    return Response({'status': 'RoadmapItem deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
