from fastAPI import FastAPI

app = FastAPI(
    title="SUS - Sistema Único de Saúde API",
    description="API para gerenciamento de dados do Sistema Único de Saúde (SUS)",
    version="1.0.0"
)

@app.get("/")
def read_root():
    return {"message": "Welcome to the SUS API"}