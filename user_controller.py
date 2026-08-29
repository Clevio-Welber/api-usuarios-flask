from flask import request, jsonify
from data.users import users

def listar_usuarios():
    return jsonify(users), 200

def criar_usuario():
    dados = request.get_json()

    if not dados or "nome" not in dados or "email" not in dados:
        return jsonify({
            "erro": "Nome e email são obrigatórios"
        }), 400

    novo_id = max(
        [user["id"] for user in users],
        default=0
    ) + 1

    novo_usuario = {
        "id": novo_id,
        "nome": dados["nome"],
        "email": dados["email"]
    }

    users.append(novo_usuario)

    return jsonify(novo_usuario), 201

def buscar_usuario(user_id):

    usuario = next(
        (
            user
            for user in users
            if user["id"] == user_id
        ),
        None
    )

    if usuario is None:
        return jsonify({
            "erro": "Usuário não encontrado"
        }), 404

    return jsonify(usuario), 200


def atualizar_usuario(user_id):

    usuario = next(
        (
            user
            for user in users
            if user["id"] == user_id
        ),
        None
    )

    if usuario is None:
        return jsonify({
            "erro": "Usuário não encontrado"
        }), 404

    dados = request.get_json()

    if not dados:
        return jsonify({
            "erro": "Dados não informados"
        }), 400

    usuario["nome"] = dados.get(
        "nome",
        usuario["nome"]
    )

    usuario["email"] = dados.get(
        "email",
        usuario["email"]
    )

    return jsonify(usuario), 200


def excluir_usuario(user_id):

    usuario = next(
        (
            user
            for user in users
            if user["id"] == user_id
        ),
        None
    )

    if usuario is None:
        return jsonify({
            "erro": "Usuário não encontrado"
        }), 404

    users.remove(usuario)

    return jsonify({
        "mensagem": "Usuário excluído com sucesso"
    }), 200