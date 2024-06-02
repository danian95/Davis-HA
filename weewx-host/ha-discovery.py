#!/bin/python
# coding: utf-8
"""
Configure home assistant discovery to identify Davis Vantage Vue sensors
"""

# MQTT username info
username="MQTT_USERNAME"
password="MQTT_PASSWORD"
hostname="MQTT_HOST_IP"
port="MQTT_PORT"

# Device configuration
device = {
        "cu": "CONFIGURATION_IP",
        "ids": ["vantage_vue_1"],
        "name": "Weather Station",
        "mf": "Davis Instruments",
        "mdl": "Vantage Vue",
        }

# State topic
topic="weather"

import paho.mqtt.client as mqtt
import cjson as json

mc = mqtt.Client(client_id="weewx",clean_session=False)

# Set the user and password;
mc.username_pw_set(username,password=password)

# Open the connection
mc.connect(hostname,port)
mc.loop_start()

# Apparent Temperature
key = "appTemp_F"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Apparent Temperature"
conf['dev_cla'] = "temperature"
conf['unit_of_measurement'] = chr(176) + "F"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Barometer
key = "barometer_inHg"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Barometer"
conf['dev_cla'] = "pressure"
conf['uniq_id'] = key
conf['unit_of_measurement'] = "inHg"
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(3, default = 0) }}"
conf['icon'] = "mdi:gauge"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Cloud base
key = "cloudbase_foot"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Cloud Base"
conf['dev_cla'] = "distance"
conf['uniq_id'] = key
conf['unit_of_measurement'] = "ft"
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(0, default = 0) }}"
conf['icon'] = "mdi:cloud-upload"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Console Battery
key = "consBatteryVoltage_volt"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Console Battery"
conf['unit_of_measurement'] = "V"
conf['dev_cla'] = "voltage"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['icon'] = "mdi:battery"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Day Rain
key = "dayRain_in"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Day Rain"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['state_class'] = "total_increasing"
conf['unit_of_measurement'] = "in"
conf['icon'] = "mdi:weather-rainy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Dewpoint
key = "dewpoint_F"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Dewpoint"
conf['unit_of_measurement'] = chr(176) + "F"
conf['dev_cla'] = "temperature"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Forecast Icon
key = "forecastIcon"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Forecast Icon"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | int }}"
conf['entity_category'] = "diagnostic"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Forecast Rule
key = "forecastRule"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Forecast Rule"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | int }}"
conf['entity_category'] = "diagnostic"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Heat Index
key = "heatindex_F"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Heat Index"
conf['dev_cla'] = "temperature"
conf['unit_of_measurement'] = chr(176) + "F"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Hour Rain
key = "hourRain_in"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Hour Rain"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "total_increasing"
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['unit_of_measurement'] = "in"
conf['icon'] = "mdi:weather-rainy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Humidex
key = "humidex_F"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Humidex"
conf['dev_cla'] = "temperature"
conf['unit_of_measurement'] = chr(176) + "F"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Indoor Dewpoint
key = "inDewpoint_F"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Indoor Dewpoint"
conf['dev_cla'] = "temperature"
conf['unit_of_measurement'] = chr(176) + "F"
conf['icon'] = "mdi:home-thermometer"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Indoor Humidity
key = "inHumidity"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Indoor Humidity"
conf['dev_cla'] = "humidity"
conf['unit_of_measurement'] = "%"
conf['icon'] = "mdi:water-percent"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Indoor Temperature
key = "inTemp_F"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Indoor Temperature"
conf['dev_cla'] = "temperature"
conf['unit_of_measurement'] = chr(176) + "F"
conf['icon'] = "mdi:home-thermometer"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Month Rain
key = "monthRain_in"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Month Rain"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "total_increasing"
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['unit_of_measurement'] = "in"
conf['icon'] = "mdi:weather-rainy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Outdoor Humidity
key = "outHumidity"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Outdoor Humidity"
conf['dev_cla'] = "humidity"
conf['unit_of_measurement'] = "%"
conf['icon'] = "mdi:water-percent"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Outdoor Temperature
key = "outTemp_F"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Outdoor Temperature"
conf['dev_cla'] = "temperature"
conf['unit_of_measurement'] = chr(176) + "F"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# 15 Min Rain Accumulations
key = "rain15"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis 15 Min Rain"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['state_class'] = "measurement"
conf['unit_of_measurement'] = "in"
conf['icon'] = "mdi:weather-rainy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# 15 Min Rain Accumulations
key = "rain15"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis 15 Min Rain"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['state_class'] = "measurement"
conf['unit_of_measurement'] = "in"
conf['icon'] = "mdi:weather-rainy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# 24 Hr Rain Accumulations
key = "rain24_in"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis 24 Hour Rain"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['state_class'] = "measurement"
conf['unit_of_measurement'] = "in"
conf['icon'] = "mdi:weather-rainy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Rain
key = "rain_in"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Rain"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['state_class'] = "total_increasing"
conf['unit_of_measurement'] = "in"
conf['icon'] = "mdi:weather-rainy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Rain Rate
key = "rainRate_inch_per_hour"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Rain Rate"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['state_class'] = "measurement"
conf['unit_of_measurement'] = "in/hr"
conf['icon'] = "mdi:weather-rainy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Storm Rain
key = "stormRain_in"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Storm Rain"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['state_class'] = "total_increasing"
conf['unit_of_measurement'] = "in"
conf['icon'] = "mdi:weather-rainy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Sunrise
key = "sunrise"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Sunrise"
conf['dev_cla'] = "timestamp"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | int | timestamp_local }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Sunset
key = "sunset"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Sunset"
conf['dev_cla'] = "timestamp"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | int | timestamp_local }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Barometer Trend Icon
key = "trendIcon"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Barometer Trend Icon"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
#conf['value_template'] = "{% if value | int == -60) %} \
#Falling Rapidly \
#{% elif value | int == -20) %} \
#Falling Slowly \
#{% elif value | int == 0) %} \
#Steady \
#{% elif value | int == 20) %} \
#Rising Slowly \
#{% elif value | int == 60) %} \
#Rising Rapidly \
#{% else %} \
#-- \
#{% endif %}"
conf['entity_category'] = "diagnostic"
conf['value_template'] = "{{ value | int }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Transmitter Battery
key = "txBatteryStatus"
conf = dict()
tpc = 'homeassistant/binary_sensor/weewx/' + key + '/config'
conf['name'] = "Davis Transmitter Battery Status"
conf['dev_cla'] = "battery"
conf['pl_on'] = "1.0"
conf['pl_off'] = "0.0"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Wind Chill
key = "windchill_F"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Wind Chill"
conf['dev_cla'] = "temperature"
conf['unit_of_measurement'] = chr(176) + "F"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Wind Direction
key = "windDir"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Wind Direction"
conf['unit_of_measurement'] = chr(176)
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(0, default = 0) }}"
conf['icon'] = "mdi:weather-windy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Wind Gust 10 Min Average
key = "windGust10"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis 10 Min Wind Gust"
conf['unit_of_measurement'] = "mph"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['icon'] = "mdi:weather-windy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Wind Gust Direction
key = "windGustDir"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Wind Gust Direction"
conf['unit_of_measurement'] = chr(176)
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(0, default = 0) }}"
conf['icon'] = "mdi:weather-windy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Wind Gust Direction 10 Min Average
key = "windGustDir10"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis 10 Min Wind Gust Direction"
conf['unit_of_measurement'] = chr(176)
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(0, default = 0) }}"
conf['icon'] = "mdi:weather-windy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Wind Gust
key = "windGust_mph"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Wind Gust"
conf['unit_of_measurement'] = "mph"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['icon'] = "mdi:weather-windy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Wind Speed 10 Min Average
key = "windSpeed10_mph"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis 10 Min Wind Speed"
conf['unit_of_measurement'] = "mph"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['icon'] = "mdi:weather-windy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Wind Speed 2 Min Average
key = "windSpeed2"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis 2 Min Wind Speed"
conf['unit_of_measurement'] = "mph"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['icon'] = "mdi:weather-windy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Wind Speed
key = "windSpeed_mph"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Wind Speed"
conf['unit_of_measurement'] = "mph"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(1, default = 0) }}"
conf['icon'] = "mdi:weather-windy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Day Rain
key = "yearRain_in"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Year Rain"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['state_class'] = "measurement"
conf['unit_of_measurement'] = "in"
conf['icon'] = "mdi:weather-rainy"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Signal Quality
key = "rxCheckPercent"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Signal Quality"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['state_class'] = "measurement"
conf['value_template'] = "{{ value | round(2, default = 0) }}"
conf['unit_of_measurement'] = "%"
conf['icon'] = "mdi:antenna"
conf['entity_category'] = "diagnostic"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)

# Storm Start
key = "stormStart"
conf = dict()
tpc = 'homeassistant/sensor/weewx/' + key + '/config'
conf['name'] = "Davis Storm Start"
conf['dev_cla'] = "timestamp"
conf['uniq_id'] = key
conf['state_topic'] = topic + '/' + key
conf['value_template'] = "{{ value | int | timestamp_local }}"
conf['device'] = device
mc.publish(tpc, json.encode(conf), retain=True)



# Close the connection
mc.loop_stop()
mc.disconnect()
