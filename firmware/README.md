# Wassermelder firmware

This water alarm is running on a *Raspberry Pi Pico W* using [MicroPython](https://micropython.org/download/RPI_PICO_W/).


## Preparation
Before loading the firmware to the Pico W, there are a few steps to do.

### 1. Flash MicroPython to the Pico W
Flash the latest MicroPyhton firmware to the Pico W. This step has do be done only once.
1. Go to [https://micropython.org/download/RPI_PICO_W/](https://micropython.org/download/RPI_PICO_W/) and download the latest MicroPython .u2f binary.
2. Keep the button "BOOTSEL" pressed while connecting the Pico W to the computer. It will show up as a USB mass storage device.
3. Then simply copy the .u2f file to the Pico W. The Pico W will dismount once the proccess is complete.

### 2. Add WiFi and Telegram credentials
Rename the file `my_config.py.example` to `my_config.py` and add your WiFi credentials as well as your Telegram token, chat id and alarm message.

### 3. Install ampy (optional)
I use Adafruit's tool **ampy** (adafruit-ampy) to copy the python files to the Pico W. You can install it with:
``` bash
pip install -r requirements.txt
```

## Uploading the firmware

You can use the `upload.sh` bash script to upload the program files to the Pico W. 
You may need to modify the `AMPY_PORT` for your system.