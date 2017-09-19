from django.shortcuts import render
from django.http import Http404
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Movie
from .serializers import MovieSerializer
from rest_framework import status


class MovieView(APIView):
    def get_object(self, id):
        try:
            return Movie.objects.get(id=id)
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, context={"request": request})
        return Response(serializer.data)

    def put(self, request, id, format=None):
        movie = self.get_object(id)
        serializer = MovieSerializer(movie, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


    def delete(self, request, id, format=None):
        movie = self.get_object(id)
        movie.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class MoviesView(APIView):
    def get_object(self):
        try:
            return Movie.objects.all()
        except Movie.DoesNotExist:
            raise Http404

    def get(self, request, format=None):
        movies = self.get_object()
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data)


    def post(self, request, format=None):
        serializer = MovieSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)