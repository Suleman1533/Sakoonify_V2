import sqlite3

from datetime import datetime, timedelta

from fastapi import FastAPI, HTTPException, Depends
from fastapi.security import OAuth2PasswordBearer

from jose import jwt

from passlib.context import CryptContext

from pydantic import BaseModel


# --------------------------------
# 1. Configuration
# --------------------------------

SECRET_KEY = "sakoonify-development-secret"

ALGORITHM = "HS256"

ACCESS_TOKEN_EXPIRE_MINUTES = 30


# --------------------------------
# 2. Password hashing
# --------------------------------

pwd_context = CryptContext(
    schemes=["bcrypt"],
    deprecated="auto"
)


# --------------------------------
# 3. OAuth2 token configuration
# --------------------------------

oauth2_scheme = OAuth2PasswordBearer(
    tokenUrl="/login"
)


# --------------------------------
# 4. FastAPI
# --------------------------------

app = FastAPI()


# --------------------------------
# 5. Request models
# --------------------------------

class RegisterRequest(BaseModel):
    username: str
    password: str


class LoginRequest(BaseModel):
    username: str
    password: str


# --------------------------------
# 6. Database initialization
# --------------------------------

def init_db():

    conn = sqlite3.connect("sakoonify.db")

    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username TEXT UNIQUE NOT NULL,
            password_hash TEXT NOT NULL
        )
    """)

    conn.commit()

    conn.close()


# --------------------------------
# 7. Hash password
# --------------------------------

def hash_password(password):

    return pwd_context.hash(password)


# --------------------------------
# 8. Verify password
# --------------------------------

def verify_password(password, password_hash):

    return pwd_context.verify(
        password,
        password_hash
    )


# --------------------------------
# 9. Create JWT
# --------------------------------

def create_access_token(username):

    expire = datetime.utcnow() + timedelta(
        minutes=ACCESS_TOKEN_EXPIRE_MINUTES
    )

    payload = {
        "sub": username,
        "exp": expire
    }

    token = jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )

    return token


# --------------------------------
# 10. Register
# --------------------------------

@app.post("/register")
def register(request: RegisterRequest):

    password_hash = hash_password(
        request.password
    )

    conn = sqlite3.connect("sakoonify.db")

    cursor = conn.cursor()

    try:

        cursor.execute(
            """
            INSERT INTO users (username, password_hash)
            VALUES (?, ?)
            """,
            (
                request.username,
                password_hash
            )
        )

        conn.commit()

    except sqlite3.IntegrityError:

        conn.close()

        raise HTTPException(
            status_code=400,
            detail="Username already exists"
        )

    conn.close()

    return {
        "message": "User registered successfully"
    }


# --------------------------------
# 11. Login
# --------------------------------

@app.post("/login")
def login(request: LoginRequest):

    conn = sqlite3.connect("sakoonify.db")

    cursor = conn.cursor()

    cursor.execute(
        """
        SELECT username, password_hash
        FROM users
        WHERE username = ?
        """,
        (request.username,)
    )

    user = cursor.fetchone()

    conn.close()

    if not user:

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    username, password_hash = user

    if not verify_password(
        request.password,
        password_hash
    ):

        raise HTTPException(
            status_code=401,
            detail="Invalid username or password"
        )

    token = create_access_token(
        username
    )

    return {
        "access_token": token,
        "token_type": "bearer"
    }


# --------------------------------
# 12. Protected endpoint
# --------------------------------

@app.get("/protected")
def protected(
    token: str = Depends(oauth2_scheme)
):

    try:

        payload = jwt.decode(
            token,
            SECRET_KEY,
            algorithms=[ALGORITHM]
        )

        username = payload.get("sub")

        if not username:
            raise HTTPException(
                status_code=401,
                detail="Invalid token"
            )

    except Exception:

        raise HTTPException(
            status_code=401,
            detail="Invalid or expired token"
        )

    return {
        "message": "You are authenticated",
        "username": username
    }


# --------------------------------
# 13. Initialize database
# --------------------------------

init_db()