from pydantic import BaseModel

class TestModel(BaseModel):
    name: str

test = TestModel(name="test")
print(test.model_dump())

