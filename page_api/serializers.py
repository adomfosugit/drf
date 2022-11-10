# build serializers
# basically converts data from database
#into readable formats for the front end ....JSON
from rest_framework import serializers
from page.models import Post

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post 
        fields = ('id', 'title', 'author',  'excerpt', 'content', 'status')