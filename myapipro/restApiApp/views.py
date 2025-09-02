# from rest_framework import viewsets
# from .models import *
# from .serializers import StudentSerializer


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import *
from .serializers import *

class StudentListCreate(APIView):

    def get(self,request):
        students=Student.objects.all()
        serializers=StudentSerializer(students,many=True)
        return Response(serializers.data)
    
    def post(self,request):
        serializer=StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)
            

class StudentDetail(APIView):

    def get_object(self,pk):
        try:
            
            return Student.objects.get(pk=pk) 

        except:
            return None
    
    def get(self,request,pk):
        student=self.get_object(pk)
        if not student:
            return Response({"error":"Student Not found"},status=status.HTTP_404_NOT_FOUND)
        
        serializer=StudentSerializer(student)
        return Response(serializer.data)

    def put(self,request,pk):
        student=self.get_object(pk)
        if not student:
            return Response({"error":"Student Not found"},status=status.HTTP_404_NOT_FOUND)

        serializer=StudentSerializer(student,data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        
        return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

    def delete(self,request,pk):
        student=self.get_object(pk)
        if not student:
            return Response({"error":"Student Not found"},status=status.HTTP_404_NOT_FOUND)

        student.delete()
        return Response({"message":"Student Deleted successfully"},status=status.HTTP_204_NO_CONTENT)