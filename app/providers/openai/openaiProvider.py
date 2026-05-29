# this class contains the rigging of openai
import openai
from openai import OpenAI
import logging
from ...models.openaiProvider import OpenAIProviderResult
logger = logging.getLogger(__name__)

class OpenAIProvider():
  def __init__(self,max_retries:int=0):
    try:
      self.client = OpenAI(
        max_retries=max_retries,
        timeout=120,)
    except Exception as e:
      logger.info(f"::Failed to create OpenAI object::Error::{e}")
  def generate(self,prompt) -> OpenAIProviderResult:
    logger.info(prompt)
    response = None
    try:
      error_code = None
      error = None
      error_type = None 
      response = None 
      provider : "openai"
      clientResponse = None
      clientResponse = self.client.responses.create(
        model = "gpt-4.1-nano",# this is cheapest
        input =  prompt["input"],
        instructions = prompt["instruction"],
        store=False
      )
    except openai.BadRequestError as e: # Don't forget to add openai
      # Handle error 400
      error_code = str(400)
      error_type = "Bad Request Error"
      logger.info(f"Error 400: {e}")
    except openai.AuthenticationError as e: # Don't forget to add openai
      # Handle error 401
      error_code = str(401)
      error_type = "Authentication Error"
      logger.info(f"Error 401: {e}")
    except openai.PermissionDeniedError as e: # Don't forget to add openai
      # Handle error 403
      error_code = str(403)
      error_type = "Permission Denied Error"
      logger.info(f"Error 403: {e}")
    except openai.NotFoundError as e: # Don't forget to add openai
      # Handle error 404
      error_code = str(404)
      error_type = "Not Found Error"
      logger.info(f"Error 404: {e}")
    except openai.UnprocessableEntityError as e: # Don't forget to add openai
      # Handle error 422
      error_code = str(422)
      error_type = "Unprocessable Entity Error"
      logger.info(f"Error 422: {e}")
    except openai.RateLimitError as e: # Don't forget to add openai
      # Handle error 429
      error_code = str(429)
      error_type = "Rate Limit Error"
      logger.info(f"Error 429: {e}")
    except openai.InternalServerError as e: # Don't forget to add openai
      # Handle error >=500
      error_code = str(500)
      error_type = "Internal Server Error"
      logger.info(f"Error >=500: {e}")
    except openai.APIConnectionError as e: # Don't forget to add openai
      # Handle API connection error
      error_code = None
      error_type = "API connection error"
      logger.info(f"API connection error: {e}")
    except openai.OpenAIError as e:
      error_code = str(403)
      error = e
      logger.info(f"::openai provider:: {e}")
    
    if(clientResponse):
      response = OpenAIProviderResult(
        success= True,
        result = clientResponse.output_text,
        provider = provider
      )
    else:
      response = OpenAIProviderResult(
        success = False,
        error = error,
        error_type = error_type,
        provider = provider,
        error_code=error_code 
      )


    logger.info("OpenAI response ##########")
    logger.info(response)
    return response