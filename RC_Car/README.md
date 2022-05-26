# RC_Car running file
- get data from DB(mysql DB) every 0.1 seconds
- according to the command written in DB, 
  - go forward, backward
  - turn left, right
  - stop
- send sensing data to DB every 1 seconds
- when danger zone, send flag, make buzzer ring, change LED to red

## get command
- get 15 current rows from command table

## send sensing data
- temperature, humidity from DHT11 sensor
- gyro x, y,z value from MPU6050
- distance value from ultrasonic sensor(HC-SRO4)
- send danger flag
  - 0: safe zone
  - 1: warning zone where obstacle is within in 10cm
  - 2: danger zone where temperature is under 0 degree Celsius or slop over 30 degree
- format:
  - num1: round(temperature / 100, 2) (unit: degree Celsius)
  - num2: round(humidity / 100, 2) (unit: %)
  - num3: round(distance / 100, 2) (unit: m)
  - meta_string: Gx|Gy|Gz|danger_flag
    - Gi = round(gyro_i / (131.0 * 100), 2) 
    - danger_flag: int
## LED & Buzzer Control
- Normal
  - go forward, backward: LED green, move wheel motor
  - stop: no LED, stop wheel motor
  - turn left, right: LED blue, move servo motor
- Warning
  - LED red
  - Buzzer ring
  - RC Car Stops
- Danger
  - LED red
  - Buzzer rings
  - RC car stops
