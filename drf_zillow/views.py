"""
    views
    ~~~~~

    Common DRF views for interacting with Zillow
"""

from rest_framework.generics import GenericAPIView
from rest_framework.parsers import JSONParser
from rest_framework.renderers import JSONRenderer
from rest_framework.response import Response
from .serializers import ZillowDeepSearchSerializer


class ZillowDeepSearchView(GenericAPIView):
    """ Zillow deep search API View """

    renderer_classes = (JSONRenderer,)
    parser_classes = (JSONParser,)
    serializer_class = ZillowDeepSearchSerializer

    def post(self, request):
        """ Query the Zillow API by address """

        serializer = self.get_serializer(data=self.request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.save())
