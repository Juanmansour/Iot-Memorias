# Memoria de Prácticas IoT  -  ESP32 con microPython
## Grupo 2
- Juan Mansour Wehbe
- Laura Muñoz Millán
- Alberto Fernández Merchán
- Sarah Saad

### 5 de Noviembre de 2024
Realizamos una toma de contacto con el dispositivo ESP32 y el lenguaje de programación microPython utilizando el IDE Thonny. Realizamos tres ejemplos en los que:

1. El [primer ejemplo](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%201/Ejemplo1.py), utiliza la librería *asyncio* conseguimos encender y apagar un LED controlando el tiempo de parpadeo con funciones asíncronas.  

2. En el [segundo ejemplo](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%201/Ejemplo2.py), añadimos un temporizador asíncrono a la aplicación para que, al mismo tiempo que enciende y apaga el led, se muestre, por consola, un temporizador que controla el tiempo de ejecución del programa.

3. Por último, en el [tercer ejemplo](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%201/Ejemplo3.py), coordinamos las dos tareas realizadas en el anterior ejercicios para que se realice una detrás de otra utilizando la clase asyncio.Event().


### 6 de Noviembre de 2024

Decidimos utilizar el protocolo de comunicación Mosquitto (MQTT) para realizar la comunicación entre las dos placas ESP32. Para ello necesitamos un brocker que haga de servidor y las dos placas hacen de clientes. Una de las placas publicará en el brocker el dato del sensor y la otra placa, tras subscribirse al tópico donde esté publicado el valor, deberá leerlo. 

Para la primera toma de contacto, nos conectamos al brocker que levanta el profesor en su portátil. Utilizando el siguiente código:

Utilizando un programa de ejemplo, conseguimos publicar datos aleatorios en el brocker, sin embargo, no conseguimos leer de él a pesar de estar suscritos. Para adelantar el trabajo del siguiente día, decidimos conectar un botón como actuador en la placa que publica los datos y conseguimos mandar un '1' cuando está pulsado y un '0' cuando no lo está.


### 19 de Noviembre de 2024
- [x] Instalación de MqttExplorer para lanzar nuestro propio broker desde nuestro portátil personal (conexión al router, cambios en la configuración del fichero .cfg...)
- [x] Conexión con nuestro broker
- [x] Recepción de mensajes con nuestro broker
- [x] Utilización de un botón para mandar una señal al broker
- [x] Activación de LED remota.

### 20 de Noviembre de 2024
- [x] Implementar funciones del día anterior con librerías asíncronas.
- [ ] Esquema circuito
- [ ] Incluir fotos y videos

![IMG_MQTT_OFF](https://github.com/Juanmansour/Iot-Memorias/blob/main/ESP32_imagenes_y_videos/IMG_Communication_OFF.jpg)
![IMG_MQTT_ON](https://github.com/Juanmansour/Iot-Memorias/blob/main/ESP32_imagenes_y_videos/IMG_Communication_ON.jpg)
