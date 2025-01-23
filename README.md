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

Este día instalamos la aplicación de MqttExplorer para lanzar nuestro propio broker desde nuestro portátil personal. El proceso se describe en las siguientes imágenes:
![IMG_DOWNLOAD_MQTT1](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%202/1.png)
![IMG_DOWNLOAD_MQTT2](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%202/2.png)
![IMG_DOWNLOAD_MQTT3](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%202/3.png)
![IMG_DOWNLOAD_MQTT4](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%202/4.png)
![IMG_DOWNLOAD_MQTT5](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%202/5.png)
![IMG_DOWNLOAD_MQTT6](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%202/6.png)
![IMG_DOWNLOAD_MQTT7](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%202/7.png)
![IMG_DOWNLOAD_MQTT8](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%202/8.png)

Después hicimos que tanto el emisor como el receptor se conectaran al broker:
![IMG_CONNECTION1](https://github.com/Juanmansour/Iot-Memorias/blob/main/ESP32_imagenes_y_videos/mem3_consol1.png)
![IMG_CONNECTION1](https://github.com/Juanmansour/Iot-Memorias/blob/main/ESP32_imagenes_y_videos/mem3_consol2.png)

Comprobamos en la aplicación de MQTT que estaba todo correcto:
![IMG_CHECK_OK](https://github.com/Juanmansour/Iot-Memorias/blob/main/ESP32_imagenes_y_videos/mem3_mqtt.png)

Por último conseguimos programar que, pulsando un botón en el ESP32, pudiéramos mandar una señal al broker y que el otro módulo ESP32 lo leyese del topic y activar un LED de forma remota.

El código se puede ver en este [enlace](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%203/ESP_1/main.py)

### 20 de Noviembre de 2024
Por último, el cuarto día implementamos el código anterior pero, esta vez, utilizando las funciones asíncronas de la librería de micropython. Los códigos pueden verse en este enlace [enlace](https://github.com/Juanmansour/Iot-Memorias/tree/main/Memorias%204/MQTT).

Los circuitos que utilizamos son los que se pueden ver en las siguientes imágenes:
En primer lugar utilizamos un sensor de movimiento para que el LED se encendiera cuando alguien pasara por delante:
![ESQUEMA_FOTORECEPTOR](https://github.com/Juanmansour/Iot-Memorias/blob/main/ESP32_imagenes_y_videos/mem4_ESP32-emisor_bb.png)

Luego, utilizamos un potenciómetro para regular la intensidad del led del receptor:
![ESQUEMA](https://github.com/Juanmansour/Iot-Memorias/blob/main/ESP32_imagenes_y_videos/mem4-ESP32-pwm_bb.png)
![ESQUEMA_RECEIVER](https://github.com/Juanmansour/Iot-Memorias/blob/main/ESP32_imagenes_y_videos/mem4_ESP32-receptor_bb.png)


Los resultados fueron los siguientes:
![IMG_MQTT_OFF](https://github.com/Juanmansour/Iot-Memorias/blob/main/ESP32_imagenes_y_videos/IMG_Communication_OFF.jpg)
![IMG_MQTT_ON](https://github.com/Juanmansour/Iot-Memorias/blob/main/ESP32_imagenes_y_videos/IMG_Communication_ON.jpg)
