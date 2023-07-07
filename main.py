from typing import List
from datetime import timedelta
from fastapi import FastAPI, status
from fastapi.middleware.cors import CORSMiddleware

from dbconnection import pdatabase, sources
from schema import Source, SourceIn, TimeSourceIn

app = FastAPI(title = "REST API using FastAPI PostgreSQL Async EndPoints")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.on_event("startup")
async def startup():
    await pdatabase.connect()

@app.on_event("shutdown")
async def shutdown():
    await pdatabase.disconnect()

@app.get('/api/health')
def root():
    return {'message': 'Hello World'}

@app.get("/get_data/", response_model=List[Source], status_code = status.HTTP_200_OK)
async def read_sources(offset: int = 0, limit: int = 20):
    query = sources.select().offset(offset).limit(limit)
    return await pdatabase.fetch_all(query)

@app.get("/get_data/{source_id}/", response_model=Source, status_code = status.HTTP_200_OK)
async def read_sources(source_id: int):
    query = sources.select().where(sources.c.source_id == source_id)
    return await pdatabase.fetch_one(query)

@app.get("/get_data_trigger/{source_id}/", response_model=Source, status_code = status.HTTP_200_OK)
async def read_sources(source_id: int):
    query = sources.select().where(sources.c.source_id == source_id)
    result = await pdatabase.fetch_one(query)
    result = dict(result)
    frequency = int(result["frequency"][:-1])
    result["from_date"] = result["from_date"] + timedelta(minutes=frequency)
    result["to_date"] = result["to_date"] + timedelta(minutes=frequency)
    return result

@app.post("/add_data/", status_code = status.HTTP_201_CREATED)
async def create_source(source: SourceIn):
    query = sources.insert().values(source.dict())
    last_record_id = await pdatabase.execute(query)
    return {"status": "success"}
    # return {**source.dict(), "source_id": last_record_id}

@app.put("/update_data/{source_id}/", response_model=Source, status_code = status.HTTP_200_OK)
async def update_source(source_id: int, payload: SourceIn):
    query = sources.update().where(sources.c.source_id == source_id).values(payload.dict())
    await pdatabase.execute(query)
    return {**payload.dict(), "source_id": source_id}

@app.patch("/update_data/{source_id}/", status_code = status.HTTP_200_OK)
async def update_source(source_id: int, payload: TimeSourceIn):
    payload_dict = {k:v for k, v in payload.dict().items() if v is not None}
    query = sources.update().where(sources.c.source_id == source_id).values(payload_dict)
    await pdatabase.execute(query)
    return {"status": "success"}
    # query = sources.select().where(sources.c.source_id == source_id)
    # return await pdatabase.fetch_one(query)

@app.delete("/delete_data/{source_id}/", status_code = status.HTTP_200_OK)
async def delete_source(source_id: int):
    query = sources.delete().where(sources.c.source_id == source_id)
    await pdatabase.execute(query)
    return {"message": f"Source with id: {source_id} deleted successfully!"}