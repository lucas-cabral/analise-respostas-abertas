# Importar bibliotecas necessárias

import pandas as pd
import re
from collections import defaultdict
import spacy

# Carregar spaCy em português
nlp = spacy.load('pt_core_news_sm')

# Categorias e palavras-chave

keywords = {
    "categoria principal 1": {
        "subcategoria1": ["palavra1", "palavra2", "palavra3"],
        "subcategoria2": ["palavra1", "palavra2", "palavra3"],
        "subcategoria3": ["palavra1", "palavra2", "palavra3"]
    },
    "categoria principal 2": {
        "subcategoria1": ["palavra1", "palavra2", "palavra3"],
        "subcategoria2": ["palavra1", "palavra2", "palavra3"],
        "subcategoria3": ["palavra1", "palavra2", "palavra3"]
    },
    "categoria principal 3": {
        "subcategoria1": ["palavra1", "palavra2", "palavra3"],
        "subcategoria2": ["palavra1", "palavra2", "palavra3"],
        "subcategoria3": ["palavra1", "palavra2", "palavra3"]
    }
}

# Lista de palavras-chave para negações (necessário acrescentar outras de acordo com o conjunto de dados).
negation_keywords = {'não', 'nunca', 'jamais', 'nenhum', 'ninguém', 'nada'}

def preprocess_text(text: str) -> str:
    text = text.lower()
    text = re.sub(r'[^\w\s]', '', text)
    return text

def lemmatize_text(text: str) -> str:
    doc = nlp(text)
    return " ".join([token.lemma_ for token in doc])

def detect_negations(doc):
    negated_phrases = set()
    negation_scope = 5  # Escopo de busca por palavras de negação. Aqui, até cinco palavras de distância.
    
    for i, token in enumerate(doc):
        if token.lemma_ in negation_keywords or token.dep_ == 'neg':
            start = max(0, i)
            end = min(len(doc), i + negation_scope + 1)
            negated_phrases.update(token.lemma_ for token in doc[start:end])
    
    print(f"Frases ou palavras potencialmente negadas: {negated_phrases}")
    return negated_phrases

def is_negated(keyword, token_positions, doc, negated_phrases):
    if keyword in token_positions:
        keyword_position = token_positions[keyword]
        keyword_token = doc[keyword_position]
        
        # Verifica se a palavra-chave está sob o escopo de uma negação
        if keyword in negated_phrases:
            # Procura por estruturas específicas de negação
            for i in range(max(0, keyword_position - 5), keyword_position):
                if doc[i].lemma_ in ['não', 'nem'] and doc[i:keyword_position+1].text.lower() in ['não gosto de', 'nem gosto de']: # Acrescentar mais expressões específicas, de acordo com o conjunto de dados.
                    return True
            return True  # Se estiver nas frases negadas e não for uma exceção, considera como negada
        
        # Verifica negações específicas como "não gosto"
        for token in doc:
            if token.lemma_ in negation_keywords and any(child.lemma_ == keyword for child in token.subtree):
                return True
    
    return False

def categorize_response(response, keywords):
    response = preprocess_text(response)
    doc = nlp(response)
    lemmatized_response = lemmatize_text(response)
    categories = defaultdict(set)

    token_positions = {token.lemma_: token.i for token in doc}
    negated_phrases = detect_negations(doc)

    print(f"Texto lematizado: {lemmatized_response}")
    print(f"Palavras-chave e posições: {token_positions}")

    for category, subcategories in keywords.items():
        for subcategory, keywords_list in subcategories.items():
            for keyword in keywords_list:
                if keyword in lemmatized_response:
                    if is_negated(keyword, token_positions, doc, negated_phrases):
                        print(f"Palavra '{keyword}' está negada, não categorizando.")
                    else:
                        categories[category].add(subcategory)
                        print(f"Palavra '{keyword}' categorizada em {category}_{subcategory}.")

    return dict(categories)

def analyze_responses(file_path):
    # Ler o arquivo CSV
    df = pd.read_csv(file_path, sep=',', encoding='utf-8')

    # Aplicar a função de categorização a cada resposta
    df['categorias'] = df['respostas'].apply(lambda x: categorize_response(x, keywords)) # Necessário substituir o "df['respostas']" pelo nome correto da coluna a ser analisada.
    
    # Criar colunas para cada categoria e subcategoria
    for category, subcategories in keywords.items():
        for subcategory in subcategories:
            col_name = f"{category}_{subcategory}"
            df[col_name] = df['categorias'].apply(lambda x: subcategory in x.get(category, []))
    
    # Remover a coluna 'categorias' temporária
    df = df.drop('categorias', axis=1)
    
    return df

# Uso do programa
file_path = 'arquivo.csv'  # Utilizar o caminho do arquivo a ser analisado.
result_df = analyze_responses(file_path)

# Exibir as primeiras linhas do resultado
print(result_df.head())

# Salvar o resultado em um novo arquivo CSV. Substituir pelo nome desejado.
result_df.to_csv('resultados.csv', index=False)

print("Análise concluída. Resultados salvos em 'resultados.csv'")
