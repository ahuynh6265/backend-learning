from fastapi import FastAPI, HTTPException, status
from pydantic import BaseModel, Field, computed_field
from typing import Optional 

app = FastAPI()

class Products(BaseModel):
  id: int = Field(gt=0, description="Must be a positive value")
  name: str = Field(min_length=1, max_length=100, description="Name is required")
  price: float = Field(gt=0, description="Price can't be a negative value")
  stock: int = Field(ge=0, description="Stock can't be a negative value")

  @computed_field
  @property
  def in_stock(self) -> bool: 
    return self.stock > 0 
  
  @computed_field 
  @property
  def total_value(self) -> float: 
    return round((self.price * self.stock),2)
  

products =[
  Products(id=1, name="Laptop",price=999.99, stock=15),
  Products(id=2, name="Phone",price=259.99, stock=10),
  Products(id=3, name="Computer",price=1279.49, stock=5),
  Products(id=4, name="Tablet",price=349.49, stock=0),
]

@app.get("/products")
def get_products(): return products

@app.get("/products/search")
def search_product(
  name: Optional[str] = None,
  min_price: Optional[float] = None,
  max_price: Optional[float] = None
):
  results = products

  if name:
    results = [p for p in results if name.lower() in p.name.lower()] 
  
  if min_price: 
    results = [p for p in results if min_price <= p.price]
  
  if max_price:
    results = [p for p in results if p.price <= max_price]

  return{
    "count": len(results),
    "products": results
  }

@app.get("/products/{product_id}")
def get_product(product_id: int):
  for product in products:
    if product_id == product.id:
      return product
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product ID not found.")

@app.post("/products", status_code=status.HTTP_201_CREATED)
def create_product(new_product: Products):
  for product in products:
    if product.id == new_product.id:
      raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"ID {new_product.id} is already assigned to {product.name}.")
  
  products.append(new_product)
  return {"message": "New Product Added", "product": new_product}

@app.put("/products/{product_id}")
def update_product(product_id: int, new_product: Products):
  if product_id != new_product.id: 
    raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail=f"URL ID {product_id} does not match Body {new_product.id}")
  
  for i, product in enumerate(products): 
    if product.id == product_id:
      products[i] = new_product 
      return {"message": "product updated", "product": new_product}
  
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product ID not found")

@app.delete("/products/{product_id}", status_code=status.HTTP_204_NO_CONTENT)
def delete_product(product_id: int):
  for i, product in enumerate(products):
    if product_id == product.id:
      products.pop(i)
      return
  raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="Product ID not found")





  

