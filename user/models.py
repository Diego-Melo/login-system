from flask import Flask, jsonify, request, session, redirect, url_for, abort
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class Usuarios:

    usuario = {
        '_id': '',
        'nome': '',
        'senha': ''
    }

    def cadastrar(self):
        ''' Cadastra um usuário de acordo com uma requisição da página anterior. '''
        # Gera um id único e aleatório
        self.usuario['_id'] = uuid.uuid4().hex
        # Recebe o nome
        self.usuario['nome'] = request.form['nome']
        # Codifica a senha
        self.usuario['senha'] = pbkdf2_sha256.encrypt(request.form['senha'])
        # Verifica se o usuário já existe
        encontrar_usuario = db.usuarios.find_one({'nome': self.usuario['nome']})
        if encontrar_usuario:
            return abort(409)
        # Insere o usuário caso ele já não exista
        db.usuarios.insert_one(self.usuario)
        # Inicia sessão
        self.iniciar_sessao(self.usuario)
        # Redireciona para dashboard
        return redirect(url_for('dashboard'))

    def iniciar_sessao(self, usuario):
        ''' Inicia a sessão '''
        session['usuario'] = usuario
        session['logado'] = True

    def logar(self):
        ''' Verifica se o usuário está cadastrado, se estiver, irá ser redirecionado, senão não terá o acesso autorizado.'''
        # Procura o usuário no banco
        usuario = db.usuarios.find_one({
            'nome': request.form['nome']
        })
        # Caso a senha corresponda, o usuário será redirecionado
        if usuario and pbkdf2_sha256.verify(request.form['senha'], usuario['senha']):
            self.iniciar_sessao(usuario)
            return redirect(url_for('dashboard'))
        else:
            return abort(401)

    def sair(self):
        ''' Acaba com a sessão '''
        session.clear()
        return redirect('/nao-logado')
