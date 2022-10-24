from pydoc_data.topics import topics
from .database import LocalSession,engine
from fastapi import FastAPI,Request,Response
from . import models
from .routers import users,bcs,questions,topics,bcs_questions
from fastapi.middleware.cors import CORSMiddleware


# disabled for Alembic
# models.Base.metadata.create_all(bind=engine)

app=FastAPI()

origins = ["*"]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(topics.router)
app.include_router(bcs.router)
app.include_router(bcs_questions.router)
# app.include_router(questions.router)

app.include_router(users.router)
# app.include_router(posts.router)
# app.include_router(votes.router)

@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Internal server error", status_code=500)
    try:
        request.state.db = LocalSession()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


@app.get("/")
def index():
    return {"Home":"Welcome every body. Peace be upon you.This is a question bank app."}



