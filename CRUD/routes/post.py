from pydantic import BaseModel,EmailStr
from fastapi import status,APIRouter,HTTPException
from datetime import datetime
from database import get_database
from models.contact_form import contact_form

router = APIRouter()


class UserBase(BaseModel):
    id: int
    name: str
    mobile: str
    email: EmailStr
    message: str
    created_date: datetime


class UserType(UserBase):
    browser_type: str


@router.post("/contact_form", status_code=status.HTTP_201_CREATED)
async def register(user: UserType):
    try:
        db = get_database()
        insert_query = contact_form.insert().values(id=user.id,
                                                    name=user.name,
                                                    mobile=user.mobile,
                                                    email=user.email,
                                                    message=user.message,
                                                    created_date=user.created_date,
                                                    browser_type=user.browser_type
                                                    )

        await db.execute(insert_query)
        #print(insert_query)
    except Exception as e:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail='enter valid details')
