from django.shortcuts import render
from django.contrib.auth.models import User

from rest_framework import viewsets
from rest_framework.pagination import PageNumberPagination
from rest_framework.decorators import action
from rest_framework.response import Response

from . import serializers, models



class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer
    lookup_field = 'username'


class DatabaseViewSet(viewsets.ModelViewSet):
    queryset = models.Database.objects.all()
    serializer_class = serializers.DatabaseSerializer
    lookup_field = 'slug'


class EntriesPagination(PageNumberPagination):
    page_size=3


class TableViewSet(viewsets.ModelViewSet):
    queryset = models.Table.objects.all()
    lookup_field = 'slug'
    pagination_class=EntriesPagination

    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.DatabaseTableListSerializer
        return serializers.TableSerializer


    @action(methods=['get'], detail=True, url_path='entries', url_name='entries')
    def entries(self, request, slug):
        obj = self.get_object()
        queryset = obj.entries.all()

        page = self.paginate_queryset(queryset)

        if page is not None:
            str_fields = request.GET.get('fields', '') if request else None
            fields = str_fields.split(',') if str_fields else None
            if not fields:
                fields = obj.fields.values_list('name', flat=True)[:2]
            serializer = serializers.EntrySerializer(page, many=True, context={'fields': fields})
            return self.get_paginated_response(serializer.data)
        serializer = serializers.EntrySerializer(queryset, many=True)
        return Response(serializer.data)
