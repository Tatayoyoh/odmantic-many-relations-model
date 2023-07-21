MONGO_URL = 'mongodb://odmantic-relation-example-mongo:27017/'
MONGO_DB = 'odmantic_example'

# SYNC client / engine
from pymongo import MongoClient
from odmantic import SyncEngine
sync_client = MongoClient(MONGO_URL)
sync_engine = SyncEngine(client=sync_client, database=MONGO_DB)

# ASYNC client / engine
from motor.motor_asyncio import AsyncIOMotorClient
from odmantic import AIOEngine
async_client = AsyncIOMotorClient(MONGO_URL)
async_engine = AIOEngine(client=async_client, database=MONGO_DB)
