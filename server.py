from ariadne import (
    gql,
    make_executable_schema,
    SubscriptionType,
    MutationType,
)

from ariadne.asgi import GraphQL
from fastapi import FastAPI

type_defs = gql("""
    type Query{
        get: Boolean!
}
    type Mutation{
        setMessage(text: String!): Boolean!
}
""")

#region Mutation
#defined mutation
mutation = MutationType()

#@mutation.field("setMessage") instend mutation.set_field("setMessage", resolve_set_message)
def resolve_set_message(obj, info, text):
    return True
mutation.set_field("setMessage", resolve_set_message)
#end region


schema = make_executable_schema(type_defs, mutation)

graph_app = GraphQL(schema)

app = FastAPI()
app.mount("/", graph_app)
#add web socket
app.add_websocket_route('/', graph_app)