import openai

openai.api_key = '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'

response = openai.Completion.create(
    engine="davinci",  # Escolha o modelo de linguagem (davinci é o mais avançado)
    prompt="Escreva uma resposta para a pergunta: 'Qual é a capital do Brasil?'",
    max_tokens=50  # Limite de tokens na resposta
)

generated_text = response.choices[0].text
print(generated_text)


