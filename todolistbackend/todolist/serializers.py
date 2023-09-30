
from rest_framework import serializers

from todolist.models import TodoItem

class TodoItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = TodoItem
        fields = '__all__'
        read_only_fields = ('author' ,)
    
        # def update(self, instance, validated_data):
        #     instance.title = validated_data.get('title', instance.title)
        #     instance.save()
        #     return instance