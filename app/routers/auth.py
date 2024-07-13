from fastapi import FastAPI , Response , status , HTTPException , Depends , APIRouter
from fastapi.security.oauth2 import OAuth2PasswordRequestForm
from sqlalchemy.orm import session
from .. import database,schemas,models,utils,oauth2
from typing import List


router = APIRouter(tags=['authentiction'])


@router.post('/login')
def login(user_credentials:OAuth2PasswordRequestForm = Depends(),db:session=Depends(database.get_db)):
    user = db.query(models.User).filter(models.User.u_email==user_credentials.username).first()
    
    if not user :
        raise HTTPException(status_code=status.HTTP_403_FORBIDDEND ,detail=f"Invalid Credentials")
       
    if not utils.verify(user_credentials.password, user.u_password):
         raise HTTPException(status_code=status.HTTP_403_FORBIDDEND ,detail=f"Invalid Credentials")
     
     
    access_token =oauth2.create_access_token(data={"user_id":user.u_id})
    


    return{"access_token": access_token ," token_type":"bearer"}


