"""Database functions"""

import os

from dotenv import load_dotenv
from fastapi import APIRouter, Depends
import sqlalchemy
from app.predict_json import predict_2021
from app.city_state_json import city_state_2_id_num


router = APIRouter()


@router.get('/state_id')
async def return_city_state(city_state: str):
    '''Returns the state_id

        for a given city_state, i.e., "Newark, New Jersey"    
    
        {"Newark, New Jersey" : 18127 }
                
    '''
    return {"id_num" : city_state_2_id_num[city_state]}


@router.get('/predict')
async def predict_city_state(city_state: str):
    '''Returns the predicted values for a given state

        for a given city_state, i.e., "Newark, New Jersey"    
    
        {
        "id_num": 17089,

        "population": 283945,

        "crime_rate": 27.4,

        "rental_rate": 1466.89,
        
        "walk_score": 79
        }
                
    '''
    return predict_2021[city_state]

