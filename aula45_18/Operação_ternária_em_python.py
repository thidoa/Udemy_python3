"""
Operador ternário em Python
"""
logged_user = False

if logged_user:
    msg = 'Usuário logado.'
else:
    msg = 'Usuário precisa logar.'

print(msg)

#               |
# Simplificando v

msg = 'Usuário logado.' if logged_user else 'Usuário precisa logar.'

print(msg)
