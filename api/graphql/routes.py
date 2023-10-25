from ariadne import ObjectType, QueryType, make_executable_schema
from api.helpers.helpers import get_products_ids, get_product_name_and_price_with_id, get_image_a_id_with_product_id

type_defs = """
    type Query {
        hello: String!
    }
"""

query = QueryType()
hello = ObjectType("Query")

@hello.field("hello")
def resolve_hello(*_):
    return "Hello, World!"

schema = make_executable_schema(type_defs, [query, hello])
