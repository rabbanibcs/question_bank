
from fastapi import APIRouter,Depends,Request,Response,HTTPException,status
from .. import models,schemas,utils
from sqlalchemy.orm import Session
from ..database import get_db
from typing import List
from ..auth import get_current_user
from sqlalchemy import or_,and_,any_,text,func

router=APIRouter(
    prefix="/bcs",
    tags=["Bcs"]
)

# create a bcs
@router.post("/",response_model=schemas.BcsOut)
async def create_bcs(bcs:schemas.CreateBcs,
                     db:Session=Depends(get_db)):
    new_bcs=models.Bcs(**bcs.dict())
    db.add(new_bcs)
    db.commit()
    db.refresh(new_bcs)
    return new_bcs

# fetch all bcs         %20 for space
@router.get("/",response_model=List[schemas.BcsOut])
async def get_bcs(db:Session=Depends(get_db), limit:int=10,skip:int=0):
    query=db.query(models.Bcs).order_by(models.Bcs.ordinal).limit(limit).offset(skip)
    print(query)
    return query.all()

# fetch a bcs
@router.get("/{ordinal}",response_model=schemas.BcsOut)
async def get_bcs(ordinal:int,db:Session=Depends(get_db)):
    query=db.query(models.Bcs).filter(models.Bcs.ordinal==ordinal)
    print(query)
    if query.first()==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'{ordinal}th BCS not found')
    return query.first()

# update a bcs
@router.put("/{ordinal}",response_model=schemas.BcsOut)
async def update_bcs(ordinal:int,bcs:schemas.BcsUpdate , db:Session=Depends(get_db)):
    query=db.query(models.Bcs).filter(models.Bcs.ordinal==ordinal)
    to_update=query.first()
    if to_update==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'{ordinal}th BCS does not exist.')

    query.update(bcs.dict(),synchronize_session=False)
    db.commit()
    return query.first()

# delete a bcs
@router.delete("/{ordinal}")
async def delete_bcs(ordinal:int,
                    db:Session=Depends(get_db)):
    query=db.query(models.Bcs).filter(models.Bcs.ordinal==ordinal)
    to_delete=query.first()
    if to_delete==None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,
        detail=f'{ordinal}th BCS not found')
    
    query.delete()
    db.commit()

    return {"detail":"Removed successfully."}
























