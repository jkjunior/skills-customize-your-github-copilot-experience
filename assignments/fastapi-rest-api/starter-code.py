from fastapi import FastAPI
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

# Modelo de dados
class Item(BaseModel):
    id: int
    nome: str
    descricao: Optional[str] = None

# Lista para armazenar itens
itens: List[Item] = []

@app.post("/itens", response_model=Item)
def criar_item(item: Item):
    itens.append(item)
    return item

@app.get("/itens", response_model=List[Item])
def listar_itens():
    return itens

@app.get("/itens/{item_id}", response_model=Item)
def buscar_item(item_id: int):
    for item in itens:
        if item.id == item_id:
            return item
    return {"error": "Item não encontrado"}

# Para rodar: uvicorn starter-code:app --reload
# Acesse a documentação automática em http://localhost:8000/docs
