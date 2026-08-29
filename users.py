from flask import Blueprint

from controllers.user_controller import (
    listar_usuarios,
    criar_usuario,
    buscar_usuario,
    atualizar_usuario,
    excluir_usuario
)

users_bp = Blueprint(
    "users",
    __name__,
    url_prefix="/users"
)


@users_bp.route("/", methods=["GET"])
def get_users():
    return listar_usuarios()


@users_bp.route("/", methods=["POST"])
def post_user():
    return criar_usuario()


@users_bp.route("/<int:user_id>", methods=["GET"])
def get_user(user_id):
    return buscar_usuario(user_id)


@users_bp.route("/<int:user_id>", methods=["PUT"])
def put_user(user_id):
    return atualizar_usuario(user_id)


@users_bp.route("/<int:user_id>", methods=["DELETE"])
def delete_user(user_id):
    return excluir_usuario(user_id)