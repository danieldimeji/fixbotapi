from django.shortcuts import render
from django.http import  HttpResponse
from django.views import View
from rest_framework.views import APIView 
from rest_framework.response import Response
from rest_framework import status

from .models import TelemetricData
from .serializers import TelemetricDataSerializer

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer


def send_socket_msg():
    telemetric_qs = TelemetricData.objects.all()
    telemetric_data = TelemetricDataSerializer(telemetric_qs, many=True)
    layer = get_channel_layer()
    async_to_sync(layer.group_send)('api', {
            'type': 'payload',
            'payload': telemetric_data.data,
        })


class TelemetricDataListAPIView(APIView):
    
    def get(self, request):

        telemetric_data = TelemetricData.objects.all()
        serializers = TelemetricDataSerializer(telemetric_data, many=True)
        
        send_socket_msg()

        return Response(serializers.data)

    def post(self, request):

        serializers = TelemetricDataSerializer(data=request.data)

        if serializers.is_valid():
            serializers.save()

            send_socket_msg()

            return Response(serializers.data, status=status.HTTP_201_CREATED)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


class TelemetricDataDetailsAPIView(APIView):

    def get_object(self,id):
        try:
            return TelemetricData.objects.get(id=id)

        except TelemetricData.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)
    
    def get(self, request, id):

        telemetric_data = self.get_object(id)
        serializers = TelemetricDataSerializer(telemetric_data)

        return Response(serializers.data)

    def put(self, request, id):

        article = self.get_object(id)
        serializers = TelemetricDataSerializer(article,data=request.data)

        if serializers.is_valid():
            serializers.save()

            send_socket_msg()

            return Response(serializers.data)

        return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):

        article = self.get_object(id)
        article.delete()

        send_socket_msg()
        
        return Response(status=status.HTTP_204_NO_CONTENT)

class FrontendView(View):

    template_name = 'index.html'

    def get(self, request, *args, **kwargs):
        return render(request, self.template_name, {})
