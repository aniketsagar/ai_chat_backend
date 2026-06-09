
class CachingService():
  def __init__(self):
    # creating a dict of this kind 
    # CONVERSATION_CACHE = {
    #   "convid1":{
    #     "data":"this is an example"
    #   }
    # }
    self.conversation_cache = {}

  def write(self, conversation_id:str , chunk:str) :
    try:
      self.conversation_cache[conversation_id]["data"] += chunk 
    except:
  
      self.conversation_cache[conversation_id] =  {"data":chunk}
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
    except:
      return None 