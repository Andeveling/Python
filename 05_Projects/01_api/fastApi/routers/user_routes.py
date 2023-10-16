from fastapi import APIRouter

router = APIRouter(prefix="/users")

users = [{"id": 1, "name": "User 1"}, {"id": 2, "name": "User 2"}]


@router.get("/")
def get_users():
    return 'all users'


@router.get("/{user_id}")
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
        else:
            return "user not found"


@router.post("/")
def create_user(name):
    user = {"id": len(users) + 1, "name": name}
    users.append(user)
    return user


@router.put("/{user_id}")
def update_user(user_id, name):
    for user in users:
        if user["id"] == user_id:
            user["name"] = name
            return user
        else:
            return "user not found"


@router.delete("/{user_id}")
def delete_user(user_id):
    for user in users:
        if user["id"] == user_id:
            users.remove(user)
            return user
        else:
            return "user not found"
