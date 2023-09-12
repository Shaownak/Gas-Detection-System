import time 
import paho.mqtt.client as mqtt

# Flags for Connection 
def on_connect(client, userdata, flags, rc):
   global Flag
   Flag = True
   client_subscriptions(client)
   print("Connected to MQTT server")

#If Disconnected
def on_disconnect(client, userdata, rc):
   global Flag
   Flag = False
   print("Disconnected from MQTT server")


def callback_esp32_1(client, userdata, msg):
   print("Esp_1",str(msg.payload.decode('utf-8')))
   return str(msg.payload.decode('utf-8'))


def callback_esp32_2(client, userdata, msg):
   print("Esp_2",str(msg.payload.decode('utf-8')))
   return str(msg.payload.decode('utf-8'))


def callback_esp32_3(client, userdata, msg):
   print("Esp_3",str(msg.payload.decode('utf-8')))
   return str(msg.payload.decode('utf-8'))

# Subscribe to topics for Esp32_nodes
def client_subscriptions(client):
   # Name of the Topics
   client.subscribe("esp32/1")
   client.subscribe("esp32/2")
   client.subscribe("esp32/3")


client = mqtt.Client("Pi_mqtt_broker")

#Global Variable for Connections
Flag = False

client.on_connect    = on_connect
client.on_disconnect = on_disconnect

client.message_callback_add("esp/1", callback_esp32_1)
client.message_callback_add("esp/2", callback_esp32_2)
client.message_callback_add("esp/3", callback_esp32_3)

#connect to Host ip
client.connect('91.121.93.94', 1883)

client.loop_start()
client_subscriptions(client)
print("Fininshed with Setting up MQtt Network")

# Esp32_1 = dict(callback_esp32_1)
# Esp32_2 = dict(callback_esp32_2)
# Esp32_3 = dict(callback_esp32_3)
#The format of ESP32_1 Should be = {"mq2": value, "mq6": value} 

#DATA parsing and Mainting if its more then threshold
def threshold(dict_data):
   pass
#GSM 
def gsm(value):
   pass

#Gas valve
def gasValve(trigger):
   pass









while True:
    time.sleep(4)
    if (Flag != True):
        print("trying to connect MQTT server..")
        