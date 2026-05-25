from fastapi import APIRouter

from ...models.chat import ChatRequest, ChatResponse

router = APIRouter(prefix="/chat", tags=["chat"])



@router.post("/")
async def process_chat(chat: ChatRequest):
  res = ChatResponse (
    conversation_id = chat.conversation_id,
    status = "ok"
  )
  return res 