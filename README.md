# Raspbery pi webcam

## 1. Setup MJPG-Streamer

Install dependcies:

```sh
sudo apt-get install cmake libjpeg9-dev
```

Download package:

```sh
wget https://github.com/jacksonliam/mjpg-streamer/archive/master.zip
```

Build and install:

```sh
unzip master.zip && cd mjpg-streamer-master/mjpg-streamer-experimental
make && sudo make install
```

Test MJPT-Stramer:

```sh
/usr/local/bin/mjpg_streamer -i "/usr/local/lib/mjpg-streamer/input_uvc.so -n -f 10 -r 1280x720" -o "/usr/local/lib/mjpg-streamer/output_http.so -p 8084 -w /usr/local/share/mjpg-streamer/www
```

Setup script:

```sh
#!/bin/bash

# adjust these
INPUT_PLUGIN="/usr/local/lib/mjpg-streamer/input_uvc.so";
DEVICE="/dev/video0";
FRAMES="10";
RESOLUTION="1280x720";

OUTPUT_PLUGIN="/usr/local/lib/mjpg-streamer/output_http.so";
PORT="8084";

# the following are defaults and should not need to be changed
EXEC="/usr/local/bin/mjpg_streamer"
WEB_DIR="/usr/local/share/mjpg-streamer/www";

# mjgp_streamer often does not start on first try. Why ?
start_streamer(){
    for i in {1..5}    # try up to 5 times
    do
        ${EXEC} -b -i "${INPUT_PLUGIN} -n -d ${DEVICE} -f ${FRAMES} -r ${RESOLUTION}" -o "${OUTPUT_PLUGIN} -p ${PORT} -w ${WEB_DIR}"  > /dev/null 2>&1
        sleep $((1+i)) # waiting progressively longer
        if pgrep mjpg_streamer > /dev/null
        then
          echo "mjpg_streamer started"
          return
        fi
    done
    echo "could not start mjpg_streamer"
}

# Carry out specific functions when asked to by the system
case "$1" in
        start)
                if pgrep mjpg_streamer > /dev/null
                then
                    echo "mjpg_streamer already running"
                else
                    start_streamer
                fi
                ;;
        stop)
                if pgrep mjpg_streamer > /dev/null
                then
                    killall mjpg_streamer
                    echo "mjpg_streamer stopped"
                else
                    echo "mjpg_streamer is not running"
                fi
                ;;
        restart)
                if pgrep mjpg_streamer > /dev/null
                then
                    killall mjpg_streamer
                    echo "mjpg_streamer stopped"
                else
                    echo "mjpg_streamer is not running"
                fi
                start_streamer
                ;;
        status)
                pid=`ps -A | grep mjpg_streamer | grep -v "grep" | grep -v mjpg_streamer. | awk '{print $1}' | head -n 1`
                if [ -n "$pid" ];
                then
                        echo "mjpg_streamer is running with pid ${pid}"
                        echo "mjpg_streamer was started with the following command line"
                        cat /proc/${pid}/cmdline ; echo ""
                else
                        echo "mjpg_streamer is not running"
                fi
                ;;
        *)
                echo "Usage: $0 {start|stop|restart|status}"
                exit 1
                ;;
esac
exit 0
```

Grant permission:

```sh
chmod u+x ~/.local/bin/mjpg-streamer
```

Add script to crontab:

```sh
@reboot /home/pi/.local/bin/mjpg-streamer start && sleep 5 && /home/pi/.local/bin/mjpg-streamer restart
```

Reboot and open server at [http://localhost:8084](http://localhost:8084)

## 2. Setup telegram bot

Install packages:

```sh
pip install -r requirements.txt
```

Build binary:

```sh
pyinstaller --onefile --distpath . telegramBot.py
```

Execute binary:

```sh
./telegramBot
```

Create a service:

```text
[Unit]
Description=Telegram snapshot bot
After=network.target
StartLimitIntervalSec=0

[Service]
Type=simple
Restart=always
RestartSec=1
User=vista
ExecStart=/home/vista/Projects/webcam/telegramBot

[Install]
WantedBy=multi-user.target
```

Enable service:

```sh
sudo systemctl enable telegramBot
```

Start service:

```sh
sudo systemctl start telegramBot
```

## 3. Useful links

- [Pyinstaller usage](https://pyinstaller.org/en/stable/usage.html)
- [Telegram send_photo API](https://docs.python-telegram-bot.org/en/stable/telegram.bot.html#telegram.Bot.sendPhoto)
- [MJPG-Streamer setup example](https://www.sigmdel.ca/michel/ha/rpi/streaming_en.html)
- [Raspberr pi using usb webcam tutorial](https://raspberrypi-guide.github.io/electronics/using-usb-webcams)
