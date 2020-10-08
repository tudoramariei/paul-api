from rest_framework import viewsets, mixins
from rest_framework.pagination import PageNumberPagination
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import action

from plugin_mailchimp import (
    models,
    serializers,
    tasks)

from api import models as api_models


class EntriesPagination(PageNumberPagination):
    page_size = 10
    page_size_query_param = "perPage"
    max_page_size = 1000

    def get_paginated_response(self, data):
        return Response(
            {
                "links": {
                    "next": self.get_next_link(),
                    "previous": self.get_previous_link(),
                },
                "count": self.page.paginator.count,
                "total_pages": self.page.paginator.num_pages,
                "results": data,
            }
        )


class TaskViewSet(viewsets.ModelViewSet):
    queryset = models.Task.objects.all()
    pagination_class = EntriesPagination

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.TaskListSerializer
        elif self.action in ["create", "update", "partial_update"]:
            return serializers.TaskCreateSerializer
        return serializers.TaskSerializer

    @action(
        detail=True,
        methods=["get"],
        name="Run Task",
        url_path="run",
    )
    def run(self, request, pk):
        task = self.get_object()
        if task.task_type == 'sync':
            task_result = tasks.sync(request)
            task_result.task = task
            task_result.save()

            result = serializers.TaskResultSerializer(
                task_result, context={'request': request})

        else:
            result = {}
        return Response(result.data)


class TaskResultViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = models.TaskResult.objects.all()
    pagination_class = EntriesPagination

    def get_serializer_class(self):
        if self.action == "list":
            return serializers.TaskResultListSerializer
        return serializers.TaskResultSerializer


class SettingsViewSet(mixins.RetrieveModelMixin,
                      mixins.UpdateModelMixin,
                      viewsets.GenericViewSet):
    queryset = models.Settings.objects.all()
    serializer_class = serializers.SettingsSerializer


class AudiencesView(APIView):
    """
    View that runs the mailchimp sync
    """

    def get(self, request, format=None):
        settings = models.Settings.objects.last()
        audiences = api_models.Entry.objects.filter(
            table__name=settings.audiences_table_name).values(
            'data__id', 'data__name')
        tags = api_models.Entry.objects.filter(
            table__name=settings.audience_tags_table_name).values(
            'data__id', 'data__name', 'data__audience_id')
        response = []
        for audience in audiences:
            audience_dict = {
                "name": audience['data__name'],
                "id": audience['data__id'],
                "tags": []
            }
            audience_tags = list(filter(
                lambda x: x['data__audience_id'] == audience_dict['id'], tags))

            for tag in audience_tags:
                audience_dict['tags'].append(tag['data__name'])
            response.append(audience_dict)
        return Response(response)
