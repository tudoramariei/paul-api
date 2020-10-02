from rest_framework import viewsets, mixins
from rest_framework.views import APIView
from rest_framework.response import Response

from plugin_woocommerce import (
    models,
    serializers,
    tasks)


class TaskResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TaskResult.objects.all()

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.TaskResultListSerializer

        return serializers.TaskResultSerializer


class SettingsViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = models.Settings.objects.all()
    serializer_class = serializers.SettingsSerializer


class RunSyncView(APIView):
    """
    View that runs the Woocommerce sync
    """

    def get(self, request, format=None):
        response = tasks.sync_wc(request)
        print(response)
        # return response
        return Response(response)