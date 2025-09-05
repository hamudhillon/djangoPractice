# from rest_framework import viewsets
# from .models import *
# from .serializers import StudentSerializer


# class StudentViewSet(viewsets.ModelViewSet):
#     queryset=Student.objects.all()
#     serializer_class=StudentSerializer


from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status,filters,generics
from django_filters.rest_framework import DjangoFilterBackend
from .models import *
from .serializers import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated


def get_tokens_for_user(user):
    refresh=RefreshToken.for_user(user)
    return {
        'refresh':str(refresh),
        'access':str(refresh.access_token)
    }


class LoginView(APIView):
    def post(self,request):
        username=request.data.get('username')
        password=request.data.get('password')

        user=authenticate(username=username,password=password)
        if user is not None:
            tokens=get_tokens_for_user(user)
            return Response({"message":"Login Successful","tokens":tokens},status=status.HTTP_200_OK)
        else:
            return Response({"error":"Invalid creds"},status=status.HTTP_404_NOT_FOUND)

class SignupView(APIView):
    def post(self,request):
        username=request.data.get('username')
        email=request.data.get('email')
        password=request.data.get('password')

        if User.objects.filter(username=username).exists():
            return Response({"error":"Username Already Exists"},status=status.HTTP_400_BAD_REQUEST)

        user=User.objects.create_user(username=username,email=email,password=password)
        user.save()
        tokens=get_tokens_for_user(user)
        return Response({"message":"User created","tokens":tokens},status=status.HTTP_201_CREATED)



class StudentListCreate(generics.GenericAPIView):
    permission_classes=[IsAuthenticated]

    queryset=Student.objects.all()
    serializer_class=StudentSerializer


    filter_backends=[DjangoFilterBackend,filters.SearchFilter,filters.OrderingFilter]
    filterset_fields={
        'age':['exact','gte','lte'],
        'name':['exact','icontains'],
        'phone':['exact']
    }
    search_fields=['age','name','phone','email']
    ordering_fields=['age','name']
    

# class StudentListCreate(APIView):

    def get(self,request):
        queryset=self.filter_queryset(self.get_queryset())
        serializers=StudentSerializer(queryset,many=True)
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