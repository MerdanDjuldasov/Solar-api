from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI()

saqlangan = []


class Olchov(BaseModel):
    panel_id: int
    quvvat_vt: float


@app.post("/quvvat")
def qabul_qil(data: Olchov):
    saqlangan.append(data)
    return {"qabul_qilindi": True}


@app.get("/quvvat")
def hammasi():
    return saqlangan