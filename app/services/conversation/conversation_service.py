# This class owns the conversation responsibility
# so load conversation, store converstaion 


class ConversationService: 
  def generate_response(self,
                       message :str)-> str:
          return f"You asked: {message}"

