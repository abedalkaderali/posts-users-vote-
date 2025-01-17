from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from sqlalchemy.orm import Session,join
from typing import List, Optional

from sqlalchemy import func
# from sqlalchemy.sql.functions import func
from .. import models, schemas, oauth2
from ..database import get_db



router =APIRouter(
    prefix="/posts",
    tags= ['posts']
    )



#get posts


@router.get("/",response_model=List[schemas.PostOut])
def get_posts(db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user), limit:int=10,skip:int=0,search:Optional[str]=""):
    
    
   
   results=db.query(models.Post,func.count(models.Vote.po_id).label("votes")).join(models.Vote,models.Vote.po_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.title.contains(search)).limit(limit).offset(skip)
   
   
   
   return results

#crete posts

@router.post("/", status_code=status.HTTP_201_CREATED, response_model=schemas.Post)
def create_posts(post: schemas.PostCreate, db: Session = Depends(get_db), current_user:int = Depends(oauth2.get_current_user)):
   # new_post = models.Post(title=post.title, content=post.content, published=post.published)
   # db.add(new_post)
   # db.commit()
   new_post = models.Post(owner_id=current_user.u_id, **post.dict())
   
   db.add(new_post)
   db.commit()
   db.refresh(new_post)
   return new_post
  



    
# get post from id

@router.get("/{id}",response_model=schemas.PostOut)
def get_post(id:int,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post = db.query(models.Post,func.count(models.Vote.po_id).label("votes")).join(models.Vote,models.Vote.po_id==models.Post.id,isouter=True).group_by(models.Post.id).filter(models.Post.id == id).first()
    if not post :
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND ,
                            detail=f"post with id: {id} was not found")
       
    return post 

#deleted post from id 

@router.delete("/{id}",status_code=status.HTTP_204_NO_CONTENT)
def delete_post(id:int,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post=post_query.first()
    
    
    if post  ==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail =f"post with id :{id} does not exist")
    if post.owner_id!= current_user.u_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail =f"not authorized")
    
    
    post_query.delete(synchronize_session=False)
    db.commit()
    return Response(status_code=status.HTTP_204_NO_CONTENT)

# update post from id 
        
@router.put("/{id}",response_model=schemas.Post)
def update_post(id:int, updated_post: schemas.PostCreate,db: Session = Depends(get_db),current_user:int=Depends(oauth2.get_current_user)):
    post_query = db.query(models.Post).filter(models.Post.id == id)
    post=post_query.first()
    
    
   
    if post==None:
       raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"post with id :{id} does not exist")
    if post.owner_id!= current_user.u_id:
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEN , detail =f"not authorized")   
   
   
    post_query.update(updated_post.dict(), synchronize_session=False)
    db.commit()
   
    return post_query.first()