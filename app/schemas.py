from unicodedata import name
from pydantic import BaseModel,EmailStr,validator
from typing import Union,Optional,List
from datetime import date
# from app.database import Base

class Topics(BaseModel):
    name:str

class TopicsOut(BaseModel):
    id:int
    name:str

    class Config:
        orm_mode=True
class QuestionTopic(BaseModel):
    name:str

    class Config:
        orm_mode=True
# ---------------------------------#

class BcsBase(BaseModel):
    ordinal:int
    total_marks:int
    duration:int


class CreateBcs(BcsBase):
    special:Optional[str]
    exam_year:str

class BcsUpdate(CreateBcs):
    pass

# ---------------------------------#

class QuestionsBase(BaseModel):
    question:str
    option_a:str
    option_b:str
    option_c:str
    option_d:str
    answer:str


class CreateBcsQuestion(QuestionsBase):
    bcs:int
    topic_id:int
    note:str
    explanation:str

class BcsQuestionOut(QuestionsBase):
    bcs:int
    # topic_id:Optional[int]
    id:int
    topic:QuestionTopic

    class Config:
        orm_mode=True

class BcsOut(BcsBase):
    special:Optional[str]
    exam_year:str
    questions:List[BcsQuestionOut]

    class Config:
        orm_mode=True

class TopicsOut(BaseModel):
    id:int
    name:str
    # questions:List[BcsQuestionOut]
    # questions:List[BcsQuestionOut]

    class Config:
        orm_mode=True
#---------------------------------------

class UserOut(BaseModel):
    id:int
    name:str
    email:EmailStr
    phone:str
    
    class Config:
        orm_mode=True


class UserVerify(BaseModel):
    email:EmailStr
    password:str

class UserCreate(UserVerify):
    name:str
    phone:str

    @validator('phone')
    def validate_like(cls, v):
        if v not in [0,1]:
            raise ValueError('[like] Must be 0 or 1.')
        return v
    

class Token(BaseModel):
    access_token: str
    token_type: str

class TokenData(BaseModel):
    id: Union[str, None] = None


class Vote(BaseModel):
    post_id:int
    like:int

    @validator('like')
    def validate_like(cls, v):
        if v not in [0,1]:
            raise ValueError('[like] Must be 0 or 1.')
        return v

















