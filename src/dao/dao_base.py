import os
import asyncio
import asyncpg
from dotenv import load_dotenv
from pydantic import BaseModel
from pydantic_settings import BaseSettings


class EnvironmentSettings(BaseSettings):
    class Config:
        env_file = "config.local.env"
        extra = "ignore"

    host: str
    username: str
    password: str
    database: str
    port: str


settings = EnvironmentSettings()


class TableFindLens:
    async def __aenter__(self):
        try:
            self.conn = await asyncpg.connect(
                host=settings.host,
                user=settings.username,
                database=settings.database,
                password=settings.password,
                port=settings.port,
            )
            return self
        except Exception as e:
            raise RuntimeError(str(e))

    async def __aexit__(self, *args):
        await asyncio.gather(self.conn.close(timeout=10), return_exceptions=True)

    def __await__(self):
        return self.__aenter__().__await__()
