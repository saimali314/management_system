from fastapi import FastAPI, Depends
from fastapi.middleware.cors import CORSMiddleware
from models import Product
from database import session
import database_model
from database import engine
from sqlalchemy.orm import Session

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_methods=["*"]
)

database_model.Base.metadata.create_all(bind=engine)

@app.get("/")
def greet():
    return "Welcome to Saim World"

products = [
    Product(id=1, name="phone", description="budget phone", price=99, quantity=10),
    Product(id=2, name="laptop", description="gaming laptop", price=999, quantity=6)
]

def get_db():
    db = session()
    try:
        yield db
    finally:
        db.close()

def init_db():
    db = session()
    count = db.query(database_model.Product).count

    if count==0:
        for product in products:
            db.add(database_model.Product(**product.model_dump()))

        db.commit()

init_db()

@app.get("/products")
def get_all_products(db: Session = Depends(get_db)):
    # # db connection
    # # query
    db_products = db.query(database_model.Product).all()

    return db_products

@app.get("/products/{id}")
def get_product_by_id(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        return db_product

    # for product in products:
    #     if product.id == id:
    #         return product

    return "product not found"

@app.post("/products")
def add_product(product: Product, db: Session = Depends(get_db)):
    db.add(database_model.Product(**product.model_dump()))
    db.commit()
    # products.append(product)
    return product

@app.put("/products/{id}")
def update_product(id: int, product: Product, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db_product.name = product.name
        db_product.description = product.description
        db_product.price = product.price
        db_product.quantity = product.quantity
        db.commit()
        return "Product is updated"

    # for i in range(len(products)):
    #     if products[i].id == id:
    #         products[i] = product
    #         return "Product Added Successfully"
    else:
        return "No Product found"

@app.delete("/products/{id}")
def delete_product(id: int, db: Session = Depends(get_db)):
    db_product = db.query(database_model.Product).filter(database_model.Product.id == id).first()
    if db_product:
        db.delete(db_product)
        db.commit()
        return "Product is deleted "
    # for i in range(len(products)):
    #     if products[i].id == id:
    #         products.remove(products[i])
    #         return "Product Deleted Successfully"
    else:
        return "No Product found"
