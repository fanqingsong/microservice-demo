from fastapi import APIRouter, FastAPI
prefix ="/user/api"

app = FastAPI(title="User API", description="User API", version="0.1", openapi_url=f"{prefix}/openapi.json", docs_url=f"{prefix}/docs")

router = APIRouter()
app.include_router(router, prefix=prefix)

users = [
    {
        "username": "user1", "id": 1, "password": "123",
        "name": "User 1", "email": "a@gmail.com", "is_active": True
    },
    {
        "username": "user2", "id": 2, "password": "124",
        "name": "User 2", "email": "b@gmail.com", "is_active": True
    },
]


@router.get('/')
async def get_users():
    return users


@router.get('/{username}')
async def get_user(username: str):
    user = [user for user in users if user['username'] == username]
    return user[0]


@router.post('/')
async def create_user(user: dict):
    users.append(user)
    return user


@router.put('/{username}')
async def update_user(username: str, user: dict):
    for u in users:
        if u['username'] == username:
            u.update(user)
            return u
