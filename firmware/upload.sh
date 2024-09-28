#!/bin/bash

set -xe

export AMPY_PORT=/dev/ttyACM0
export AMPY_BAUD=115200

ampy put main.py main.py
ampy put my_config.py my_config.py
ampy mkdir --exists-okay utelegram
ampy put utelegram/utelegram.py utelegram/utelegram.py
