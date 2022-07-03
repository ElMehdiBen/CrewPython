from bson import ObjectId
from fastapi import APIRouter, Depends, HTTPException
from pydantic import BaseModel
from auth import main as auth
from talents import utils

class Talent(BaseModel):
    _id: str
    firstName: str
    lastName: str
    picture: str
    job: str
    location: str
    linkedin: str
    github: str
    twitter: str
    tags: list
    stage: str

#APIRouter creates path operations for user module
router = APIRouter(
    prefix = "/talents",
    tags = ["talents"],
    responses = { 404: { "description": "Not found"} },
)

@router.get("/health/")
def check_health():
    return { "message" : "talents API are OK !" }

@router.get("/getAll/")
def get_talents(username: str = Depends(auth.authenticate)):
    talents = utils.mongo_connect_talents()
    return [talent for talent in talents.find({},{'_id': 0})]

@router.post("/insertOne/")
def insert_talent(talent: Talent, username: str = Depends(auth.authenticate)):
    talents = utils.mongo_connect_talents()
    try:
        talents.insert_one(talent.dict())
    except Exception as e:
        raise HTTPException(status_code = 404, detail = "Error: " + str(e))
    return { "message" : "talent inserted" }
