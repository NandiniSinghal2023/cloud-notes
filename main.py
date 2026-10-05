from fastapi import FastAPI 

app = FastAPI()

notes = [
    "ABC", "DEF"
]

@app.get("/")
def home():
    return {"message" : "Cloud notes API is running!"}

@app.get("/notes")
def get_notes():
    return{"notes":notes}

@app.post("/notes")
def add_note(note:str):
    notes.append(note)
    return{
        "message" : "note added", 
        "note" : note
    }
