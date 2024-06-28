from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import viewsets
from .models import Post
from .serializers import PostSerializer

class PostList(APIView):
    def get(self, request):
        posts = Post.objects.all()
        return Response([{'id': post.id, 'title': post.title, 'content': post.content, 'author': post.author} for post in posts])

    def post(self, request):
        post = Post(title=request.data['title'], content=request.data['content'], author=request.data['author'])
        post.save()
        return Response({'id': post.id, 'title': post.title, 'content': post.content, 'author': post.author})

class PostDetail(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        return Response({'id': post.id, 'title': post.title, 'content': post.content, 'author': post.author})

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer