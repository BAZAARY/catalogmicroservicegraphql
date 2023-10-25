from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from ariadne.asgi import GraphQL
from api.graphql.routes import schema


app = FastAPI()

origins = [
    "*",
    "http://localhost:8000",
    "http://localhost:3000",
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Create the GraphQL app
graphql_app = GraphQL(schema, debug=True)

app.add_route("/graphql", graphql_app)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)