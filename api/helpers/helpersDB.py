from api.db.supabasecon import sup

#data retrieved from database---------------------------------------
def get_products_ids():
    response = sup.table('product').select("id").execute()
    return response


def get_product_name_and_price_with_id(product_id):
    response = sup.table('product').select("name,price").eq("id",product_id).execute()
    return response


def get_image_a_id_with_product_id(product_id):
    response = sup.table('media').select("img_a").eq("id_product",product_id).execute()
    return response.data[0]["img_a"]

