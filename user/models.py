from flask import Flask, jsonify, request, session
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class Usuarios:
    usuario = {
        '_id': '',
        'nome': '',
        'senha': ''
    }
    
    def iniciar_sessao(self, usuario):
        session['logado'] = True
        session['usuario'] = usuario
        
    def logar(self):
        usuario = db.usuarios.find_one({
            'nome': request.form['nome']
        })
        if usuario and pbkdf2_sha256.verify(request.form['senha'], usuario['senha']):
            return self.iniciar_sessao(usuario)
        else:
            return jsonify({'error':'Invalid login credentials'}), 401
    
    def sair(self):
        return jsonify(self.usuario)
