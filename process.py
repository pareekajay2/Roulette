from database import is_user_exists,get_user_details, insert_feedback,get_product_details,get_top_5_products,\
    is_product_exists,insert_product,is_username_exists,insert_users,is_feedback_exists,update_ratings
import uuid
import datetime


def first_time_user():
    username = input("find a suitable username: ", )
    username_status = is_username_exists(username=username)
    while username_status is False:
        print("username already exists")
        username = input("find a suitable username: ", )
        username_status = is_username_exists(username=username)
    password = input("use a strong password: ", )
    confirm_password = input("confirm password: ", )
    while password != confirm_password:
        print("passwords does not match")
        password = input("use a strong password: ", )
        confirm_password = input("confirm password: ", )
    persona = input("choose a field you work in: ", )
    insert_users(id=str(uuid.uuid4()), username=username, password=password, persona=persona,
                 created_at=str(datetime.datetime.now()), updated_at=str(datetime.datetime.now()))


def user_login():
    user_exists = False

    while user_exists is False:
        user_input = input("signin/signup:", )
        if user_input == "signin":
            username = input("username: ", )
            password = input("password: ", )

            user_exists = is_user_exists(username=username, password=password)
        else:
            first_time_user()

    print("Welcome")
    return username, password


def product_details_process(persona):
    get_top_5_products(persona=persona)

    product_search = input("Product you want to search for:", )
    product_id = None

    if product_search == "signout":
        app()
    else:
        try:
            product_id, product_name = get_product_details(product_search)
        except:
            product_status = is_product_exists(product_search)
            if product_status is False:
                product_id = str(uuid.uuid4())
                insert_product(id=product_id, product_name=product_search, created_at=str(datetime.datetime.now()),
                               updated_at=str(datetime.datetime.now()))
            else:
                print("Something went wrong!")
    return product_id, product_search


def feedback_process(username,password,product_id):
    user_id = get_user_details(username, password)['user_id'].iloc[0]

    rating = input("Please provide rating from 1 to 5: ", )
    if rating == "signout":
        app()
    else:
        review = input("Please provide review: ", )

        if review == "signout":
            app()
        else:
            review_exists = is_feedback_exists(user_id=user_id, product_id=product_id)
            if review_exists is False:
                insert_feedback(id=str(uuid.uuid4()), product_id=product_id, user_id=user_id,
                                rating=int(rating), review=review, created_at=str(datetime.datetime.now()),
                                updated_at=str(datetime.datetime.now()))
            else:
                update_ratings(rating=rating, review=review, user_id=user_id, product_id=product_id)


def start(user_input, username, password):
    persona = get_user_details(username, password)['persona'].iloc[0]
    product_id, product_search = product_details_process(persona)
    feedback_process(username, password, product_id)
    return start("signin", username, password)

def app():
    print("Enter username and password")
    username, password = user_login()
    start("signin", username, password)
