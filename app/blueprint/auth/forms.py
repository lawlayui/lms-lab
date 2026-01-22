from pydantic import BaseModel, field_validator

class Validatior(BaseModel):
    username: str 
    password: str 

    @field_validator('username')
    def username(cls,v):
        if len(v) > 25 or len(v) < 5:
            raise ValueError("Username must be at least 5 characters and a maximum of 25 characters")
        return v 
    
    @field_validator('password')
    def password(cls,v):
        if len(v) > 40 or len(v) < 8:
            raise ValueError("Password must be at least 8 characters and a maximum of 40 characters")
        return v 
    
def validation_forms(data:dict):
    username = None 
    password = None 
    try: 
        username = data['username']
        password = data['password']
    except:
        raise ValueError("Key not found")
    
    Validatior(username=username,password=password)