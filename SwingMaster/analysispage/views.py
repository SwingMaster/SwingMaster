from django.core.files.storage import default_storage
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import datetime

def index(request):
    return render(request, 'camera_base.html')


@api_view(['POST'])
def file_upload(request):
    if request.method == "POST":
        now = datetime.datetime.now()
        for i in range(150):
            file = request.FILES['image' + str(i)]
            default_storage.save(str(now.year) + str(now.month) + str(now.day) + str(now.hour) + str(
                now.minute) + "outputs" + '/' + file.name, file)

        return Response('success', status=status.HTTP_200_OK)
    return redirect("../camera")