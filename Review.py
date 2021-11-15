# -*- coding: utf-8 -*-
"""
Created on Sat Feb 27 23:10:39 2021

@author: KHODIYAR
"""


from pydantic import BaseModel
from flask import request

# 2. Class which describes Review 
class UserReview(BaseModel):
    review :str

