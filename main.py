from langchain_groq.chat_models import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, HumanMessagePromptTemplate
from dotenv import load_dotenv
import os  
from langchain_core.output_parsers import StrOutputParser
from fastapi import FastAPI
from pydantic import BaseModel



load_dotenv()



api_key=os.getenv("GROQ_API_KEY")
model_name=os.getenv("MODEL_NAME")
chat_groq = ChatGroq(api_key=api_key, model=model_name) #type:ignore




#langsmith: python

langchain_api_key=os.getenv("LANGCHAIN_API_KEY")

os.environ["LANGCHAIN_TRACING_V2"] = "true"


prompt=ChatPromptTemplate(
    messages=[
        (
            "system",
            "You are an helpful assistant .Please Provide response to the user queries."
        ),
        (
            "user",
            "{query}."
        )
    ]
)

chain=prompt|chat_groq|StrOutputParser()

app = FastAPI()
class QueryRequest(BaseModel):
    query: str
    
@app.post("/get_response")
def get_response(query_request: QueryRequest):
    query = query_request.query
    response=chain.invoke({
        "query": query
    })
    return {"response": response}

