"""
    serializers
    ~~~~~~~~~~~

    Zillow related DRF serializers.
"""

from rest_framework import serializers
from .utils import deep_search


class ZillowDeepSearchForm(serializers.Serializer):
    """ ZillowDeepSearchForm serializer """

    street = serializers.CharField(max_length=100)
    citystatezip = serializers.CharField(max_length=100)

    def save(self, **kwargs):
        """ DRF Override to perform the Zillow query """

        return deep_search(
            self.validated_data['street'],
            self.validated_data['citystatezip'],
        )
