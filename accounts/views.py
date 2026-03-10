"""Views for the Accounts app."""
from rest_framework import status, generics
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken
from django.contrib.auth import authenticate, get_user_model

from .serializers import SyraUserSerializer, RegisterSerializer, LoginSerializer

User = get_user_model()


class RegisterView(generics.CreateAPIView):
    """API endpoint for user registration."""
    queryset = User.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.save()
        
        refresh = RefreshToken.for_user(user)
        
        return Response({
            'user': SyraUserSerializer(user).data,
            'refresh': str(refresh),
            'access': str(refresh.access_token),
            'message': 'User registered successfully.'
        }, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@permission_classes([AllowAny])
def login_view(request):
    """API endpoint for user login using National ID."""
    serializer = LoginSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    
    national_id = serializer.validated_data['national_id']
    password = serializer.validated_data['password']
    
    try:
        user = User.objects.get(national_id=national_id)
    except User.DoesNotExist:
        return Response(
            {'error': 'Invalid credentials.'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    user = authenticate(username=user.username, password=password)
    
    if user is None:
        return Response(
            {'error': 'Invalid credentials.'},
            status=status.HTTP_401_UNAUTHORIZED
        )
    
    refresh = RefreshToken.for_user(user)
    
    return Response({
        'user': SyraUserSerializer(user).data,
        'refresh': str(refresh),
        'access': str(refresh.access_token),
        'message': 'Login successful.'
    })


@api_view(['GET', 'PUT'])
@permission_classes([IsAuthenticated])
def profile_view(request):
    """API endpoint to get or update current user profile."""
    if request.method == 'GET':
        serializer = SyraUserSerializer(request.user)
        return Response(serializer.data)
    
    elif request.method == 'PUT':
        serializer = SyraUserSerializer(request.user, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
