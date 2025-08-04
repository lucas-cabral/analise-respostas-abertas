# Análise de respostas a questão aberta

Este programa foi criado para analisar 604 respostas a uma questão aberta de um survey sobre a relação entre os públicos e o jornalismo local.

O programa foi criado com o auxílio de duas IAs generativas: *ChatGPT (OpenAI)* e *Claude.ai (Anthropic)*. Ele categoriza as respostas de acordo com a presença de palavras-chave.

O processo de desenvolvimento do programa se deu da seguinte forma:

1. Leitura humana das respostas abertas;
2. Criação de quatro categorias base;
3. Diálogo com plataformas de IA para a criação de novas categorias. Exemplo de prompt:

```
    Olá! Eu tenho uma planilha com respostas à pergunta: "por que você acessa notícias no seu dia a dia?". Gostaria de analisar essas respostas, mas são muitas (604). E elas são respostas bastante subjetivas, olhar as palavras mais frequentes não basta. Você tem alguma ideia do que eu posso fazer?
    Pensei em criar 4 variáveis para categorizar as respostas. São elas: motivação (necessidade/utilidade/gosto); geográfica (cidade/país/mundo); assunto (trânsito/saúde/política etc.); e tempo (dia/semana etc.). O que você acha? Tem alguma outra sugestão de variável?
    Posso te enviar o arquivo para você dar uma olhada e me ajudar?
```

O prompt gerou a seguinte resposta:

```
     Achei a ideia das quatro variáveis bastante interessante, pois cobrem aspectos essenciais para categorizar as respostas. Aqui estão algumas sugestões adicionais:
  
      Frequência: Para entender como as pessoas relatam a frequência com que acessam notícias. Isso pode complementar a variável "tempo", focando mais na regularidade.
  
      Fonte de Acesso: Considerar se mencionam a mídia tradicional, redes sociais, ou outras fontes. Pode ajudar a identificar as plataformas preferidas.
  
      Emoção: Categorizar respostas que expressam emoções (ansiedade, curiosidade, necessidade de se manter informado) pode fornecer insights sobre a relação emocional das pessoas com as notícias.
  
    Se quiser enviar o arquivo, posso te ajudar a definir melhor as categorias e a automatizar a análise.
```

As primeiras categorias e palavras-chave criadas pelo ChatGPT, por exemplo, foram:

```
     categorias_keywords = {
      'motivacao': {
          'necessidade': ['necessidade', 'preciso', 'importante', 'essencial'],
          'utilidade': ['util', 'relevante', 'prático'],
          'gosto': ['gosto', 'interesso', 'curiosidade']
      },
      'geografica': {
          'cidade': ['município', 'cidade', 'local', 'bairro'],
          'país': ['país', 'nacional', 'brasil'],
          'mundo': ['mundo', 'internacional', 'global']
      },
      'assunto': {
          'trânsito': ['trânsito', 'tráfego', 'rodovias'],
          'saúde': ['saúde', 'pandemia', 'hospital'],
          'política': ['política', 'governo', 'eleições']
      },
      'tempo': {
          'dia': ['dia', 'diário', 'hoje'],
          'semana': ['semana', 'semanal']
      },
      'frequencia': {
          'alta': ['todo dia', 'frequentemente', 'constantemente'],
          'baixa': ['raramente', 'ocasionalmente']
      },
      'fontes_acesso': {
          'tradicional': ['televisão', 'jornal', 'rádio'],
          'online': ['internet', 'redes sociais', 'site', 'portal']
      },
      'emocao': {
          'ansiedade': ['preocupado', 'ansioso'],
          'curiosidade': ['curioso', 'interesse']
      }
```
  
As categorias e palavras-chave criadas foram complementadas em diálogo com o Claude.ai e o ChatGPT, utilizando cada um dos sistemas para criticar e complementar as sugestões do outro. Às sugestões, foram somadas ideias dos próprios pesquisadores;

4. Criação do programa em Python que trata o texto e identifica as palavras-chave e palavras de negação para categorizar cada uma das respostas;
5. Simplificação das categorias para autoexclusão e para desenvolvimento teórico;
6. Leitura e categorização humana de 100 respostas, comparação com os resultados da categorização automática e adaptação do programa conforme os motivos identificados para as diferenças nas categorias. As comparações foram realizadas até que os resultados humanos e do programa fossem semelhantes;
7. A partir dos resultados do programa, foi possível realizar inferências teóricas e pensar categorias mais amplas, que englobam as primeiras, para melhorar a confiabilidade dos resultados e evitar problemas de redundância.

O programa disponível no repositório utiliza categorias e palavras-chave genéricas. O objetivo é que os interessados possam utilizá-lo para analisar seus próprios conjuntos textuais. A categorização e palavras-chave finais utilizadas neste projeto de pesquisa estão disponíveis em artigos científicos e podem ser utilizadas para avaliar o trabalho aqui desenvolvido.
