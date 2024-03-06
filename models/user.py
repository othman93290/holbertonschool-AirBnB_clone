from base_model import BaseModel

class User(BaseModel):
    def __init__(self, username, email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.username = username
        self.email = email

    def to_dict(self):
        user_dict = super().to_dict()
        user_dict.update({
            'username': self.username,
            'email': self.email
        })
        return user_dict
