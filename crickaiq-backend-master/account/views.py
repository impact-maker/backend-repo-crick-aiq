from rest_framework.response import Response
from django.contrib.auth import authenticate
from .models import *
from .serializers import *
from rest_framework import viewsets
from django_filters import rest_framework as filters
from rest_framework import filters as rest_framework_filters
from rest_framework.authentication import TokenAuthentication
from rest_framework.decorators import action
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny
from django.db.models import Q
from django.contrib.auth import login, logout
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt
from rest_framework.authtoken.models import Token

class UserFilter(filters.FilterSet):
    class Meta:
        model = User
        fields = {
            'username': ['icontains'],
            'name': ['icontains'],
            'email': ['icontains'],
            'mobile': ['icontains'],
            'role__role': ['exact', 'icontains'],
            'status': ['exact'],
        }

class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    authentication_classes = [TokenAuthentication]
    filterset_class = UserFilter
    filter_backends = [rest_framework_filters.SearchFilter,
                       filters.DjangoFilterBackend, rest_framework_filters.OrderingFilter]
    ordering_fields = ['created_on']
    ordering = ['-created_on']

    def update(self, request, pk=None):
        # request.data.pop("upload_signature")
        instance = User.objects.get(pk=pk)
        serializer = UserSerializer(
            instance=instance, data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=401)

    @action(detail=False, methods=["GET"])
    def my_profile(self, request):
        if request.method == "GET":
            # data = request.data
            serializer = UserSerializer(instance=request.user, context={"request": request})
            return Response(serializer.data, status=201)
        return Response(status=404)




class RoleFilter(filters.FilterSet):

    class Meta:
        model = Role
        fields = {
            'role': ['icontains'],
            'user_type': ['icontains'],
            'status': ['exact'],
        }


class RoleViewSet(viewsets.ModelViewSet):
    """
    A simple ViewSet for listing or retrieving Role.
    """
    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    authentication_classes = [TokenAuthentication]
    filterset_class = RoleFilter
    filter_backends = [rest_framework_filters.SearchFilter,
                       filters.DjangoFilterBackend, rest_framework_filters.OrderingFilter]
    ordering_fields = ['created_on']
    ordering = ['-created_on']

    def update(self, request, pk=None):
        instance = self.get_object()
        data = request.data
        
        serializer = RoleSerializer(instance=instance, data=request.data)
        if serializer.is_valid():
            instance = serializer.save()
            instance.save()
            return Response(serializer.data)
        return Response({'errors': serializer.errors}, status=401)
    
class LoginView(APIView):
    permission_classes = [AllowAny]
    authentication_classes = []

    def post(self, request):
        username = request.data['username']
        password = request.data['password']

        probable_user = User.objects.filter(username=username).exists()
        probable_user_details = User.objects.filter(username=username).first()
        
        if probable_user:
            user = authenticate(request, username=probable_user_details.username, password=password) 
            if user:
                login(request, user)
                token, created = Token.objects.get_or_create(user=user)
                serializer = UserSerializer(instance=user, context={"request": request})

                return Response(
                    {
                        "token": token.key,
                        "user": serializer.data,
                    },
                    status=200,
                )
            else:
                return Response({"msg": "Credentials are wrong"}, status=402)
        error_code = 404
        if error_code == 404:
            return Response({"msg": "User does not exist with this username"}, status=402)
        elif error_code == 400:
            return Response({"msg": "User must provide email and password"}, status=402)
        return Response({"msg": "Credentials are wrong"}, status=402)


class LogoutView(APIView):
    authentication_classes = (TokenAuthentication,)

    @method_decorator(csrf_exempt)
    def post(self, request):
        logout(request)
        return Response(status=204)
