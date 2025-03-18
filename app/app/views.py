from django.http import HttpResponse
from django.shortcuts import render
from app.lib.bedrock import Bedrock
from pprint import pprint
import json


def home(request):
  if request.method == 'GET':

    return render(request, 'app/index.html', {})

  # POSTback (old school)
  # We can do AJAX style, but it will make this tutorial 
  # more complicated than it should be.
  elif request.method == 'POST':

    query = request.POST.get('query')
    bedrock_client = Bedrock()
    response = bedrock_client.retrieve_and_generate(query)
    
    message = response['output']['text']
    citations = response["citations"]
    retrieved_references = [citation["retrievedReferences"] for citation in citations]


    #Flatten retrieved_references
    flat_retrieved_references = [item for retrienved_reference_item in retrieved_references for item in retrienved_reference_item]
  
    references = set([
      f'''
        <div>
          <blockquote>...{flat_retrieved_references_item['content']['text']}...</<blockquote>
          <cite>&mdash; {flat_retrieved_references_item['location']['s3Location']['uri']}</cite>
        </div>
      '''
      for flat_retrieved_references_item in flat_retrieved_references
    ])

    references_string = " ".join(references)

    return render(request, 'app/index.html', {
      'query': query, 
      'message': json.dumps(message),
      'references': json.dumps(references_string),
      'references_count': len(references)
    }) 
      
