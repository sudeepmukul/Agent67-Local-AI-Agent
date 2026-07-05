from llm import llm

def chatbot(state):
    return{
        "messages":[
            llm.invoke(state["messages"])
        ]
    }