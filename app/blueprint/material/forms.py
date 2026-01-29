from pydantic import BaseModel

class ValidationFormsBase(BaseModel):
    title: str 
    description: str 



