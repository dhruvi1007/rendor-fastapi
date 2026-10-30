from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def home():
    return{
        "Message": "Hello from FastAPI on Render..."
    }

@app.get("/users")
def get_users():
    return[
        {
            "name": "Dhruvi",
            "Role": "Admin"
        },
        {
            "name": "Gopi",
            "Role": "Employee"
        }
    ]

@app.get("/contact")
def home():
    return{
        "Message": "Contact Page"
    }

app.get("/About")
