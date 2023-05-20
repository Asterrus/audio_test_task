from pydantic import BaseModel

# User
class UserBase(BaseModel):
    name: str


class UserSecrets(BaseModel):
    unique_slug: str
    UUID: str


class UserSecretsOut(UserSecrets):

    class Config:
        orm_mode = True


class UserCreate(UserBase):
    pass


class User(UserBase, UserSecrets):
    id: int

    class Config:
        orm_mode = True

# Audio
class AudioBase(BaseModel):
    UUID: str
    user_UUID: str

class Audio(AudioBase):
    id: int
    file_path: str

    class Config:
        orm_mode = True