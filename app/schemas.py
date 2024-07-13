from pydantic import BaseModel ,EmailStr
from datetime import datetime



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