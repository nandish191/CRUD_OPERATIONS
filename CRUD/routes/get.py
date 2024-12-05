from models.contact_form import contact_form
from database import get_database
from fastapi import APIRouter

router = APIRouter()


@router.get("/person-data")
async def retrieve_info():
    select_stmt = contact_form.select()
    result = await get_database().fetch_all(select_stmt)
    return result


@router.get("/individual_data")
async def retrieve_mentee_info(mobile: str):
    db = get_database()
    select_query = contact_form.select().where(contact_form.c.mobile == mobile)
    result = await db.fetch_one(select_query)
    #print(result)
    return result