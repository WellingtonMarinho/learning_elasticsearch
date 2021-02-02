from django.shortcuts import render

import logging
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
import elasticsearch

from .document import PeoplesDocument
from .helps import ElasticSearchPeopleService
from .utils import is_empty_or_null, rebuild_elasticsearch_index, delete_elasticsearch_index

logger = logging.getLogger(__name__)


class PeopleSearchView(APIView):
    def __send_response(self, message, status_code, data=None):
        content = {
            'message': message,
            'result': data if data is not None else []
            }
        return Response(content, status=status_code)

    def post(self, request):
        query = request.data.get('queries', None)
        k = request.data.get('k', None)

        if is_empty_or_null(query):
            error_messsage = 'Consultas não podem ser realizadas.'
            return self.__send_response(error_messsage, status.HTTP_400_BAD_REQUEST)

        if is_empty_or_null(k):
            error_message = 'Houve algum erro ao tentar realizar a busca.'
            return self.__send_response(error_message, status.HTTP_400_BAD_REQUEST)

        try:
            rebuild_elasticsearch_index()

            search_doc = ElasticSearchPeopleService(PeoplesDocument, query, k)
            result = search_doc.run_query_list()
            response = {'Pessoas': result}
            delete_elasticsearch_index()

        except elasticsearch.ConflictError as connection_error:
            logger.debug('ConnectionError: ', str(connection_error))
            error_message = "ElasticSearch Connection refused."
            return self.__send_response(error_message, status.HTTP_503_SERVICE_UNAVAILABLE)


        except Exception as exception_msg:
            logger.debug('Exception: ', str(exception_msg))
            error_message = str(exception_msg)
            return self.__send_response(error_message, status.HTTP_400_BAD_REQUEST)

        return self.__send_response('success', status.HTTP_200_OK, response)

