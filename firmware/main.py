from machine import Pin
keepalive = Pin(0, Pin.OUT)
keepalive.on() # set keepalive pin as soon as possible


from time import sleep
import network
import utelegram.utelegram as utelegram
import my_config


led = Pin("LED", Pin.OUT)
led.on()


def connect():
    #Connect to WLAN
    wlan = network.WLAN(network.STA_IF)
    print(f"MAC: {wlan.config('mac').hex()}")
    wlan.active(True)
    if not wlan.isconnected():
        try:
            wlan.connect(my_config.wifi_config['ssid'], my_config.wifi_config['pass'])
        except OSError:
            return False
    while wlan.isconnected() == False:
        print('Waiting for connection...')
        sleep(1)
    ip = wlan.ifconfig()[0]
    print(f'Connected on {ip}')
    return True


def send_message():
    bot = utelegram.ubot(my_config.telegram_config['token'])
    if bot.send(my_config.telegram_config['chat_id'], my_config.telegram_config['text']):
        return True
    else:
        for _ in range(20):
            led.toggle()
            sleep(0.2)
        return False
        

def main():
    while True:
        sleep(1)
        try:
            if not connect():
                continue
            if send_message():
                return 0
        except KeyboardInterrupt:
            return 0
        except:
            continue
    

if __name__ == "__main__":
    main()
    led.off()
    keepalive.off()