from __future__ import annotations
from rest_framework.response import Response
from rest_framework.views import APIView
from catalog.catalog_services.catalog_page import get_catalog_page_data


class CatalogAPIView(APIView):
    def get(self, request) -> Response:
        data = get_catalog_page_data()
        return Response({
            "status": "ok",
            **data
            })

