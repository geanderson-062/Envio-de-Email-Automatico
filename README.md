# Aplicaticação de Envio de Email Automático

Este documento fornece uma visão geral e instruções para a utilização de um aplicativo simples em Python para enviar e-mails automaticamente. O script usa a biblioteca `smtplib` para conectar-se a um servidor de e-mail e enviar uma mensagem.

---

## Descrição

O aplicativo foi desenvolvido para enviar e-mails automáticos informando sobre o status de uma encomenda. Ele constrói uma mensagem de e-mail e a envia para um destinatário específico, informando o código de rastreamento da encomenda.

---

## Pré-requisitos

Antes de executar o script, certifique-se de que o Python está instalado em seu sistema. Além disso, você precisará das seguintes bibliotecas:

- `smtplib`
- `email`

Se não estiverem instaladas, você pode instalá-las usando o pip:

```bash
pip install secure-smtplib email
```
---

## Configuração

1. **Credenciais de Email**: Você deve configurar as credenciais do remetente. No script, substitua `'batatinha@gmail.com'` pelo endereço de e-mail que deseja usar para enviar as mensagens.

2. **Senha**: O script usa um arquivo `segredos.py` para armazenar a senha. Crie este arquivo e defina uma variável `senha` com a senha do seu e-mail.

    ```python
    # segredos.py
    senha = 'SuaSenhaAqui'
    ```

3. **Informações do Destinatário**: Altere o endereço de e-mail do destinatário (`'puredebatata@outlook.com'`) para o endereço para o qual você deseja enviar a notificação.

4. **Assunto e Conteúdo da Mensagem**: Modifique o assunto e o conteúdo da mensagem conforme necessário.

---

## Uso

Para usar o aplicativo, execute o script Python. Certifique-se de que todas as configurações estejam corretas antes de executá-lo.

```bash
python nome_do_seu_script.py
```
---

## Segurança

Como boa prática de segurança, não armazene senhas diretamente no código-fonte. Este script usa um arquivo separado para armazenar a senha, mas existem métodos mais seguros para gerenciar credenciais, como variáveis de ambiente ou gerenciadores de segredos.

---

## Limitações e Considerações

- O script está configurado para usar o servidor SMTP do Gmail. Se você estiver usando outro provedor de e-mail, precisará ajustar o servidor e a porta no script.
- Certifique-se de que o acesso a aplicativos menos seguros esteja ativado na conta do Gmail que você está usando para enviar e-mails, embora essa prática não seja recomendada para contas de e-mail principais devido a preocupações de segurança.
- O script não possui tratamento de erros avançado, portanto, pode falhar sem fornecer informações detalhadas sobre o motivo.

---

## Contribuições

Contribuições para o projeto são bem-vindas. Sinta-se à vontade para propor melhorias ou adicionar novas funcionalidades.

---

## Suporte

Se você encontrar algum problema ao usar este script ou tiver sugestões para melhorias, por favor, abra uma issue no repositório do projeto ou envie um e-mail para o desenvolvedor.

---

Este README fornece as informações básicas necessárias para configurar e usar o aplicativo de envio de e-mails. Para qualquer esclarecimento adicional ou suporte, entre

em contato com o desenvolvedor ou consulte a documentação oficial das bibliotecas utilizadas.


