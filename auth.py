def autenticar(usuario, senha):
    # TODO: validar contra base de usuarios real
    if not usuario or not senha:
        return False
    if len(senha) < 8:
        return False
    return True
