#!/usr/bin/env python3
"""Exemplos de envio de e-mail"""
import smtplib

SERVER = "localhost"
PORT = 8025

FROM = "tiagouruba@gmail.com"
TO   = ["destino1@server.com", "destino2@server.com"]
SUBJECT = "Meu email via python"
TEXT = """\
Este é o meu email enviado pelo Python
<b>Olá mundo</b>
"""

#SMTP
mensage = f"""\
From: {FROM}
To: {",".join(TO)}
Subject: {SUBJECT}

{TEXT}
"""

with smtplib.SMTP(host=SERVER, port=PORT) as server:
    server.sendmail(FROM, TO, mensage.encode("utf-8"))