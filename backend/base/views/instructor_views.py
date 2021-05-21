from django.shortcuts import render

from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated, IsAdminUser
from rest_framework.response import Response

from django.http import JsonResponse
from django.contrib.auth.models import User

from base.models import Instructor
from base.serializers import InstructorSerializer

from rest_framework import status




@api_view(['GET'])
def getInstructors(request):
   instructors = Instructor.objects.all()
   serializer = InstructorSerializer(instructors, many=True)
   return Response(serializer.data)


@api_view(['GET'])
def getInstructor(request, pk):
    instructor = Instructor.objects.get(_id=pk)
    serializer = InstructorSerializer(instructor, many=False)
    return Response(serializer.data)
    