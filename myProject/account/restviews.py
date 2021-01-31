from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from rest_framework import permissions
from rest_framework.response import Response

from .serializers import UserSerializer, GroupSerializer, User1Serializer
from rest_framework import status
import json
from django.core.exceptions import ObjectDoesNotExist

class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = UserSerializer
    #permission_classes = [permissions.IsAuthenticated]


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer
    #permission_classes = [permissions.IsAuthenticated]



from rest_framework.decorators import api_view, permission_classes
#from rest_framework.permissions import IsAuthenticated
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def welcome(request):
    content = {"msg": "welcome to webservice"}
    return JsonResponse(content)


"""
web service to create the user:
-----------------------------

URL:<BASE_URL>/rest1/adduser
HTTP METHOD: post
request json:
   {
            "username": "krishna12",
            "password": "krishna12",
            "email": "krishna@y.com",
            "firstName": "krishna",
            "lastName": "krishna"
   }

"""
@api_view(["GET"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def get_users(request):
    users = User.objects.all()
    serializer = UserSerializer(users, many=True, context={
            'request': request,
        })
    return JsonResponse({'users': serializer.data}, safe=False, status=status.HTTP_200_OK)

@api_view(["POST"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def add_user(request):
    payload = json.loads(request.body)
    """
     How to get the data from json:

     userName = payload["username"]
     pwd = payload["password"]
     email = payload["email"]
     fN= payload["firstName"]
     ln = payload["lastName"]

     """
    try:
        user  = User.objects.create_user(
                    username=payload["username"] , password=payload["password"],email=payload["email"], first_name= payload["firstName"] , last_name=payload["lastName"])
        serializer = UserSerializer(user,context={
            'request': request,
        })
        return JsonResponse({'books': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        print("issue",ex)
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["DELETE"])
@csrf_exempt
def delete_user(request, userName):
    try:
        eObj = User.objects.get(username=userName)
        eObj.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["PUT"])
@csrf_exempt
#@permission_classes([IsAuthenticated])
def update_user(request, userName):
    payload = json.loads(request.body)
    print(payload)
    try:
        eObj = User.objects.get(username=userName)
        # returns 1 or 0
        eObj.set_password(payload['password'])
        eObj.email =payload['email']
        eObj.first_name = payload['firstName']
        eObj.last_name = payload['lastName']

        eObj.save()
        serializer = UserSerializer(eObj, context={
            'request': request,
        })
        return JsonResponse({'response': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        print(ex)
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


@api_view(["GET"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def get_User(request, userName):
    try:
        eObj = User.objects.get(username=userName)
        serializer = UserSerializer(eObj, context={
            'request': request,
        })
        return JsonResponse({'response': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': 'Invalid username :' + userName}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception as ex:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False,
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)


