# this class contains the rigging of openai
import os
from datetime import datetime
import openai
from openai import OpenAI
import logging
from dotenv import find_dotenv, load_dotenv
from ...models.openaiProvider import OpenAIProviderResult
logger = logging.getLogger(__name__)

load_dotenv(find_dotenv("local"))
print("*(*(*(*(*(*(*(*(*(*(*))))))))))")
print (os.getenv("OPENAI_API_KEY"))
class OpenAIProvider():
  def __init__(self,max_retries:int=0):
    try:
      self.client = OpenAI(
        max_retries=max_retries,
        timeout=120
      )
      self.provider = "openai"
    except Exception as e:
      logger.info(f"::Failed to create OpenAI object::Error::{e}")
  def generate(self,prompt) -> OpenAIProviderResult:
    logger.info(prompt)
    response = None
    error_code = None
    error = None
    error_type = None 
    response = None 
    provider =self.provider
    clientResponse = None
    conversation_id = prompt["conversation_id"]
    timestamp = None
    try:
     
      clientResponse = self.client.responses.create(
        model = "gpt-4.1-nano",# this is cheapest
        input =  prompt["input"],
        instructions = prompt["instruction"],
        store=False
      )
    except openai.BadRequestError as e: # Don't forget to add openai
      # Handle error 400
      error_code = str(400)
      error_type = "BAD_REQUEST_ERROR"
      logger.info(f"Error 400: {e}")
    except openai.AuthenticationError as e: # Don't forget to add openai
      # Handle error 401
      error_code = str(401)
      error_type = "AUTH_ERROR"
      logger.info(f"Error 401: {e}")
    except openai.PermissionDeniedError as e: # Don't forget to add openai
      # Handle error 403
      error_code = str(403)
      error_type = "PERMISSION_DENIED_ERROR"
      logger.info(f"Error 403: {e}")
    except openai.NotFoundError as e: # Don't forget to add openai
      # Handle error 404
      error_code = str(404)
      error_type = "NOT_FOUND_ERROR"
      logger.info(f"Error 404: {e}")
    except openai.UnprocessableEntityError as e: # Don't forget to add openai
      # Handle error 422
      error_code = str(422)
      error_type = "UNPROCESSABLE_ENTITY_ERROR"
      logger.info(f"Error 422: {e}")
    except openai.RateLimitError as e: # Don't forget to add openai
      # Handle error 429
      error_code = str(429)
      error_type = "RATE_LIMIT_ERROR"
      logger.info(f"Error 429: {e}")
    except openai.InternalServerError as e: # Don't forget to add openai
      # Handle error >=500
      error_code = str(500)
      error_type = "INTERNAL_SERVER_ERROR"
      logger.info(f"Error >=500: {e}")
    except openai.APIConnectionError as e: # Don't forget to add openai
      # Handle API connection error
      error_code = None
      error_type = "API_CONNECTION_ERROR"
      logger.info(f"API connection error: {e}")
    except openai.OpenAIError as e:
      error_type = "OPENAI_ERROR"
      error = e
      logger.info(f"::openai provider:: {e}")
    
    logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>")
    logger.info(clientResponse)
    if(clientResponse):
      response = OpenAIProviderResult(
        success= True,
        result = clientResponse.output_text,
        provider = provider,
        timestamp = datetime.now().timestamp(),
        conversation_id=conversation_id,
        response_status="completed"
      )
    else:
      logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> IN else")
      response = OpenAIProviderResult(
        success = False,
        error = None,
        error_type = error_type,
        provider = provider,
        error_code=error_code ,
        timestamp = datetime.now().timestamp(),
        conversation_id=conversation_id,
        response_status="failed"
      )
    logger.info("OpenAI response ##########")
    logger.info(response)
    logger.info("OpenAI response ?>>>>>>>>>>>>>>>>>>>>>##########")
    return response
  
  # streaming the response from openai 
  
  def stream(self,prompt) :

    
    # {
    # data:"",
    # timestamp:"",
    # response_status:"",
    # conversation_id:""
    # }

    logger.info(prompt)
    response = None
    error_code = None
    error = None
    error_type = None 
    response = None 
    provider =self.provider
    stream = None
    
    try:
      conversation_id = prompt["conversation_id"]
      stream = self.client.responses.create(
        model = "gpt-4.1-nano",# this is cheapest
        input =  prompt["input"],
        instructions = prompt["instruction"],
        store=False,
        stream = True
      ) 
      for event in stream:
        print (event)
        chunk = {
          "data":None,
          "timestamp":datetime.now().timestamp(),
          "response_status":None,
          "converstation_id":conversation_id
        }
        if(event.type== "response.created" or
           event.type == "response.output_text.delta" or
          event.type == "response.in_progress" ):
          chunk["response_status"]= "in_progress"
        elif(event.type=="response.output_text.done" or 
             event.type == "response.content_part.done" or 
             event.type =="response.completed"):
          chunk["response_status"]= "completed"
        if(event.type == "response.output_text.delta"):
          chunk["data"] = event.delta
        yield chunk
        
       
    except openai.BadRequestError as e: # Don't forget to add openai
      # Handle error 400
      error_code = str(400)
      error_type = "BAD_REQUEST_ERROR"
      logger.info(f"Error 400: {e}")
    except openai.AuthenticationError as e: # Don't forget to add openai
      # Handle error 401
      error_code = str(401)
      error_type = "AUTH_ERROR"
      logger.info(f"Error 401: {e}")
    except openai.PermissionDeniedError as e: # Don't forget to add openai
      # Handle error 403
      error_code = str(403)
      error_type = "PERMISSION_DENIED_ERROR"
      logger.info(f"Error 403: {e}")
    except openai.NotFoundError as e: # Don't forget to add openai
      # Handle error 404
      error_code = str(404)
      error_type = "NOT_FOUND_ERROR"
      logger.info(f"Error 404: {e}")
    except openai.UnprocessableEntityError as e: # Don't forget to add openai
      # Handle error 422
      error_code = str(422)
      error_type = "UNPROCESSABLE_ENTITY_ERROR"
      logger.info(f"Error 422: {e}")
    except openai.RateLimitError as e: # Don't forget to add openai
      # Handle error 429
      error_code = str(429)
      error_type = "RATE_LIMIT_ERROR"
      logger.info(f"Error 429: {e}")
    except openai.InternalServerError as e: # Don't forget to add openai
      # Handle error >=500
      error_code = str(500)
      error_type = "INTERNAL_SERVER_ERROR"
      logger.info(f"Error >=500: {e}")
    except openai.APIConnectionError as e: # Don't forget to add openai
      # Handle API connection error
      error_code = None
      error_type = "API_CONNECTION_ERROR"
      logger.info(f"API connection error: {e}")
    except openai.OpenAIError as e:
      error_type = "OPENAI_ERROR"
      error = e
      logger.info(f"::openai provider:: {e}")
    
    if (error_code or error_type):
      logger.info(">>>>>>>>>>>>>>>>>>>>>>>>>>>>>> IN else")
      response = OpenAIProviderResult(
        success = False,
        error = None,
        error_type = error_type,
        provider = provider,
        error_code=error_code,
        timestamp:datetime.now().timestamp(),
        conversation_id=conversation_id
      )
      logger.info("OpenAI response ##########")
      logger.info(response)
      logger.info("OpenAI response ?>>>>>>>>>>>>>>>>>>>>>##########")
      yield response