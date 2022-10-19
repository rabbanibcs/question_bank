from fastapi import APIRouter,Depends,Request,Response,HTTPException,status
from .. import models,schemas,utils
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
from ..auth import get_current_user
from sqlalchemy import or_,and_,any_,text,func

router=APIRouter(
    prefix="/topics",
    tags=["topics"]
)

# create a topic
@router.post("/",response_model=schemas.TopicsOut)
async def create_topic(topic:schemas.Topics, db:Session=Depends(get_db)):
    new_topic=models.Topic(**topic.dict())
    db.add(new_topic)
    db.commit()
    db.refresh(new_topic)
    return new_topic

# fetch all topics 
@router.get("/",response_model=List[schemas.TopicsOut])
async def get_topics(db:Session=Depends(get_db)):
    query=db.query(models.Topic)
    print(query)
    return query.all()


# fetch questions by topic_id
@router.get("/{id}",response_model=List[schemas.BcsQuestionOut])
async def get_questions_with_topic_id(id:int,db:Session=Depends(get_db)):
    query=db.query(models.BcsQuestion).filter(models.BcsQuestion.topic_id==id)
    print(query)
    return query.all()
