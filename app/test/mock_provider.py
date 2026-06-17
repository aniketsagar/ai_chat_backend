

class MockProvider():
  def __init__(self):
    pass

  def streamEvents(self, tokens:[str],conversation_id:str):
    event_count = 0
    chunk = {
      "data":None,
      "timestamp":datetime.now().timestamp(),
      "response_status":None,
      "converstation_id":conversation_id
    }

    for token in tokens:
      chunk["data"] = token
      chunk["response_status"]="in_progress"
      event_count += event_count
      yield chunk
    
    # sending last chunk here 
    chunk = {
      "data":None,
      "timestamp":datetime.now().timestamp(),
      "response_status":"completed",
      "converstation_id":conversation_id
    }
    yield chunk