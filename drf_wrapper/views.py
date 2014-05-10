# REST Wrapper is a wrapper api which gets a list of api calls and return their result in one request
import urlparse
from django.core.urlresolvers import resolve
from django.http import QueryDict
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView


class RestWrapper(APIView):
    permission_classes = ()

    def get(self, request, *args, **kwargs):
        query_params = request.QUERY_PARAMS
        urls = query_params.get('urls').split(',')
        if urls is None:
            return Response(status=status.HTTP_200_OK)

        results = []
        store_query_params = request.QUERY_PARAMS
        for url in urls:
            parse_result = urlparse.urlparse(url)
            if parse_result.netloc == '':
                r = resolve(parse_result.path)

                if issubclass(r.func.cls, APIView):
                    url_query_params = QueryDict(parse_result.query)
                    request._request.GET = url_query_params
                    response = r.func(request)
                    results.append({
                        'url': url,
                        'status_code': response.status_code,
                        'result': response.data
                    })

        request._request.GET = store_query_params

        return Response({
            'results': results,
        })

wrapper_view = RestWrapper.as_view()