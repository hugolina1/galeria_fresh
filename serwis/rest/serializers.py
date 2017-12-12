
from rest_framework import serializers
from .models import Post

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


