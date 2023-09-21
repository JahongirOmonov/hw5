from django.shortcuts import render
from rest_framework.views import APIView
from .serializer import PupilSerializer
from rest_framework.response import Response
from .models import PupilModel
from django.shortcuts import get_object_or_404


# Create your views here.

class CreatePupil(APIView):
    def post(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            if request.user.roles == 2:
                serialzier = PupilSerializer(data=request.data)
                if serialzier.is_valid():
                    serialzier.save()
                    return Response(serialzier.data)
                return Response(serialzier.errors)
        return Response({"msg":"only controller members can add"})
    

class ListPupil(APIView):
    def get(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            print(self.request.user.roles)
            x = PupilModel.objects.filter(status=True)
            serializer=PupilSerializer(x, many=True)
            return Response(serializer.data)
        return Response({'msg':'Go away'})
    
class ChangePupil(APIView):
    def patch(self, request, *args, **kwargs):
        if str(request.user) != "AnonymousUser":
            if request.user.roles == 3:
                x= get_object_or_404(PupilModel, id=kwargs['forid'])
                serializer=PupilSerializer(x, data=request.data, partial=True)
                if serializer.is_valid():
                    serializer.save()
                    return Response(serializer.data)
                return Response(serializer.errors)
        return Response("Only admin can change")