from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
import json


class CoachesPageView(TemplateView):
    template_name = "Coaches.html"


def index(request):
    return render(request, 'index.html')


@api_view(["POST"])
def login(req):
    try:
        login_details = json.loads(req.body)
        username = login_details.get('username')
        password = login_details.get('password')
        if(username=='admin' and password=='12345'):
            return Response(status.HTTP_200_OK)
        else:
            return Response(status.HTTP_400_BAD_REQUEST)
            #return JsonResponse('Incorrect User name or Password ', safe=False)
    except ValueError as e:
        return Response(e.args[0], status.HTTP_400_BAD_REQUEST)