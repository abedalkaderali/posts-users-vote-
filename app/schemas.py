from pydantic import BaseModel ,EmailStr

from datetime import datetime
from typing import Optional , List
from pydantic import BaseModel, conint





class PostBase(BaseModel):
    title: str
    content: str
    published: bool=True 
   
class PostCreate(PostBase):
    

    pass

class UserOut(BaseModel):
    u_id:int
    u_email:EmailStr
    u_created_at:datetime
    class Config:
        from_attributes = True  
        
        
        
class Post(PostBase):
    
    id:int
    created_at:datetime
    owner_id:int
    owner:UserOut
    class Config:
        from_attributes = True
        
class PostOut(BaseModel):
    Post:Post
    votes :int
    class Config:
        from_attributes = True        

class UserCreate(BaseModel):
    u_email:EmailStr
    u_password:str
   
   

        
        
class UserLogin(BaseModel):
    u_email:EmailStr
    u_password:str
        
        
class Token(BaseModel):
    access_token:str
    token_type:str
    
class TokenData(BaseModel):
      user_id: Optional[int]=None
      

class Vote(BaseModel):
    po_id:int
    dir: int