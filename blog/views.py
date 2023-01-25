from rest_framework.response import Response
from rest_framework.decorators import api_view
from .utils import getPostDetails, getPostList

# Create your views here.
@api_view(['GET'])
def getPosts(request):
    return Response(getPostList(request))

@api_view(['GET'])
def getPost(request, pk):
    return Response(getPostDetails(request, pk))