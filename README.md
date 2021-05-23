
# BACKUP OLT FIBERHOME

## Visão Geral
Script desenvolvido em Python3 para automatizar o backup das configurações e logs dos chassis Fiberhome AN5506.

### Bibliotecas Necessárias
Para o funcionamento correto do script baixe as bibliotecas
<p>
  <a href="https://docs.python.org/3/library/configparser.html">🔗 configparser</a>
</p>
<p>
  <a href="https://docs.python.org/3/library/datetime.html">🔗 datetime</a>
</p>
<p>
  <a href="https://github.com/python-telegram-bot/python-telegram-bot">🔗 telegram</a>
</p>
<p>
  <a href="https://docs.python.org/3/library/telnetlib.html">🔗 telnetlib</a>
</p>
<p>
  <a href="https://docs.python.org/3/library/time.html">🔗 time</a>
</p>
<p>
  <a href="https://pypi.org/project/pytz/">🔗 pytz</a>
</p>

### Bot Telegram
  <a href="https://core.telegram.org/bots#6-botfather">Crie um bot no Telegram</a> para receber as mensagens de alerta.
  <p>
    Primeiro passo é ter um Telegram Bot. Para criá-lo, abra seu app do Telegram, busque por: @BotFather e clique sobre ele;
  </p>
  
 ![fig1](https://user-images.githubusercontent.com/46397610/119211619-acf5ae00-ba89-11eb-8238-8e838ea5a229.png)
 
  <p>
    Envie o comando: /newbot;
  </p>
    
  ![fig2](https://user-images.githubusercontent.com/46397610/119211373-18d71700-ba88-11eb-86c6-7e2650e21759.png)
    
  <p>
    De um nome ao seu bot;
  </p>
  
  ![fig3](https://user-images.githubusercontent.com/46397610/119211340-e6c5b500-ba87-11eb-8b2a-b2d5eb53ddd9.png)
  
  
  <p>
   Insira um username para o bot. O username obrigatoriamente tem que terminar com a palavra bot;
  </p>
  
  ![fig4](https://user-images.githubusercontent.com/46397610/119211342-ed542c80-ba87-11eb-868f-b7174972ef96.png)
  
  <p>
  Feito isso, você receberá um Token;
  </p>
  
  ![fig5](https://user-images.githubusercontent.com/46397610/119211465-93079b80-ba88-11eb-929c-9e5352e98cdc.png)
  
  <p>
  Insira o Token no arquivo config.ini no campo TOKEN = <Token Telegram do BOT>;
  </p>
  <p>
  Clique no link para seu bot; 
  </p>
  
  ![fig7](https://user-images.githubusercontent.com/46397610/119212673-5049c180-ba90-11eb-9cdd-091987f15294.png)
  
  <p>
  Clique em começar ou envie /start no chat para poder receber as notificações;
  </p>
  
  ![fig8](https://user-images.githubusercontent.com/46397610/119212844-686e1080-ba91-11eb-8aa6-de8c2fb49f44.png)

  <p>
  Para descobrir seu chat id busque no telegram por @userinfobot;
  </p>
  
  ![fig6](https://user-images.githubusercontent.com/46397610/119212478-fac0e500-ba8e-11eb-88b4-3cc916c6441e.png)
  
  <p>
  Insira o chat id no arquivo config.ini no campo USUARIO = <Seu id no telegram>;
  </p><p></p>
  
### Rodando o Script no Linux
  
  <p>
  Instale o <a href="https://www.gnu.org/software/screen/">screen</a> no seu servidor caso não tenha, no Debian ou Ubuntu use o comando apt-get install screen;
  </p>
  
  <p>
  No terminal digite screen para iniciar a sessão, depois navegue até o diretório onde se encontra o script e digite python3 <nome do script>.py
  </p>
  

  
### Contribuindo
Desde de já agradeço por se disponibilizarem a contribuir com melhorias para este script. Todos podem ajudar este projeto com novos recursos, correções de bugs ou melhorias de desempenho.
