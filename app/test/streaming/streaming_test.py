import uuid    
from ..mock_provider import MockProvider
class StreamingTest():
  def __init__(self):
    

    self.__corpus_a = ("Hey Product Hunt. "
                          "We built Dopami because we kept asking the same question: " 
                          "why does TikTok know exactly when to grab my attention, but my to-do list doesn't? "
                          "The answer is behavioral algorithms. TikTok learns your habits, your active windows," 
                          "your patterns and serves content at the exact moment you'll engage. "
                          "It works flawlessly. The problem is it works against you. "
                          "We built the same engine. But instead of serving you a Reel, "
                          "it surfaces the right chore at the right moment. "
                          " Here's what that means in practice: "
                          "No alarms to set. No rigid routines to maintain. "
                          "Dopami observes when you open the app, which missions you complete, "
                          "in what order, at what time. "
                          "The more you use it, the more precisely it knows when to nudge you not with "
                          "a generic reminder, but with a specific mission calibrated to your energy right now. " )



    self.__corpus_b = ("Models matter. Context matters more. That one line is the whole reason this exists. "
                      "I build with AI agents every day, and I kept hitting the same wall: "
                      "an agent starts a long task brilliantly, then somewhere around hour three it quietly drifts. "
                      "The diff still compiles — it's just not what I asked for. There was never a clean way to resume, "
                      "because the whole plan lived in a chat window that had grown too long to trust. "
                      "I stopped treating that as a prompting problem and started treating it as a structural one. "
                      "The fix wasn't a smarter model. It was giving the agent a plan it couldn't drift from "
                      "written into the repository itself. "
                      "That's Deep Work Plan. The idea is two moves: "
                      "Make the plan the source of truth, not the chat. Before any code, "
                      "you write a spec: a goal, atomic tasks, and for each task explicit acceptance criteria  "
                      "a validation gate. Done is decided by the gate, "
                      "not by how the model feels. And it lives on disk, so it survives a context reset or "
                      "a handoff to a different agent tomorrow. " )
  def tokenize(self, corpus:str):
    result = corpus.split(" ")
    return result
  
  def testStream(self):
    conversation_id_1 = uuid.uuid4()
    conversation_id_2 = uuid.uuid4()  
    
    print("###############TOKENS#######################")
    tokens_a = self.tokenize(self.__corpus_a)
    print(tokens_a)
    print("###############TOKENS#######################")
    tokens_b = self.tokenize(self.__corpus_b)
    print(tokens_b)

    # we want to instantiate two threads, with each corpus and tokens
    # then we want to 


s = StreamingTest()

s.testStream()