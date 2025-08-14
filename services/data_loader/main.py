from fastapi import FastAPI

from services.data_loader.dataLoader import ConnectionWrapper
from services.data_loader.queries import Queries

app = FastAPI()

queries=Queries()
@app.get("/")
def get():
   return queries.getAll()