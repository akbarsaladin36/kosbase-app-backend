from passlib.context import CryptContext
from uuid import uuid4
from bcrypt import gensalt, hashpw, checkpw
from random import randint
from datetime import datetime

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

def generate_hash_password(password: str) -> str:
    password_encode = password.encode("utf-8")
    salt = gensalt()
    hashed_password = hashpw(password_encode, salt)
    return hashed_password.decode("utf-8")

def verify_hash_password(plain_password: str, hashed_password: str) -> bool:
    encode_plain_password = plain_password.encode("utf-8")
    encode_hashed_password = hashed_password.encode("utf-8")
    return checkpw(encode_plain_password, encode_hashed_password)

def generate_uuid() -> str:
    return uuid4().hex

def generate_code(code: str) -> str:
    now = datetime.now()
    formatted_date = now.strftime("%Y%m%d")
    return f"{code}-{randint(1000, 9999999)}-{formatted_date}"