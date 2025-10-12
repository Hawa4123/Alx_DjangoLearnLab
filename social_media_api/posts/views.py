from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from django.shortcuts import get_object_or_404

from .models import Post, Like
from notifications.models import Notification

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def like_post(request, pk):
    # Get the post or return 404
    post = get_object_or_404(Post, pk=pk)

    # Create a like if it doesn't exist
    like, created = Like.objects.get_or_create(user=request.user, post=post)
    if not created:
        return Response({"detail": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)
    
    # Create notification for the post author (skip if user likes their own post)
    if post.author != request.user:
        Notification.objects.create(
            recipient=post.author,
            actor=request.user,
            verb='liked your post',
            target=post
        )

    return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def unlike_post(request, pk):
    # Get the post or return 404
    post = get_object_or_404(Post, pk=pk)

    # Remove the like if it exists
    like = Like.objects.filter(user=request.user, post=post)
    if like.exists():
        like.delete()
        return Response({"detail": "Post unliked"}, status=status.HTTP_200_OK)
    
    return Response({"detail": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)
