from models.base_model import BaseModel

class User(BaseModel):
    def __init__(self, username, email, full_name, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = username
        self.email = email
        self.full_name = full_name

    def greet(self):
        return f"Hello, {self.full_name}!"

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict.update({
            'username': self.username,
            'email': self.email,
            'full_name': self.full_name
        })
        return user_dict
