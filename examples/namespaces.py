from __future__ import print_function
import time
import core.api
from core.api.rest import ApiException
from pprint import pprint
configuration = core.api.Configuration()
configuration.api_key['authorization'] = ''
configuration.api_key_prefix['authorization'] = 'Bearer'  # Enter a context with an instance of the API client
# Enter a context with an instance of the API client
with core.api.ApiClient(configuration) as api_client:
    api_client.configuration.host = "http://localhost:8888"
    # Create an instance of the API class
    api_instance = core.api.NamespaceServiceApi(api_client)

    try:
        api_response = api_instance.list_namespaces()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling NamespaceServiceApi->list_namespaces: %s\n" % e)