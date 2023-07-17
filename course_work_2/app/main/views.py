from flask import Blueprint, render_template
from course_work_2.app import utils


main_blueprint = Blueprint("main_blueprint", __name__)


@main_blueprint.route("/")
def main_page():
    posts = utils.get_posts_all()
    bookmark_count = len(posts)

    return render_template("index.html", posts=posts, bookmark_count=bookmark_count)


@main_blueprint.route("/posts/<int:post_id>")
def post_page(post_id):
    post = utils.get_post_by_pk(post_id)
    comments = utils.get_comments_by_id(post_id)
    comments_count = len(comments)

    return render_template("post.html", post=post, comments=comments, comments_count=comments_count)


@main_blueprint.route("/users/<string:user_name>")
def user_page(user_name):
    user_posts = utils.get_posts_by_user(user_name)

    return render_template("user-feed.html", user_posts=user_posts)


@main_blueprint.route("/api/posts", methods=["GET"])
def posts_api_page():
    posts = utils.get_posts_all()

    return posts


@main_blueprint.route("/api/posts/<int:post_id>", methods=["GET"])
def post_api_page(post_id):
    post = utils.get_post_by_pk(post_id)

    return post
