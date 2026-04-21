import os
import sys
import aiohttp
import asyncio


project_root= os.path.abspath( 
    os.path.join(os.path.dirname(__file__), '..', '..') )
sys.path.append(project_root)

from configurations.conf import Config
async def user_service(url,id,session):
    user_service_url = url + "/users"+"/"+str(id)
    print(f"User service URL: {user_service_url}")
    async with session.get(user_service_url) as response:
        if response.status == 200:
            user_data = await response.json()
            user_data={
                "id": user_data["id"],
                "name": user_data["name"],
                "email": user_data["email"]
            }
            return user_data
        else:
            print(f"Failed to fetch user data. Status code: {response.status}")
            return None
async def post_service(url,id,session):
    post_service_url = url + "/posts"+"/"+str(id)
    print(f"Post service URL: {post_service_url}")
    async with session.get(post_service_url) as response:
        if response.status == 200:
            post_data = await response.json()
            post_data={
                "id": post_data["id"],
                "title": post_data["title"],
                "body": post_data["body"]

            }
            return post_data
        else:
            print(f"Failed to fetch post data. Status code: {response.status}")
            return None
async def albums_service(url,id,session):
    albums_service_url = url + "/albums"+"/"+str(id)
    print(f"Albums service URL: {albums_service_url}")
    async with session.get(albums_service_url) as response:
        if response.status == 200:
            albums_data = await response.json()
            albums_data={
                "userId": albums_data["userId"],
                "id": albums_data["id"],
                "title": albums_data["title"]
            }
            return albums_data
        else:
            print(f"Failed to fetch albums data. Status code: {response.status}")
            return None
async def photos_service(url,id,session):
    photos_service_url = url + "/photos"+"/"+str(id)
    print(f"Photos service URL: {photos_service_url}")
    async with session.get(photos_service_url) as response:
        if response.status == 200:
            photos_data = await response.json()
            photos_data={
                "albumId": photos_data["albumId"],
                "id": photos_data["id"],
                "title": photos_data["title"],
                "url": photos_data["url"],
                "thumbnailUrl": photos_data["thumbnailUrl"]
            }
            return photos_data
        else:
            print(f"Failed to fetch photos data. Status code: {response.status}")
            return None
async def dashboard(url):
    async with aiohttp.ClientSession() as session:
        user_data, post_data, albums_data, photos_data = await asyncio.gather(
            user_service(url,1,session),
            post_service(url,1,session),
            albums_service(url,1,session),
            photos_service(url,1,session)
        )
        dashboard_data = { 
            "user": user_data,
            "post": post_data,
            "albums": albums_data,
            "photos": photos_data
        }
        return dashboard_data

if __name__ == "__main__":
    config = Config()
    print(config.url)
    result = asyncio.run(dashboard(config.url))
    print(result)
    
    try:
        asyncio.run(dashboard(config.url))
    except aiohttp.ClientError as e:
        print(f"HTTP error occurred: {e}")
    
    except Exception as e:
        print(f"An error occurred: {e}")



