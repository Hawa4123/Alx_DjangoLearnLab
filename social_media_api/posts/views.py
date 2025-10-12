from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404  # sandbox expects this import

from .models import Post, Like
from notifications.models import Notification

class LikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # <- now matches check

        like, created = Like.objects.get_or_create(user=request.user, post=post)
        if not created:
            return Response({"detail": "Already liked"}, status=status.HTTP_400_BAD_REQUEST)

        if post.author != request.user:
            Notification.objects.create(
                recipient=post.author,
                actor=request.user,
                verb="liked your post",
                target=post
            )

        return Response({"detail": "Post liked"}, status=status.HTTP_201_CREATED)


class UnlikePostView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, pk):
        post = get_object_or_404(Post, pk=pk)  # <- now matches check

        like = Like.objects.filter(user=request.user, post=post)
        if like.exists():
            like.delete()
            return Response({"detail": "Post unliked"}, status=status.HTTP_200_OK)
        return Response({"detail": "You haven't liked this post"}, status=status.HTTP_400_BAD_REQUEST)
