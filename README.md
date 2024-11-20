# Memoria de Prácticas IoT  -  ESP32 con microPython
## Grupo 2
- Juan Mansour
- Laura Muñoz
- Alberto Fernández Merchán
- Sarah 

### 5 de Noviembre de 2024
Realizamos una toma de contacto con el dispositivo ESP32 y el lenguaje de programación microPython utilizando el IDE Thonny. Realizamos tres ejemplos en los que:

1. El [primer ejemplo](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%201/Ejemplo1.py), utiliza la librería *asyncio* conseguimos encender y apagar un LED controlando el tiempo de parpadeo con funciones asíncronas.  

2. En el [segundo ejemplo](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%201/Ejemplo2.py), añadimos un temporizador asíncrono a la aplicación para que, al mismo tiempo que enciende y apaga el led, se muestre, por consola, un temporizador que controla el tiempo de ejecución del programa.

3. Por último, en el [tercer ejemplo](https://github.com/Juanmansour/Iot-Memorias/blob/main/Memorias%201/Ejemplo3.py), coordinamos las dos tareas realizadas en el anterior ejercicios para que se realice una detrás de otra utilizando la clase asyncio.Event().


### 6 de Noviembre de 2024

 - [ ] Decisión de protocolo de comunicación (MQTT)
 - [ ] Conexión con el broker del profesor
 - [ ] Publicación de datos en el broker
 - [ ] Recepción de datos en el broker
 - [ ] Utilización de un botón para mandar una señal al broker.

### 19 de Noviembre de 2024
- [ ] Instalación de MqttExplorer para lanzar nuestro propio broker desde nuestro portátil personal (conexión al router, cambios en la configuración del fichero .cfg...)
- [ ] Conexión con nuestro broker
- [ ] Recepción de mensajes con nuestro broker
- [ ] Utilización de un botón para mandar una señal al broker
- [ ] Activación de LED remota.

### 20 de Noviembre de 2024
- [ ] Implementar funciones del día anterior con librerías asíncronas.
