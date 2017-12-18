# rest/api/serializers.py
from rest_framework import serializers

<<<<<<< HEAD:rest/rest/api/serializers.py
from ..models import Posts

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Posts
        fields = ['id', 'text']
=======
class PostSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    text = serializers.CharField(max_length=10000)

    def create(self, validated_data):
        return Post.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.text = validated_data.get('text', instance.text)
        instance.save()
        return instance
# class PostSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ('text')


>>>>>>> a6c0765b6801b8caee53e5efc11f0f1b468bf419:serwis/rest/serializers.py
