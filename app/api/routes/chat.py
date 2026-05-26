from fastapi import APIRouter

from ...models.chat import ChatRequest, ChatResponse
from ...services.conversation.conversation_service import ConversationService

import logging

logger = logging.getLogger(__name__)


router = APIRouter(prefix="/chat", tags=["chat"])

service = ConversationService()
logger.info("*******************************")
logger.info(service)
@router.post("/")
async def process_chat(chat: ChatRequest):
  conversation_history = service.generate_response(chat.message)
  res = ChatResponse (
    conversation_id = chat.conversation_id,
    status = "ok",
    response= f"success:  {conversation_history}"
  )
  return res 