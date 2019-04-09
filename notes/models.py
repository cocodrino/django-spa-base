from django.db import models

from rest_framework import serializers

from django.contrib.auth.models import User


class Note(models.Model):
    text = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, related_name="notes", on_delete=models.CASCADE, null=True)

    def __str__(self):
        return self.text


class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ("id", "text", "created_at")
