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
    type Subscription{
        deliverMessage: String!
    }
""")
from broadcaster import Broadcast
broadcast = Broadcast("memory://")

#region Mutation
mutation = MutationType()

#@mutation.field("setMessage")
async def resolve_set_message(obj, info, text):
    await broadcast.publish(channel="chatroom", message=text)
    return True
mutation.set_field("setMessage", resolve_set_message)
#end region

#region subscription
subscription = SubscriptionType()

#@subscription.field("deliverMessage")
#resolver
def resolve_deliver_message(obj, info):
    return obj
subscription.set_field("deliverMessage", resolve_deliver_message)
#end region

#source
#@subscription.source("deliverMessage")
async def source_deliver_message(obj, info):

    async with broadcast.subscribe(channel="chatroom") as subscriber:
        async for event in subscriber:
                yield event.message
subscription.set_source("deliverMessage", source_deliver_message)
#end region

schema = make_executable_schema(type_defs, mutation, subscription)

graph_app = GraphQL(schema)

app = FastAPI(on_startup=[broadcast.connect], on_shutdown=[broadcast.disconnect])
app.mount("/", graph_app)
#add web socket
app.add_websocket_route('/', graph_app)