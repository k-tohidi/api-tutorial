¨¨¨
zia tohidi
¨¨¨
import random
form Fastapi import FastAPI

app = FastAPI()

@app.get("/random")
def get_random():
    return random.randint(0, 100000)
