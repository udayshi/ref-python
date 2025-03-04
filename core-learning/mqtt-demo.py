apt-get install mosquitto
apt-get install mosquitto-clients

#Change Conf
/etc/mosquitto/mosquitto.conf

allow_anonymous false
password_file /etc/mosquitto/pwfile
listener [port_to_listen|1883]


#Create user and password
sudo mosquitto_passwd -c /etc/mosquitto/pwfile uday




##Start Server
mosquitto

#Subscribe the topic on Client which you gotta interest
mosquitto_sub -d -u uday -p password -t my_topic
mosquitto_sub -d -t my_topic



#Public the topic from any device
mosquitto_pub -d -t my_topic -m 'this is my msg'


#Python Communication
pip install paho-mqtt

client.py
--------
import paho.mqtt.client as mqtt



def on_connect(mqttc, obj, flags, rc):
    print("rc: " + str(rc))


def on_message(mqttc, obj, msg):
    print(msg.topic + " " + str(msg.qos) + " " + str(msg.payload))


def on_publish(mqttc, obj, mid):
    print("mid: " + str(mid))


def on_subscribe(mqttc, obj, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos))


def on_log(mqttc, obj, level, string):
    print(string)


mqttc=mqtt.Client()
mqttc.on_message = on_message
mqttc.on_connect = on_connect
mqttc.on_publish = on_publish
mqttc.on_subscribe = on_subscribe
# Uncomment to enable debug messages
mqttc.on_log = on_log


#mqttc.username_pw_set(“username”, “password”)
mqttc.connect("127.0.0.1", 1883, 60)
mqttc.subscribe("my_topic", 0)
mqttc.loop_forever()


#######Publish ########
mqtt_publish.py
----------
import paho.mqtt.publish as publish
publish.single("my_topic", "Hey whats up", hostname="127.0.0.1")
