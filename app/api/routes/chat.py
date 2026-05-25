from fastapi import APIRouter

from ...models.chat import ChatRequest, ChatResponse
from ...services.conversation.conversation_service import ConversationService
router = APIRouter(prefix="/chat", tags=["chat"])

service = ConversationService()
@router.post("/")
async def process_chat(chat: ChatRequest):
  conversation_history = service.generate_message(chat.message)
  res = ChatResponse (
    conversation_id = chat.conversation_id,
    status = "ok",
    response= f"success:  {conversation_history}"
  )
  return res 