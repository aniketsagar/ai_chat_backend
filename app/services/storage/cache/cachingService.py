
class CachingService():
  def __init__(self):
    # creating a dict of this kind 
    # CONVERSATION_CACHE = {
    #   "convid1":{
    #     "data":"this is an example",
    #     "conversation_id": conversation_id
    #     "timestamp": time at which event was generated.
    #     "status": Started/InProgress/Completed/Failed
    #   }
    # }
    self.conversation_cache = {}

  def write(self, conversation_id:str , chunk:str) :
    try:
      print(">>>>>>>>>>>>>>>>>>>>>CACHE<<<<<<<<<<<<<<<<<<<<<<<<<<")
      print(chunk)
      if(chunk["data"]):
        self.conversation_cache[conversation_id]["data"] += chunk["data"] 
      self.conversation_cache[conversation_id]["timestamp"] = chunk["timestamp"]
      self.conversation_cache[conversation_id]["response_status"] = chunk["response_status"]
      self.conversation_cache[conversation_id]["conversation_id"] = conversation_id

    except:
      if(chunk["data"]):
        self.conversation_cache[conversation_id] =  {"data":chunk["data"]}
      else:
        self.conversation_cache[conversation_id] =  {"data":None}
      self.conversation_cache[conversation_id]["timestamp"] = chunk["timestamp"]
      self.conversation_cache[conversation_id]["response_status"] = chunk["response_status"]
      self.conversation_cache[conversation_id]["conversation_id"] = conversation_id

  def read(self,conversation_id):
    # here we are returning the object since this is mostly for 
    # storage

    try:
      return self.conversation_cache[conversation_id]
    except:
      return None
  
  def delete(self, conversation_id):
    try:
      return self.conversation_cache.pop(conversation_id, None)
    except Exception as  e:
      return e 