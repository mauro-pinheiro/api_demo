from fastapi import FastAPI

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/demo/")
async def demo(media: float, perc_faltas: float, perc_disc_conc: float):
    return [
        {"class1": 0.01},
        {"class2": 0.09},
    ]