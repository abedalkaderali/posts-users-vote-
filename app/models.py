
from sqlalchemy import Column, ForeignKey , Integer , String ,Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql.expression import text
from sqlalchemy.sql.sqltypes import TIMESTAMP
from .database import Base

class Post(Base):
    __tablename__ = "posts"
    
    id = Column(Integer , primary_key=True,  nullable=False )
    title = Column(String, nullable=False)
    content = Column(String, nullable=False)
    published= Column(Boolean,server_default='True',nullable=False,)
    created_at= Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    owner_id=Column(Integer,ForeignKey("users.u_id", ondelete="CASCADE"), nullable=False)
    
    
    owner=relationship("User")
    
    
class User(Base):
    __tablename__ = "users"
    u_id=Column(Integer , primary_key=True,  nullable=False )
    u_email=Column(String,nullable=False,unique=True)
    u_password=Column(String,nullable=False)
    u_created_at=Column(TIMESTAMP(timezone=True),nullable=False,server_default=text('now()'))
    u_phone_number=Column(String)
    
class Vote(Base):
    __tablename__ = "votes"
    us_id = Column(Integer, ForeignKey(
        "users.u_id", ondelete="CASCADE"), primary_key=True)
    po_id = Column(Integer, ForeignKey(
        "posts.id", ondelete="CASCADE"), primary_key=True)
    