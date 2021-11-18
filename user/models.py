from flask import Flask, jsonify, request
from passlib.hash import pbkdf2_sha256
from app import db
import uuid


class Usuarios:
    usuario = {
        '_id': '',
        'nome': '',
        'senha': ''
    }
    
    
    def logar(self):
        usuario = db.usuarios.find_one({
            'nome': request.form['nome']
        })
        if usuario and pbkdf2_sha256.verify(request.form['password'], usuario['senha']):
            return self.start_session(usuario)
        else:
            return jsonify({'error':'Invalid login credentials'}), 401
        
        
    def sair(self):
        return jsonify(self.usuario)
