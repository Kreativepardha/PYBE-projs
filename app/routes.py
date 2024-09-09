from fastapi import APIRouter, Depends, HTTPExceptions, status
from app.models import UserCreate, UserLogin, PostCreate
from prisma import Prisma

router = APIRouter()
db = Prisma()

@router.post("/signup")
async def signup(user_data: UserCreate):
    user = await db.user.find_unique(where={"email": user_data/email})
    if user: 
        raise HTTPException(status_code=400, detail="email already regsitered")

    await db.user.create(data={"email": user_data.email, "password":user_data.password})
    return {"msg": "user created Succesffully"}

@router.post("/login")
async def signup():
    user = await db.user.find_unique(where={"email": user_data/email})
    if user: 

    return {"msg": "user Logged in Succesffully"}

