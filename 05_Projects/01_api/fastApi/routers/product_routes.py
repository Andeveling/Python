from fastapi import APIRouter
router = APIRouter(prefix="/products")


class Product():
    id: int
    name: str
    description: str
    price: float
    stock: int

    def __init__(self, id, name, description, price, stock):
        self.id = id
        self.name = name
        self.description = description
        self.price = price
        self.stock = stock


products_list: list[Product] = [{'id': 1, 'name': 'Book', 'description': 'A book', 'price': 10.0, 'stock': 10},
                                {'id': 2, 'name': 'Pen', 'description': 'A pen',
                                    'price': 1.0, 'stock': 10},
                                {'id': 3, 'name': 'Pencil', 'description': 'A pencil',
                                    'price': 0.5, 'stock': 10},
                                {'id': 4, 'name': 'Eraser', 'description': 'An eraser', 'price': 1.5, 'stock': 10},]


@router.get("/")
def get_products():
    return products_list


@router.get("/{product_id}")
def get_product(product_id: int):
    for product in products_list:
        if product["id"] == product_id:
            return product
        else:
            return "product not found"


@router.post("/")
def create_product(product: Product):
    product["id"] = len(products_list) + 1
    products_list.append(product)
    return product


@router.put("/{product_id}")
def update_product(product_id: int, name: str):
    for product in products_list:
        if product["id"] == product_id:
            product["name"] = name
            return product
        else:
            return "product not found"


@router.delete("/{product_id}")
def delete_product(product_id: int):
    for product in products_list:
        if product["id"] == product_id:
            products_list.remove(product)
            return product
        else:
            return "product not found"
