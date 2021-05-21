from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.http import JsonResponse
from django.contrib.auth.models import User

from base.models import PersonalClass
from base.serializers import PersonalClassSerializer

from rest_framework import status


@api_view(['GET'])
def getPersonalClasses(request):
   instructors = PersonalClass.objects.all()
   serializer = PersonalClassSerializer(instructors, many=True)
   return Response(serializer.data)


@api_view(['GET'])
def getPersonalClass(request, pk):
    instructor = PersonalClass.objects.get(_id=pk)
    serializer = PersonalClassSerializer(instructor, many=False)
    return Response(serializer.data)
    