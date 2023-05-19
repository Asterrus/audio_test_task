from sqlalchemy.orm import Mapped, mapped_column, DeclarativeBase


class Base(DeclarativeBase):
    id: Mapped[int] = mapped_column(primary_key=True, index=True)


class User(Base):
    __tablename__ = 'user'

    name: Mapped[str]
    unique_slug: Mapped[str]
    UUID: Mapped[str]

    def __repr__(self) -> str:
        return f'User(id={self.id!r}, name={self.name!r})'


class Audio(Base):
    __tablename__ = 'audio'

    UUID: Mapped[str]
    user_UUID: Mapped[str]
    file_path: Mapped[str]

    def __repr__(self) -> str:
        return f'AudioFile(id={self.id!r}, url={self.file_path!r})'
