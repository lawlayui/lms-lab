from .models import create_user, read_user
from app.utils.security import generate_hash, generate_jwt, verify_hash

def user_register(username: str, password: str, role: str):
    username = username.strip()
    password = password.strip()
    password = generate_hash(password)
    role = role.strip()

    if read_user(username=username):
        raise ValueError("Account already registered")

    user_id = create_user(username,password,role)
    role = read_user(user_id)['role']
    data = {'user_id':user_id,'role':role}
    token = generate_jwt(data)
    return token

def user_login(username: str, password: str):
    username = username.strip()
    password = password.strip()
    result = read_user(username=username)
    password_hash = result['password']

    if not result:
        raise ValueError("Account not found")

    if verify_hash(password,password_hash):
        data = {'user_id':result['id'],'role':result['role']}
        token = generate_jwt(data)
        return token 
    
    raise ValueError("Invalid Password")


        
