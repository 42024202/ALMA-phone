from __future__ import annotations
from rest_framework.views import APIView
from rest_framework.response import Response
from catalog.catalog_services.main_page import main_page_data


class MainPageAPIView(APIView):
    def get(self, request) -> Response:
        data = main_page_data()
        return Response({
            "status": "ok",
            **data 
            })

