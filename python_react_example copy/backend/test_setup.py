import os
from dotenv import load_dotenv
load_dotenv()

from app.models.product import Product

test_product = Product(
    id=1,
    name="Test Product",
    sku="TEST001",
    category="Test",
    price=99.99
)

print(test_product.model_dump_json())
