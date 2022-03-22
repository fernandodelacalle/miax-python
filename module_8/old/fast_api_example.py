from fastapi import APIRouter, HTTPException
from fastapi import FastAPI

router = APIRouter()

@router.get("/mi_primer_get",
            summary='summary')
def ingest_data_gcloud(competi: str):
    print(competi)
    return competi

app = FastAPI(
    title='mIA-X API',
    description='mIA-X API',
    version='0.0.1',
)

app.include_router(
    router,
)