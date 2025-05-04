def fazer_pergunta(texto, resposta_correta):
    resposta = input(texto).upper().strip()
    if resposta == resposta_correta:
        print("\nCorreto!!!\n")
        return 1
    else:
        print(f"\nIncorreto! A resposta correta é {resposta_correta}).\n")
        return 0

print("\nSeja bem vindo ao QUIZ sobre Lógica de programação!"
      "\nVocê terá 5 perguntas e para cada resposta correta você ganhará 1 ponto.\n")

acertos = 0

acertos += fazer_pergunta(
    "\nO que é um algoritmo?"
    "\nA) Um tipo de dado usado em programação"
    "\nB) Um conjunto de instruções para resolver um problema"
    "\nC) Um erro no código"
    "\nD) Um tipo de linguagem de programação  ", "B"
)

acertos += fazer_pergunta(
    "\nQual das estruturas abaixo é usada para repetir um bloco de código enquanto uma condição for verdadeira?"
    "\nA) if"
    "\nB) else"
    "\nC) while"
    "\nD) def  ", "C"
)

acertos += fazer_pergunta(
    "\nO que significa a expressão x = x + 1 em lógica de programação?"
    "\nA) A variável x recebe 1"
    "\nB) A variável x é multiplicada por 1"
    "\nC) A variável x é incrementada em 1"
    "\nD) O código gera erro  ", "C"
)

acertos += fazer_pergunta(
    "\nO que acontece se você usar uma variável sem inicializá-la antes?"
    "\nA) Ela será criada automaticamente com valor 0"
    "\nB) O programa ignora e continua"
    "\nC) O programa imprime None"
    "\nD) O programa gera um erro  ", "D"
)

acertos += fazer_pergunta(
    "\nEm qual estrutura de decisão o programa avalia várias condições diferentes?"
    "\nA) if simples"
    "\nB) if...else"
    "\nC) if...elif...else"
    "\nD) while  ", "C"
)

# Mensagem final
mensagens = {
    0: "Não desanime, se esforce mais um pouco que você consegue!",
    1: "Continue estudando! Você vai melhorar!",
    2: "Estude um pouquinho mais e você consegue!",
    3: "Não foi mal não ;)!",
    4: "Excelente trabalho! Quase gabaritou!",
    5: "Parabéns, você é um ótimo garoto de programa kkkk! Continue assim!"
}

print(f"\nVocê acertou {acertos}/5 perguntas.\n{mensagens[acertos]}")