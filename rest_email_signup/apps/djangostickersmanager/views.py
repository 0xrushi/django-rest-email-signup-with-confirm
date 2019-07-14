from rest_framework.parsers import MultiPartParser, FormParser
from .serializers import StickerSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


class StickerUploadView(APIView):
    # MultiPartParser AND FormParser
    # https://www.django-rest-framework.org/api-guide/parsers/#multipartparser
    # "You will typically want to use both FormParser and MultiPartParser
    # together in order to fully support HTML form data."
    parser_classes = (FormParser,MultiPartParser)
    def post(self, request, *args, **kwargs):
        #print("hete"+request.data)
        file_serializer = StickerSerializer(data=request.data)
        if file_serializer.is_valid():
            file_serializer.save()
            return Response(file_serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(file_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
