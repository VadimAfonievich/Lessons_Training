import json


def get_posts_all():
    with open("./data/posts.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_comments_all():
    with open("./data/comments.json", "r", encoding="utf-8") as file:
        data = json.load(file)
    return data


def get_posts_by_user(user_name):
    posts = get_posts_all()
    posts_by_user = []

    for post in posts:
        if post["poster_name"] == user_name:
            posts_by_user.append(post)
    return posts_by_user

    #         return print(post)
    # if user_name not in posts:
    #     raise ValueError("Такого пользователя нет!")


def get_comments_by_id(post_id):
    comments = get_comments_all()

    comments_by_id = []

    for comment in comments:
        if comment["post_id"] == post_id:
            comments_by_id.append(comment)

    return comments_by_id


def search_for_posts(query):
    posts = get_posts_all()

    posts_list = []

    for post in posts:
        if query.lower() in post["content"].lower():
            posts_list.append(post)
    return posts_list


def get_post_by_pk(pk):
    posts = get_posts_all()
    for post in posts:
        if post["pk"] == pk:
            return post


# print(get_posts_by_user("leo"))
# print(get_posts_by_user("hank"))
#
# print(f"Комментарии По id {1}: {get_comments_by_id(1)}")
# print(f"Поису по ключевому слову: {search_for_posts('опять')}")
# print(f"Пост по pk: {get_post_by_pk(2)}")
