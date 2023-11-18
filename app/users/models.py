from app.database import Base
from sqlalchemy import Column, Integer, String, Boolean, JSON, ForeignKey, Date, Computed
from sqlalchemy.orm import relationship, Mapped, mapped_column



class Users(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(primary_key=True)
    email: Mapped[str]
    hashed_password: Mapped[str]

    bookings: Mapped[list["Bookings"]] = relationship(back_populates="user")

    def __str__(self):
        return f" Пользователь {self.email}"

    