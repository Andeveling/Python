from fastapi import APIRouter


router = APIRouter(prefix="/products")

products_list = [{"id": 1, "name": "Product 1"}, {"id": 2, "name": "Product 2"}, {
    "id": 3, "name": "Product 3"
}, {"id": 4, "name": "Product 4"}]


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
def create_product(name: str):
    product = {"id": len(products_list) + 1, "name": name}
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
