# this class contains the rigging of openai
import openai
from openai import OpenAI, OpenAIError
import logging
logger = logging.getLogger(__name__)
class OpenAIProvider():
  def __init__(self):
    try:
      self.client = OpenAI(
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