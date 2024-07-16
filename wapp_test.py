import pywhatkit as kit
import datetime
grupo = "..."  #channel
telefono = "+51..." #number
mensaje = "hola, esta es una prueba"
# Enviar el mensaje
for i in range(1):
    hora_actual = datetime.datetime.now().hour
    minuto_actual = datetime.datetime.now().minute + 1 # Agrega 1 minuto para asegurar el envío futuro
    if minuto_actual == 60:
        hora_actual +=1
        minuto_actual = 0
    else:
        pass
    print(hora_actual, minuto_actual)
    mensaje = f"¡mensaje prueba! {hora_actual}:{minuto_actual}"
    kit.sendwhatmsg_to_group(grupo, mensaje, hora_actual, minuto_actual, 15, True, 10)
    print(f"mensaje enviado a {grupo}")
    kit.sendwhatmsg(telefono, mensaje, hora_actual, (minuto_actual+1), 15, True, 10)
    print(f"mensaje enviado a {telefono}")
print(f"Mensajes enviados")