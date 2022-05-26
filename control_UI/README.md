# Control UI for RC Car
- run on Raspberry Pi 4B with Raspberry Pi screen
- using PySide2
- with buttons send command to the AWS server
- show status of the car

## send command
- when buttons are clicked, insert command to the DB table
- format:
  - time, cmd_string, arg_string, is_finish
  - time: datetime, string
  - cmd_string: types of command(stop, go, left, right, mid, back), string
  - arg_string: set as "0", string
  - is_finish: set to 0, string

## get sensor data
- get data every 0.3 second
- show 15 current rows from command and sensing table
- show current temperature and humidity
- show currunt state and direction
  - as label
  - as status bar
![UI](https://user-images.githubusercontent.com/74483608/170508910-5435eb13-d59c-442f-9ed4-ac165b75639c.png)
