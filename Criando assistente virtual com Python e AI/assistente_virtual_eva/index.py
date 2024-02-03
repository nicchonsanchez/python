import speech_recognition as sr
import re
import pyttsx3
from datetime import datetime

nome = "Nick"  # Criando variável do nome
nomeAI = "Eva" # Nome da IA
frase = ""

# Para fazer calculos
def calcular(operacao, num1, num2):
    if operacao in ['soma', 'mais', '+']:
        resultado = num1 + num2
    elif operacao in ['subtracao', 'menos', '-']:
        resultado = num1 - num2
    elif operacao in ['multiplicacao', 'vezes', '*']:
        resultado = num1 * num2
    elif operacao in ['divisao', 'dividido', '/']:
        if num2 != 0:
            resultado = num1 / num2
        else:
            return "Erro: Divisão por zero não permitida."
    else:
        return "Erro: Operação inválida. Escolha entre 'soma', 'subtracao', 'multiplicacao' ou 'divisao'."

    return resultado




# Ativando a IA ######################################################################

# Criando loop infinito
while True:
    # Dando acesso ao microfone
    mic = sr.Recognizer()

    with sr.Microphone() as source:
        engine = pyttsx3.init()
        engine.setProperty('voice', "com.apple.speech.synthesis.voice.luciana")  # Colocando a voz da Luciana disponível gratuitamente pelo Google
        mic.adjust_for_ambient_noise(source)  # Ajusta com o som ambiente, pro caso de ruídos e barulhos

        print("Fale alguma coisa...")

        audio = mic.listen(source)

        try:
            frase = mic.recognize_google(audio, language='pt-BR')  # Usando o Google para reconhecer a fala

            # Buscando comandos na fala
            if re.search(r'\b' + "atenção " + nomeAI + r'\b', format(frase)):
                engine.say("Sim senhor!")
                engine.runAndWait()
                print("Você me solicitou.")

            elif re.search(r'\b' + "meu nome é " + r'\b', format(frase)):
                t = re.search('meu nome é (.*)', format(frase))  # Buscando o seu nome
                nome = t.group(1)  # Definindo variável 'nome' com o seu nome
                print("Seu nome é " + nome)
                engine.say("Olá " + nome + "! Meu nome é "+nomeAI+", estou aqui para ajudá-lo.")
                engine.runAndWait()

            elif re.search(r'\b' + "como você está" + r'\b', format(frase)):
                engine.say("Obrigada por perguntar! Estou funcionando perfeitamente.")
                engine.runAndWait()
                print("Você perguntou como a IA está.")

            # Verificar horas
            elif re.search(r'\b' + "que horas são" + r'\b', format(frase)) or re.search(r'\b' + "Que horas são" + r'\b', format(frase)) or re.search(r'\b' + "quantas horas são" + r'\b', format(frase)) or re.search(r'\b' + "Quantas horas são" + r'\b', format(frase)):
                agora = datetime.now()
                hora_atual = agora.strftime("%H:%M")
                engine.say("Agora são " + hora_atual)
                engine.runAndWait()
                print("São atualmente:", hora_atual)

            # Calcular
            elif re.search(r'\b' + "calcule" + r'\b', format(frase)) or re.search(r'\b' + "Calcule" + r'\b', format(frase)) or re.search(r'\b' + "quanto é" + r'\b', format(frase)) or re.search(r'\b' + "Quanto é" + r'\b', format(frase)):
                operacoes = re.findall(r'(\+|-|\*|/|mais|menos|vezes|dividido|soma|subtracao|multiplicacao|divisao)', frase)
                numeros = re.findall(r'\b\d+\b', format(frase))
                
                if len(operacoes) == 1 and len(numeros) >= 2:
                    operacao = operacoes[0]
                    num1 = float(numeros[0])
                    num2 = float(numeros[1])
                    resultado_calculo = calcular(operacao, num1, num2)
                    print(f"O resultado da {operacao} de {num1} e {num2} é: {resultado_calculo}")
                    engine.say(f"O resultado é: {resultado_calculo}")
                    engine.runAndWait()
                else:
                    print("Comando de cálculo inválido.")

            else:
                print("Comando não reconhecido.")
                print("Você disse:", frase)

        # Caso ocorra algum erro
        except sr.UnknownValueError:
            print("Ops, algo deu errado.")
            print("Você disse:", frase)



