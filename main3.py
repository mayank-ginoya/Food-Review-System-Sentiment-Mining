# 1 . Library Required

import uvicorn
from fastapi import FastAPI
from Review import UserReview 
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# 2 . Create Object
app = FastAPI()
sid=SentimentIntensityAnalyzer()

# 3 . Index Route , Opens Automatically on server
@app.get('/')
async def index():
    return {'message':"Hello ,Welcome to Food Review System "}

# 4 . Single parameter
@app.get('/item/{name}')
async def get_name(name:str):
    return {'name': name}

@app.post('/predict')
async def predict_senti(data:UserReview):
    data=data.dict()
    i=data['review']
    prediction = sid.polarity_scores(i)
    print(prediction)
    prediction=prediction["compound"]
    if prediction > 0:
        return "Positive Review"
    else:
        return "Negative Review"


# 5 . Run The API with uvicorn
#   Will run on the Server 

if __name__ == '__main__':
    uvicorn.run(app,host="127.0.0.1",port=8000)

#uvicorn main:app --reload
