from app.configs.database import db
from werkzeug.security import generate_password_hash, check_password_hash
from sqlalchemy import Column, Integer, String, Boolean


class UserModel(db.Model):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)

    login = Column(String(50), nullable=False)
    is_admin = Column(Boolean, default=False)

    password_hash = Column(String)


    @property
    def password(self):
        raise AttributeError("Password cannot be accessed!")

    @password.setter
    def password(self, password_to_hash):
        self.password_hash = generate_password_hash(password_to_hash)


    def check_password(self, password_to_compare):
        return check_password_hash(self.password_hash, password_to_compare)
