from dataclasses import dataclass
from .customer import Customer
from .product import Product

@dataclass
class ProductReview:
    rating: int
    review: str
    product: Product
    reviewer: Customer
