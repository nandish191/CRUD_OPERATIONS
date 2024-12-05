from fastapi import FastAPI
from models.contact_form import metadata
from database import Database
import sqlalchemy
from database import sqlalchemy_engine
from routes.post import router as post_router
from routes.get import router as get_router


app = FastAPI()


DATABASE_URL = "sqlite:///contact_form.db"
database = Database(DATABASE_URL)
sqlalchemy_engine = sqlalchemy.create_engine(DATABASE_URL)


@app.on_event("startup")
async def startup():
    await database.connect()
    metadata.create_all(sqlalchemy_engine)


@app.on_event("shutdown")
async def shutdown():
    await database.disconnect()


metadata.create_all(sqlalchemy_engine)
app.include_router(post_router)
app.include_router(get_router)