import re
import random

def get_respuesta(input_usuario):
    mensaje = re.split(r'\s|[,:;.?!-_]\s*', input_usuario.lower())
    respuesta = check_mensajes(mensaje)
    return respuesta

def probabilidad_mensaje(mensaje_usuario, palabras_reconocidas = [], respuesta_simple = False, palabras_requeridas = []):
    certeza = 0
    tiene_palabras_requeridas = True

    for palabra in mensaje_usuario:
        if palabra in palabras_reconocidas:
            certeza += 1

    porcentaje = int(float(certeza) / float(len(palabras_reconocidas)) * 100)

    for palabra in palabras_requeridas:
        if palabra not in mensaje_usuario:
            tiene_palabras_requeridas = False
            break

    if tiene_palabras_requeridas or respuesta_simple:
        return porcentaje
    else:
        return 0

def check_mensajes(mensaje):
        mayor_prob = {}

        def respuesta(bot_respuesta, lista_palabras = [], respuesta_simple = False, palabras_requeridas = []):
            nonlocal mayor_prob
            mayor_prob[bot_respuesta] = probabilidad_mensaje(mensaje, lista_palabras, respuesta_simple, palabras_requeridas)

        respuesta('¡Hola soy Marco, tu asistente de Fixer!', ['hola', 'saludos', 'buenas'], respuesta_simple = True)
        respuesta('¡Estoy muy bien!¿En que puedo ayudarte hoy?', ['como', 'estas', 'va', 'vas', 'sientes'], palabras_requeridas = ['como'])
        respuesta('¡No hay de que! No dudes en decirme si necesitas algo mas', ['gracias', 'te lo agradezco', 'muchas gracias'], respuesta_simple = True)

        best_match = max(mayor_prob, key = mayor_prob.get)
        print(mayor_prob)

        return unknown() if mayor_prob[best_match] < 1 else best_match

def unknown():
    respuesta = ['No entiendo a que te referis ¿Podes repetirlo?', 'No estoy seguro de lo queres'][random.randrange(2)]
    return respuesta

while True:
    print("Marco: " + get_respuesta(input('Yo: ')))