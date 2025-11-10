import asyncio
import time
import uuid
from fastapi import APIRouter, HTTPException, Request
from pydantic import BaseModel, Field

from calyx.vectordb.vectordb import VectorDB
from calyx.config import settings
from calyx.logging import logger

router = APIRouter(prefix="/v1/search", tags=["vectordb"])

db = VectorDB()
db.load(settings.db_config.db_name)

class SearchRequest(BaseModel):
    question: str = Field(..., example="Give me movie list about intergalactic wars")
    top_k: int =  Field(..., example=3)

class SearchResponse(BaseModel):
    result: list
    latency_ms: int


@router.post("/search", response_model=SearchResponse)
def perform_search(req:Request, payload: SearchRequest):
    search_id = str(uuid.uuid4())
    start = time.perf_counter()

    try:
        result = db.search(query=payload.question,
                           top_k=payload.top_k)
        latency_ms = int((time.perf_counter() - start) * 1000)
        logger.info("Search success", extra={"search_id": search_id})

        return SearchResponse(
            result=result,
            latency_ms=latency_ms
        )

    except Exception as e:
        latency_ms = int((time.perf_counter() - start) * 1000)
        logger.error("Search failed", extra={"search_id": search_id})
        raise HTTPException(
            status_code=500,
            detail={"message": "Search failed", "error": str(e), "search_id": search_id},
        )
