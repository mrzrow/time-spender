import uvicorn

from contextlib import asynccontextmanager
from fastapi import FastAPI

from backend.api import router
from backend.core.models import db_helper, Base


@asynccontextmanager
async def lifespan(_app: FastAPI):
    async with db_helper.engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)
    yield


app = FastAPI(title='TimeSpender', lifespan=lifespan)
app.include_router(router=router)

if __name__ == "__main__":
    uvicorn.run(app)
