from fastapi import APIRouter

from ...models.chat import ChatRequest, ChatResponse
from ...services.conversation.conversation_service import ConversationService

import logging

logger = logging.getLogger(__name__)


router = APIRouter(prefix="/chat", tags=["chat"])

service = ConversationService()
logger.info("*******************************")
logger.info("created conversation service object")
logger.info(service)
@router.post("/")
async def process_chat(chat: ChatRequest) -> ChatResponse:

  try:
    generated_response = service.generate(chat.message,chat.conversation_id)
    logger.info("********************************")
    logger.info(generated_response)
    if(generated_response.result):
      res = ChatResponse (
        conversation_id = chat.conversation_id,
        status = "successful",
        success=True,
        result= generated_response.result,
        provider_name=generated_response.provider_name
      )
    else:
       res = ChatResponse (
        conversation_id = chat.conversation_id,
        status = "Failed",
        success=False,
        error=generated_response.error,
        error_code=generated_response.error_code,
        provider_name=generated_response.provider_name
      )
  except Exception as e:
    logger.info(f"::ChatApi::Exception::{e}")
    res = ChatResponse (
      conversation_id = chat.conversation_id,
      status = "Failed",
      success=False,
      error="internal server error",
      error_code="500",
      provider_name=generated_response.provider_name
    )
  return res 




@router.post("/stream")
async def process_chat(chat: ChatRequest):

  try:
    result = service.stream(chat.message,chat.conversation_id) 

    for chunk in result:
      print(chunk)
      yield chunk
    
  except Exception as e:
    logger.info(f"::ChatApi::Exception::{e}")
    res = ChatResponse (
      conversation_id = chat.conversation_id,
      status = "Failed",
      success=False,
      error="internal server error",
      error_code="500",
      provider_name="openai"
    )
    yield res 