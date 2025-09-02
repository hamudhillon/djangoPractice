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
            
