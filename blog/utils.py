from rest_framework.response import Response
from .serializers import PostSerializer
from .models import Post

def getPostDetails(request, pk):
    posts = Post.objects.get(id=pk)
    serializer = PostSerializer(posts, many=False)

    return serializer.data

def getPostList(request):
    posts = Post.objects.all().order_by('-date_created')
    serializer = PostSerializer(posts, many=True)

    return serializer.data
