from modulos import ArquivoExiste, jaCadastrado, novoCadastro, login

if ArquivoExiste():
    if jaCadastrado():
        login()
    else:
        novoCadastro()
