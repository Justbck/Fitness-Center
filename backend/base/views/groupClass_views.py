from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.http import JsonResponse
from django.contrib.auth.models import User

from base.models import GroupClass
from base.serializers import GroupClassSerializer

from rest_framework import status


@api_view(['GET'])
def getGroupClasses(request):
   instructors = GroupClass.objects.all()
   serializer = GroupClassSerializer(instructors, many=True)
   return Response(serializer.data)


@api_view(['GET'])
def getGroupClass(request, pk):
    instructor = GroupClass.objects.get(_id=pk)
    serializer = GroupClassSerializer(instructor, many=False)
    return Response(serializer.data)
    