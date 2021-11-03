from fastapi import FastAPI

app = FastAPI()

#デコレーター 直下の関数で処理する
#ルートページにアクセスされたとき，index()関数が呼び出される
#async: 非同期処理ができる
@app.get("/hello")
async def index():
    return {"message": "Hello World"}

#パスに入ってきた変数を元にページを表示できる
@app.get("/countries/{country_name}")
async def country(country_name: str):       #型ヒントで制限できる
    return {"country_name": country_name}

#クリエパラメータ
#http://127.0.0.1:8000/countries?country_name=USA&country_no=3
@app.get("/countries/")
async def country(country_name: str = 'japan', country_no: int = 1):
    return {
        "country_name": country_name,
        "country_no": country_no
    }

#パスパラメータとクリエパラメータの組み合わせ
@app.get("/countries/{country_name}")
async def country(country_name: str = 'japan', city_name: str = 'tokyo'):
    return {
        "country_name": country_name,
        "city_name": city_name
    }