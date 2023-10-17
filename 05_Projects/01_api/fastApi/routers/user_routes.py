from fastapi import APIRouter


class User():
    id: int
    name: str
    email: str
    password: str

    def __init__(self, id, name, email, password):
        self.id = id
        self.name = name
        self.email = email
        self.password = password

router = APIRouter(prefix="/users")

oneUser = User(1, "Bard", "bard@example.com", "password123")


users: list[User] = [{'id': 1, 'name': 'Bard', 'email': 'bard@example.com', 'password': 'password123'},
                     {'id': 2, 'name': 'Alice', 'email': 'alice@example.com',
                         'password': 'qwerty123'},
                     {'id': 3, 'name': 'Bob', 'email': 'bob@example.com',
                         'password': '123456'},
                     {'id': 4, 'name': 'Carol', 'email': 'carol@example.com', 'password': 'password123'}]


@router.get("/")
def get_users():
    return users


@router.get("/{user_id}")
def get_user(user_id):
    for user in users:
        if user["id"] == user_id:
            return user
        else:
            return "user not found"


@router.post("/")
def create_user(user: User):
    user["id"] = len(users) + 1
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
