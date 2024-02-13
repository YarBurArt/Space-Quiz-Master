""" 
Module for async retrieving a random image with description from the other API.
"""
import json
import asyncio
import aiohttp 


URL = 'https://api.nasa.gov/planetary/apod?api_key=DEMO_KEY&count=1'


async def get_img_with_descr():
    """
    Retrieves an image with description from the NASA API using aiohttp.
    Returns:
        dict: date, explanation, hdurl (better quality)
              mediatype (video/image), title, url
    """
    async with aiohttp.ClientSession() as session:
        is_image = False
        while not is_image:
            async with session.get(URL) as res:
                resj = await res.json()
                is_image = resj[0]['media_type'] == 'image'

    if resj is None:
        return {'date': '1995-08-12', 'explanation': 'the shuttles land' 
                'on are among the longest in the world.', 
                'hdurl': 'https://nasa.gov/', 
                'media_type': 'image', 'service_version': 'v1', 
                'title': 'Atlantis Landing', 'url': 'https://apod.nasa.gov/'}
    return resj[0]


if __name__ == '__main__':
    result = asyncio.run(get_img_with_descr())
    print(json.dumps(result, indent=4))

