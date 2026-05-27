# this class contains the rigging of openai
import openai
from openai import OpenAI, OpenAIError
import logging
logger = logging.getLogger(__name__)
class OpenAIProvider():
  def __init__(self):
    try:
      self.client = OpenAI(
        #api_key ="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"
      )
    except Exception as e:
      logger.info(f"::Failed to create OpenAI object::Error::{e}")
  def processRequest(self,prompt):
    logger.info(prompt)
    response = None 
    try:
      
      response = self.client.responses.create(
        model = "gpt-4.1-nano",# this is cheapest
        input =  prompt["input"],
        instructions = prompt["instruction"]
      )
    except OpenAIError as e:
      response = {
        "status": 1,
        "agent_error": e     
      }
    logger.info("OpenAI response ##########")
    logger.info(response)
    return response