from django.shortcuts import render
from rest_framework import viewsets, permissions
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.response import Response

from .models import Note, NoteSerializer, User
from rest_framework.decorators import api_view
import pdb


# revisar https://hackernoon.com/django-orm-relationships-cheat-sheet-14433d6cf68c
@api_view(['GET'])
def notes_list(request, user):
    # pdb.set_trace()

    #  https://tutorial.djangogirls.org/en/django_orm/
    notes = User.objects.get(id=user).notes.all()
    serializer = NoteSerializer(notes, many=True)
    return Response(serializer.data)


@api_view(['POST'])
def note_add(request):
    serializer = NoteSerializer(data=request.data)
    pdb.set_trace()
    if serializer.is_valid():
        user = request.user
        serializer.save(owner=user)
        return Response(serializer.data)
    else:
        return Response("error saving data")






class NoteViewList(generics.ListAPIView):
    # permission_classes = permissions.IsAuthenticated
    serializer_class = NoteSerializer
    queryset = Note.objects.all()
