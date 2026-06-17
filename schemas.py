from pydantic import BaseModel,ConfigDict
from typing import Optional

class SignUpModel(BaseModel):
    id:Optional[int]=None
    username:str
    email:str
    password:str
    is_staff:Optional[bool]=False
    is_active:Optional[bool]=True

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "username": "johndoe",
                "email": "johndoe@gmail.com",
                "password": "password",
                "is_staff": False,
                "is_active": True
            }
        }
    )

class Settings(BaseModel):
    authjwt_secret_key:str='82c3c082c458248ef2c7538059f3fc0db6d485c77d599f2d3574b36ecdf58c06'

class LoginModule(BaseModel):
    username:str
    password:str

class OrderModel(BaseModel):
    id:Optional[int]=None
    quantity:int
    order_status:Optional[str]="PENDING"
    pizza_size:Optional[str]="SMALL"
    user_id:Optional[int]

    model_config = ConfigDict(
        from_attributes=True,
        json_schema_extra={
            "example": {
                "quantity": 2,
                "pizza_size":"LARGE"
            }
        }
    )