from fastapi import FastAPI
from pydantic import BaseModel
from fastapi import File,UploadFile
app= FastAPI()
class Chatrequest(BaseModel):
    user_id : str
    name : str
    
    
    
    
    
    
@app.post("/chat")

def chat (request :  Chatrequest):
    print(request.user_id,request.name)
    return "successfull" 

@app.post("/Uploadvoice")
def Uploadvoice(file:UploadFile= File(...)):
    file.filename
    
