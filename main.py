import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from router import artists, comment, user, like
from db import models
from db.database import engine


app = FastAPI(
    title="Article API",
    description="This API was developed for teaching Fast API",
    version="0.0.1",
    terms_of_service="http://localhost:5000",
)
app.include_router(artists.router)
app.include_router(user.router)
app.include_router(like.router)
app.include_router(comment.router)

# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    uvicorn.run("main:app", port=5000, reload=True)


origins = [
    'http://127.0.0.1:5173',
    "*",
 
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=['*']
)

models.Base.metadata.create_all(engine)
