"""
    serializers
    ~~~~~~~~~~~

    Zillow related DRF serializers.
"""

from rest_framework import serializers
from .utils import deep_search


class ZillowDeepSearchSerializer(serializers.Serializer):
    """ ZillowDeepSearchSerializer serializer """

    street = serializers.CharField(max_length=100)
    citystatezip = serializers.CharField(max_length=100)

    def save(self, **kwargs):
        """ Override the default save method """

        return deep_search(
            self.validated_data['street'],
            self.validated_data['citystatezip'],
        )
