
# from fastapi import APIRouter,Depends,Request,Response,HTTPException,status
# from .. import models,schemas,utils
# from sqlalchemy.orm import Session
# from ..database import get_db
# from typing import List
# from ..auth import get_current_user
# from sqlalchemy import or_,and_,any_,text,func

# router=APIRouter(
#     prefix="/questions",
#     tags=["questions"]
# )

# # create a question
# @router.post("/",response_model=schemas.QuestionOut)
# async def create_question(question:schemas.CreateQuestion, db:Session=Depends(get_db)):
#     new_question=models.BcsQuestion(**question.dict())
#     db.add(new_question)
#     db.commit()
#     db.refresh(new_question)
#     return new_question

# # fetch all question 
# @router.get("/",response_model=List[schemas.BcsQuestionOut])
# async def get_questions(db:Session=Depends(get_db),limit:int=10,skip:int=0,search:str=""):
#     print(search)
#     query=db.query(models.BcsQuestion).filter(models.BcsQuestion.question.contains(search)).limit(limit).offset(skip)
#     print(query)
#     return query.all()



# # fetch questions by bcs
# @router.get("/{ordinal}",response_model=List[schemas.QuestionOut])
# async def get_question_by_bcs(ordinal:int,db:Session=Depends(get_db)):
#     query=db.query(models.BcsQuestion).filter(models.BcsQuestion.bcs==ordinal)
#     print(query)
    
#     return query.all()

# # update a post
# @router.put("/{post_id}",response_model=schemas.Post)
# async def update_question(post_id:int,post:schemas.PostUpdate , db:Session=Depends(get_db),user:int=Depends(get_current_user)):
#     query=db.query(models.Post).filter(models.Post.id==post_id)
#     to_update=query.first()
#     if to_update==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         detail=f'Post with id-{post_id} does not exist.')
#     # print(type(to_update.owner_id))    
#     # print(type(user_id.id))    
#     if to_update.owner_id != int(user.id):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#         detail=f'You can not update other\'s post.')
#     query.update(post.dict(),synchronize_session=False)
#     db.commit()
#     return query.first()

# # delete a post
# @router.delete("/{post_id}")
# async def delete_question(post_id:int,
#                     db:Session=Depends(get_db),
#                     user:int=Depends(get_current_user)):
#     query=db.query(models.Post).filter(models.Post.id==post_id)
#     to_delete=query.first()
#     if to_delete==None:
#         raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
#         detail=f'Post with id-{post_id} not found')
#     if to_delete.owner_id != int(user.id):
#         raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED,
#         detail=f'You can not delete other\'s post.')
#     query.delete()
#     db.commit()

#     return {"detail":"The post has been removed."}
























