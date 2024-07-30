from fastapi import FastAPI, Response, status, HTTPException, Depends, APIRouter
from .. import schemas,database,models,oauth2
from sqlalchemy.orm import Session



router = APIRouter (
    prefix="/vote",
    tags=['Vote']
)

@router.post("/",status_code=status.HTTP_201_CREATED)
def vote(vote:schemas.Vote,db:Session = Depends(database.get_db),current_user:int=Depends(oauth2.get_current_user)):
    post=db.query(models.Post).filter(models.Post.id==vote.po_id).first()
    if not post:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"post with id :{vote.po_id} does not exist")
    
    
    
    vote_query=db.query(models.Vote).filter(models.Vote.po_id==vote.po_id,models.Vote.us_id==current_user.u_id)
    found_vote = vote_query.first()

    if(vote.dir==1):
        if found_vote:
            raise HTTPException(status_code=status.HTTP_409_CONFLICT,detail=f"User {current_user.u_id} has already voted on post {vote.po_id}")
        new_vote = models.Vote(po_id=vote.po_id,us_id=current_user.u_id)
        db.add(new_vote)
        db.commit()
        return{"message":"successfully added vote"}
    else:
        if not found_vote:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Vote does not exist")
        vote_query.delete(synchronize_session=False)
        db.commit()
        return{"message":"successfully deleted vote"}
        