
from fastapi import APIRouter,Depends,Request,Response,HTTPException,status
from .. import models,schemas,utils
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
from ..auth import get_current_user
from sqlalchemy import or_,and_,any_,text,func

router=APIRouter(
    prefix="/questions/bcs",
    tags=["Bcs questions"]
)

# create a question
@router.post("/",response_model=schemas.BcsQuestionOut)
async def create_question(question:schemas.CreateBcsQuestion, db:Session=Depends(get_db)):
    new_question=models.BcsQuestion(**question.dict())
    db.add(new_question)
    db.commit()
    db.refresh(new_question)
    return new_question

# fetch all question 
@router.get("/",response_model=List[schemas.BcsQuestionOut])
async def get_questions(db:Session=Depends(get_db),limit:int=10,skip:int=0,search:str=""):
    print(search)
    query=db.query(models.BcsQuestion).filter(models.BcsQuestion.question.contains(search)).limit(limit).offset(skip)
    print(query)
    return query.all()



# fetch questions by bcs
@router.get("/{ordinal}",response_model=List[schemas.BcsQuestionOut])
async def get_question_by_bcs(ordinal:int,db:Session=Depends(get_db)):
    query=db.query(models.BcsQuestion).filter(models.BcsQuestion.bcs==ordinal)
    print(query)
    
    return query.all()

# update a question
@router.put("/{id}",response_model=schemas.BcsQuestionOut)
async def update_question(id:int,question:schemas.CreateBcsQuestion , db:Session=Depends(get_db)):
    query=db.query(models.BcsQuestion).filter(models.BcsQuestion.id==id)
    to_update=query.first()
    if to_update==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'Post with id-{id} does not exist.')
    query.update(question.dict(),synchronize_session=False)
    db.commit()
    return query.first()

# delete a question
@router.delete("/{id}")
async def delete_question(id:int,
                    db:Session=Depends(get_db)):
    query=db.query(models.BcsQuestion).filter(models.BcsQuestion.id==id)
    to_delete=query.first()
    if to_delete==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'question with id no {id} not found')
    query.delete()
    db.commit()

    return {"detail":"The question has been removed."}




