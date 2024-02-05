"""
    Traduce la voz a texto pudiendo asi
    dar indicaciones, el texto resultante
    lo convierte a voz

    Nota: El programa esta en fase de desarrollo
    temprana
"""

import pyttsx3
import speech_recognition as sr
import pywhatkit
import yfinance as yf
import pyjokes
import webbrowser
import datetime
import wikipedia

# Transformar voz en texto
def trasformar_audio_texto():
    
    # Almacenar el reconocedor en una variable
    r = sr.Recognizer()
    with sr.Microphone() as origen:
        # Tiempo de espera
        r.pause_threshold = 0.8

        # Informar comienzo de grabacion
        print("Ya puedes hablar")

        # Guardar el audio
        audio = r.listen(origen)

        try:
            # Buscar en google
            pedido = r.recognize_google_cloud(audio, language = "es-mx")

            # Transformar voz
            print("Dijiste: " + pedido)

            # Devolver pedido
            return pedido
        
        except sr.UnknownValueError:

            # Prueba que no comprendio el audio
            print("Chin, no entendi")

            # Devolver error
            return "Sigo esperando"
        
        except sr.RequestError:
            # Prueba que no comprendio el audio
            print("Chin, no lo encontre")

            # Devolver error
            return "Sigo esperando"
        
        except:
            # Prueba que no comprendio el audio
            print("Chin, algo salio mal")

            # Devolver error
            return "Sigo esperando"

# Transformar texto en voz
def hablar(mensaje):

    # Encender pyttsx3
    engine = pyttsx3.init()

    # Leer mensaje
    engine.say(mensaje)
    engine.runAndWait()

# Informar dia de la semana
def pedir_dia():
    dia = datetime.date.today()
    print(dia)

    dia_semana = dia.weekday()
    print(dia_semana)

    calendario ={0:'Lunes', 1:'Martes', 2:'Miercoles', 3:'Jueves', 4:'Viernes', 5:'Sabado', 6:'Domingo'}

    hablar(f'Hoy es {calendario[dia_semana]}')

# Informar hora
def pedir_hora():
    hora = datetime.datetime.now()
    hora = f'En este momento son las {hora.hour} horas con {hora.minute} minutos'
    hablar(hora)

# Saludo inicial
def saludo_inicial():

    momento_dia = datetime.datetime.now()
    if momento_dia.hour < 6 or momento_dia.hour > 20:
        momento = 'Buenas noches'
    elif momento_dia.hour >= 6 or momento_dia.hour < 12:
        momento = 'Buen día'
    else:
        momento = 'Buenas tardes'

    hablar(f'Hola, {momento}, soy Jarvis, tu asistente personal. Dime en que te puedo ayudar')

#! Main
def pedir_cosas():

    saludo_inicial()

    comenzar = True
    while comenzar:
        # Activar el microfono y guardar pedido
        pedido = trasformar_audio_texto().lower()
        
        if 'abrir youtube' in pedido:
            hablar('Con gusto, estoy abriendo youtube')
            webbrowser.open('https://www.youtube.com')
            continue
        elif 'abrir un navegador' in pedido:
            hablar('Claro, estoy en eso')
            webbrowser.open('https://www.google.com')
            continue
        elif 'qué día es hoy' in pedido:
            pedir_dia()
            continue
        elif 'qué hora es' in pedido:
            pedir_hora()
            continue
        elif 'buscar en wikipedia' in pedido:
            hablar('Lo buscare en wikipedia')
            pedido = pedido.replace('buscar en wikipedia', '')
            wikipedia.set_lang('es')
            resultado = wikipedia.summary(pedido, sentences = 1)
            hablar('Segun wikipedia: ')
            hablar(resultado)
            continue
        elif 'buscar en internet' in pedido:
            hablar('Lo hare')
            pedido = pedido.replace('buscar en internet', '')
            pywhatkit.search(pedido)
            hablar(f'Esto encontre en internet sobre {pedido}')
            continue
        elif 'reproducir' in pedido:
            hablar('En seguida')
            pedido = pedido.replace('reproducir', '')
            pywhatkit.playonyt(pedido)
            continue
        elif 'broma' in pedido:
            hablar('Ahi te va uno bueno')
            hablar(pyjokes.get_joke('es'))
            continue
        elif 'precio de las acciones' in pedido:
            accion = pedido.split('de')[-1].strip()
            cartera = {'apple':'APPL', 'amazon':'AMZN', 'google':'GOOGL'}
            try:
                accion_buscada = cartera[accion]
                accion_buscada = yf.Ticker(accion_buscada)
                precio_actual = accion_buscada.info['regularMarketPrice']
                hablar(f'La encontre, el precio de {accion} es {precio_actual}')
                continue
            except:
                hablar('Perdon pero no la he encontrado')
                continue
        elif 'adiós' in pedido:
            hablar("Nos vemos")
            break


pedir_cosas()
