from ariadne import ObjectType, QueryType, make_executable_schema
from api.helpers.helpersDB import get_products_ids, get_product_name_and_price_with_id, get_image_a_id_with_product_id
from api.helpers.helpersDrive import get_root_folder_ids, getFilesIdsOfFolderWithId

type_defs = """
    type Query {
        hello: String!
        getProducsIds: [Product]!
        getProductNameAndPriceWithId(productId: ID!): [Product]
        getImageAIdWithProductId(productId: String!): String!
    }
    type Product {
        id: Int!
        name: String
        price: Int!
    }
"""

query = QueryType()
hello = ObjectType("Query")
Product = ObjectType("Product")

@hello.field("hello")
def resolve_hello(*_):
    return "Hello, World!"

@query.field("getProducsIds")
def resolve_getProducsIds(*_):
    return get_products_ids().data

@query.field("getProductNameAndPriceWithId")
def resolve_getProductNameAndPriceWithId(*_,productId):
    return get_product_name_and_price_with_id(str(productId)).data

@query.field("getImageAIdWithProductId")
def resolver_getImageAIdWithProductId(*_,productId):
    return get_image_a_id_with_product_id(str(productId))

schema = make_executable_schema(type_defs, [query, hello])
