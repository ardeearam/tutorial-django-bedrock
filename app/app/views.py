from django.http import HttpResponse
from django.shortcuts import render
from app.lib.bedrock import Bedrock
from pprint import pprint
import json


def home(request):
  if request.method == 'GET':
    return render(request, 'app/index.html', {})
  elif request.method == 'POST':
    query = request.POST.get('query')
    bedrock_client = Bedrock()
    response = bedrock_client.retrieve_and_generate(query)
    
    message = response['output']['text']
    citations = response["citations"]
    
    contexts = []
    for citation in citations:
        retrievedReferences = citation["retrievedReferences"]
        for reference in retrievedReferences:
            contexts.append(reference["content"]["text"])


    pprint(response)
    pprint(message)

    return render(request, 'app/index.html', {'query': query, 'message': json.dumps(message)})
