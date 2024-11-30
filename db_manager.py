import random
import motor.motor_asyncio
import asyncio
from rnd_img import get_img_with_descr
from config import DB_URL


async def connect_to_db() -> motor.motor_asyncio.AsyncIOMotorCollection:
    client = motor.motor_asyncio.AsyncIOMotorClient(DB_URL)
    database = client["datamini"]
    return database["Questions"]


async def get_some(
    collection: motor.motor_asyncio.AsyncIOMotorCollection, samples: int = 1):
    async for doc in collection.aggregate([
            {'$sample':
                {'size': samples}}
            ]):
        return doc  # TODO:


async def fill_db(
    collection: motor.motor_asyncio.AsyncIOMotorCollection, items: int = 5):
    for _ in range(items):
        doc = await get_img_with_descr()
        doc['rnd'] = random.random()
        await collection.insert_one(doc)


if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    collection = loop.run_until_complete(connect_to_db())

    # Get a random document from the collection
    random_fact = loop.run_until_complete(get_some(collection))
    print(random_fact)

    # Fill the database with 10 documents
    loop.run_until_complete(fill_db(collection))
