import boto3
import json

class Bedrock:
  def __init__(self):
    self.client =  boto3.client("bedrock-agent-runtime", region_name='us-east-1')


  def retrieve_and_generate(self, query, model_arn=None, kb_id=None):

    #TODO: Use environment variables
    region_name = 'us-east-1'
    kb_id = 'BT29E7DRDU'
    model_id = 'anthropic.claude-3-5-sonnet-20241022-v2:0'
    model_arn = 'arn:aws:bedrock:us-east-1:357984781678:inference-profile/us.anthropic.claude-3-5-sonnet-20241022-v2:0'

    prompt_template = '''
        Instructions:
        You are an expert in the Philippine Labor Code. 
        Unless otherwise stated, assume that you are talking about Philippine laws. 
        You are answering a client's question. Be direct, straight-to-the-point, professional, but be empathic as well.
        Always state relevant law names and links if possible and available so that the user can double-check and cross-reference.
        You may use your pretrained data for response, provided it does not conflict with the search results.
        If there are no search results, feel free to look into your pretrained data.
        The data from the knowledge base has more weight than your pretrained data.
        If you are using pretrained data, always state the relevant law names and links (e.g. "According to....").
        If there is a conflict between the data from the knowledge base vs. your pretrained data, explain it, but give more weight to the knowledge base.
        If there are any conflicting provisions, explain in detail the conflict, and choose one path.

        Here are the law database results in numbered order:
        $search_results$ 

        Here is the user's question:
        <question>
        $query$
        </question>

        $output_format_instructions$

        Assistant:
    '''

    response = self.client.retrieve_and_generate(
        input={
            'text': query
        },
        retrieveAndGenerateConfiguration={
            'type': 'KNOWLEDGE_BASE',
            'knowledgeBaseConfiguration': {
                'knowledgeBaseId': kb_id,
                'modelArn': model_arn,
                'generationConfiguration': {
                'promptTemplate': {
                    'textPromptTemplate': prompt_template
                }
            }
            },
  
        },
    )

    return response

