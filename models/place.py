#!/usr/bin/python3
"""Module for Place class"""
from models.base_model import BaseModel


class Place(BaseModel):
    """
    Description:
        Class that defines place attributes.

    Attributes:
        city_id: city's id (empty string))
        user_id: user's id (empty string)
        name: place's name (empty string)
        description: place's description (empty string)
        number_rooms: number of rooms (integer)
        number_bathrooms: number of bathrooms (integer)
        max_guest: maximum number of guests (integer)
        price_by_night: price by night (integer)
        latitude: place's latitude (float)
        longitude: place's longitude (float)
        amenity_ids: list of amenity ids (empty list)
    """
    city_id = ""
    user_id = ""
    name = ""
    description = ""
    number_rooms = 0
    number_bathrooms = 0
    max_guest = 0
    price_by_night = 0
    latitude = 0.0
    longitude = 0.0
    amenity_ids = []