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
        self.usuario['_id'] = uuid.uuid4().hex
        self.usuario['nome'] = request.form['nome']
        self.usuario['senha'] = pbkdf2_sha256.encrypt(request.form['senha'])
        encontrar_usuario = db.usuarios.find_one({'nome': self.usuario['nome']})
        if encontrar_usuario:
            return abort(409)
        db.usuarios.insert_one(self.usuario)
        self.iniciar_sessao(self.usuario)
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
