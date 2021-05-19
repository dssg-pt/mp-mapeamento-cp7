![DSGG Portugal](assets/dssg_logo_lettering.png)

# 👶🚀 Mini-Projecto [Mapeamento de Códigos Postais para localizações em Portugal] 

Este é o repositório do Mini-Projecto **[Mapeamento de Códigos Postais para localizações em Portugal]**.

## 🤔 Contexto

O Banco Alimentar - Rede de Emergência Alimentar tem estado a modernizar a sua gestão de informação. De momento, encontram-se a trabalhar no desenvolvimento de uma plataforma web para a gestão de pedidos de ajuda alimentar.

Um dos desafios desta plataforma será reduzir, tanto quanto possível, a introdução manual de dados, uma das maiores causas de duplicação de pedidos devido a gralhas e erros ortográficos.

Assim, seria fundamental conseguir obter a freguesia, concelho e distrito a partir do código postal na forma XXXX-XXX.

Algumas ferramentas existentes permitem fazê-lo, como a plataforma dos CTT e a API [Dumínio](https://www.duminio.com/ptcp/#two), mas estes não têm em conta a atualização de freguesias após a Reorganização Administrativa do Território das Freguesias ocorrida em 2012. 

## 🥅 Objectivo

Criação de uma tabela .csv e endpoint que permita o mapeamento entre um código postal na forma XXXX-XXX e a freguesia, concelho e distrito correspondente, com a atualização de freguesias após a Reorganização Administrativa do Território das Freguesias ocorrida em 2012. 

## ⛲ Fontes de dados

O miniprojeto será criado a partir de duas fontes de dados distintas, sendo que os participantes podem encontrar alternativas:
- [API para mapeamento entre Código Postal e Localização, com as denominações antigas](https://www.duminio.com/ptcp/#two)
- [Mapeamento entre denominações pós 2012 e pré 2012](https://www.sg.mai.gov.pt/AdministracaoEleitoral/Autarquias/ReorganizacaoFreguesias/Paginas/default.aspx) 
- [Bases de dados de moradas CTT](http://centraldedados.pt/codigos_postais/) 

## 🧱 Principais etapas

O projeto seguirá dois passos:

- Mapeamento entre código postal e freguesia, concelho, e distrito
- Conversão das freguesias após a Reorganização Administrativa do Território das Freguesias ocorrida em 2012
- Criação de um endpoint em FastAPI/Flask para fazer os pedidos

## 🎯 Resultado final

Ficheiro CSV com mapeamento entre todos os códigos postais possíveis em Portugal e a freguesia, concelho, e distrito, disponível em:
 - [cod_post_freg_matched.csv](https://github.com/dssg-pt/mp-mapeamento-cp7/blob/main/output_data/cod_post_freg_matched.csv)

Endpoint com imagem Docker em:
 - [API](https://github.com/dssg-pt/mp-mapeamento-cp7/tree/main/api)
 - Exemplo de utilização:
  ```
  http://127.0.0.1:8000/1234567
  ```
  
  Resposta:
  ```
  0:
      'Distrito': "XXXXX"
      'Concelho': "XXXXX"
      'Freguesia': "XXXXX"
      'CodigoPostal': 1234567
  ```

Limitações:

  Não se conseguiu encontrar informação relativamente a 1257 códigos postais, disponíveis em [cod_post_freg_missing.csv](https://github.com/dssg-pt/mp-mapeamento-cp7/blob/main/output_data/cod_post_freg_missing.csv).

## 👥 Equipa

- João Rodrigues:
  - [GitHub](https://github.com/J-Rodrigues0)
  - [LinkedIn](https://www.linkedin.com/in/joao-rodrigues0/)

## ⏲️ Duração prevista

Dado o tamanho da equipa e os resultados finais descritos, este mini-projecto tem uma duração estimada de 4 semanas (com a alocação de algumas horas por semana por cada membro da equipa) para a conclusão dos 2 primeiros pontos, mais 2 semanas para a criação do endpoint.

## 🔁 Reprodutibilidade

O código utilizado para reproduzir os resultados do miniprojeto deverá estar organizado neste repositório, com as dependências necessárias descritas num ficheiro. 

# 👉 Chegaste aqui e queres juntar-te a este Mini-Projecto?

Vê a [#1](/../../issues/1).

--- 

## 📜 Sobre os Mini-Projectos

_Os Mini-Projectos são iniciativas da [DSSG PT](https://dssg.pt) em que uma pequena equipa de Voluntários trabalha de forma independente numa iniciativa concreta e a curto prazo que, baseada em dados abertos, visa gerar resultados valiosos para a sociedade em geral. A lista de Mini-Projectos activos pode ser [consultada no nosso GitHub](https://github.com/dssg-pt/)._
