import os
import uvicorn 


from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.agent.langgraph_agent import initialize_graph, close_graph
from app.db.session import async_engine
from app.db.base import Base
from app.utils.logger import setup_logger
from app.core.config import settings
from app.api.api import api_router

logger = setup_logger(__name__)
async def lifespan(app: FastAPI):
    await initialize_graph()
    async with async_engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)   
    
    logger.info(f"LANGCHAIN_TRACING_V2: {os.getenv('LANGCHAIN_TRACING_V2')}")
    logger.info(f"LANGSMITH_PROJECT: {os.getenv('LANGSMITH_PROJECT')}")


    yield

    await async_engine.dispose()
    await close_graph()


app = FastAPI(
    title = settings.PROJECT_NAME,
    openai_url = f"{settings.API_V1_STR}/openapi.json",
    lifespan = lifespan,
)

if settings.BACKEND_CORS_ORIGINS:
    app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

app.include_router(api_router, prefix =settings.API_V1_STR)
if __name__ == "__main__":
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True)