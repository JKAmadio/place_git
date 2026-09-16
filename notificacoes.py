def enviar_notificacao(destinatario, mensagem):
    if not destinatario:
        raise ValueError("destinatario obrigatorio")
    print(f"[notificacao] {destinatario}: {mensagem}")
