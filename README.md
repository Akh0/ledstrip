<h1 align="center" >
<img src="https://upload.wikimedia.org/wikipedia/commons/8/86/RGB_color_model.svg" width="24" style="vertical-align: middle" />
LED Strip Server/CLI controller
<img src="https://upload.wikimedia.org/wikipedia/fr/thumb/3/3b/Raspberry_Pi_logo.svg/1200px-Raspberry_Pi_logo.svg.png" width="24" style="vertical-align: middle" />
</h1>

HTTP Server and CLI for WS2801 RGB LED strip plugged on a Raspberry Pi.

This program use [Adafruit_CircuitPython_WS2801](https://github.com/adafruit/Adafruit_CircuitPython_WS2801) driver.

## Introduction

Raspberry Pi and WS2801 communicate via the SPI protocol.

The SPI kernel module must be enabled beforehand:

    sudo raspi-config

Go to `3 Interface Options` -> `P4 SPI` -> `Yes` -> Reboot.

## Wiring

| WS2081 LED Strip | Raspberry Pi            | Power Supply |
| ---------------- | ----------------------- | ------------ |
| 5V               | -                       | +V           |
| CK/CI            | Pin 23 (SCKL - GPIO 11) | -            |
| SI/DI            | Pin 19 (MOSI - GPIO 10) | -            |
| GND              | Pin 6 (GND)             | -V or COM    |

## Getting started

- Requirements:

  - python3
  - pip3

- Install:

  - Clone this repository
  - `make install` - Install the dependencies

- Commands:

  - `make start_server` - Start the API server
  - `./cli.py` - Control the LED Strip. Add `--help` argument to see usage.

## JSON API Endpoints

- **GET** `/animations` - Get a key/value object containing all available animations.

- **POST** `/set` - Control the LED Strip by setting a color, a brightness and/or an animation.

  - Parameters:

    - `color` - Hexadecimal color.
    - `brightness` - Brightness in percentage.
    - `animation` - The animation name. The value must be a key of the object returned by the **GET** `/animations` query.

  - Payload examples:

    - Light the LED Strip in red with 80% brightness:

      ```json
      { "color": "FF0000", "brightness": 80 }
      ```

    - Run _Rainbow_ animation with 100% brightness:
      ```json
      { "brightness": 100, "animation": "rainbow" }
      ```

## Configuration

The number of LEDs to control and the port on which the server is running can be configured in the `config.yml` file.
