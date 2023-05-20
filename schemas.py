from pydantic import BaseModel


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
