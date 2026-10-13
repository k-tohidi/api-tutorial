"""
zia tohidi
"""
import random

import uvicorn
from fastapi import FastAPI

app = FastAPI()

@app.get("/random")
def get_random():
    random_number = random.randint(0, 100000)
    print("the random is:", random_number)
    return random_number


@app.post("/to-be-printed")
def printer(message: str):
    print(message)
    return None


# api 
# اول برای این است که
# سوال کاربر را بگیریم
# به او ۲ جواب مختلف بدهیم
# به علاوه یک آیدی که آن آیدی برای مقایسه کردن استفاده خواهد شد


# ۲
# برای این است که کاربر به ما بگوید از ۲ پاسخی که به او دادیم کدامیک بهتر بود
# پاسخ ها با آیدی که در ای پی آی قبلی به کاربر دادیم شناسایی میشوند.
# برای ذخیره سازی دادگان از یک فایل txt استفاده میکنیم


# ۳
# از آن فایل txt که نوشتیم و نتایج در آن ذخیره شده است
# استفاده میکنیم و نتایج را به کاربر نشان میدهیم



if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
