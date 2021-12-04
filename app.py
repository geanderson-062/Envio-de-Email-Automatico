import os 
import smtplib
from email.message import EmailMessage
from segredos import senha

#configurando email,-senha

EMAIL_ADDRESS = 'batatinha@gmail.com' #digite seu email aqui

EMAIL_PASSWORD = senha#exportando vareavel do segredos.py

  #criando o email

msg = EmailMessage()
msg['Subject'] = 'seu pacote está a caminho'#digite o assunto
msg['From'] = 'batatinha@gmail.com' #digite seu email aqui novamente
msg['To'] = 'puredebatata@outlook.com'#digite o email para que deseja enviar
msg.set_content('sua encomenda foi entregue a transportadora o codiogo de rastreio e 1234')

# enviando email

with smtplib.SMTP_SSL('smtp.gmail.com',465) as smtp: #especificar qual provedor e a porta

    smtp.login(EMAIL_ADDRESS,EMAIL_PASSWORD)
    smtp.send_message(msg)