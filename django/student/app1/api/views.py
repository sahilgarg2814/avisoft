from app1.models import movies_model
from app1.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status

# def movie_list(request):
#     movies=movies_model.objects.all()
#     data={
#         'movies':list(movies.values())   # movies.values values of objects in the variable movies
#     }
#     return JsonResponse(data)  # returning data in the form of json response
# def movie_detail(request,id):
#     movie=movies_model.objects.get(movie_name=id)
#     data={
#         'name':movie.movie_name,
#         'description':movie.movie_description,
#         'active':movie.movie_active
#     }
#     return JsonResponse(data)

# @api_view(['GET','POST'])
# def movie_list(request):
#     if request.method=='GET':
#         movie=movies_model.objects.all()
#         serial=MovieSerializer(movie,many=True)
#         return Response(serial.data)
    
#     if request.method=='POST':
#         serial=MovieSerializer(data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data)
#         else:
#             return Response(serial.errors)
        

# @api_view(['GET','PUT','DELETE'])
# def movie_detail(request,id):
    
#     if request.method=='GET':
#         try:
#             movie=movies_model.objects.get(movie_name=id)
#         except movies_model.DoesNotExist:
#             return Response({'ERROR':'MOVIE not found'},status=status.HTTP_404_NOT_FOUND)
#         serial=MovieSerializer(movie)
#         return Response(serial.data)
    
#     if request.method=='PUT':
#         movie=movies_model.objects.get(movie_name=id)
#         serial=MovieSerializer(movie,data=request.data)
#         if serial.is_valid():
#             serial.save()
#             return Response(serial.data)
#         else:
#             return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)


#     if request.method=='DELETE':
#         movie=movies_model.objects.get(movie_name=id)
#         movie.delete()
#         return Response(status=204)


# class based views
class movie_list_av(APIView):
    def get(self,request):
        movie=movies_model.objects.all()
        serial=MovieSerializer(movie,many=True)
        return Response(serial.data)
    
    def post(self,request):
        serial=MovieSerializer(data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors)

class movie_detail_av(APIView):
    def get(self,request,id):
        try:
            movie=movies_model.objects.get(movie_name=id)
        except movies_model.DoesNotExist:
            return Response({'ERROR':'MOVIE not found'},status=status.HTTP_404_NOT_FOUND)
        serial=MovieSerializer(movie)
        return Response(serial.data)
    
    def put(self,request,id):
        movie=movies_model.objects.get(movie_name=id)
        serial=MovieSerializer(movie,data=request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data)
        else:
            return Response(serial.errors,status=status.HTTP_400_BAD_REQUEST)
        
    def delete(self,request,id):
        movie=movies_model.objects.get(movie_name=id)
        movie.delete()
        return Response(status=204) 
