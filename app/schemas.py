from pydantic import BaseModel ,EmailStr
from datetime import datetime
from typing import Optional , List





class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True 
   
class PostCreate(PostBase):

    pass


class Post(PostBase):
    
    id:int
    created_at:datetime
    class Config:
        from_attributes = True

class UserCreate(BaseModel):
    u_email:str
    u_password:str
   
   
class UserOut(BaseModel):
    u_id:int
    u_email:EmailStr
    u_created_at:datetime
    class Config:
        from_attributes = True  
        
        
class UserLogin(BaseModel):
    u_email:EmailStr
    u_password:str
        
        
class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
     id : Optional[str] = None 