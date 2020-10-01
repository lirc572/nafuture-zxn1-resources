# nafuture-zxn1-resources

Resources for Nafuture ZhiXi-N1

English | [简体中文](./README.zh-CN.md)

## Introduction

The Nafuture Zhixi-N1 is a low cost temperature and humidity sensor produced by [Nafuture](http://www.nafuture.cn/) (discontinued). It feafures an ESP-12F module (ESP8266), a DHT11 temerature sensor and **2** 200mAh LiPo batteries. It has a micro-USB port that you can use to charge the batteries and re-program the ESP-12F module with a custom UART programmer.

You can get one from Taobao for only 4.9 CNY.

## On-Board Components

- 1 X ESP-12F (with an LED)
- 1 x DHT11
- 2 x 200mAh LiPo batteries
- 1 additional LED
- 1 x push switch

## Pinout References

|   Pin   |          Connected to          |
|:-------:|:------------------------------:|
|  GPIO12 |            Main LED            |
|  GPIO4  |              DHT11             |
|  GPIO2  |           ESP-12F LED          |
|   ADC   |  VCC through a voltage divider |

## MicroPython Code

## Where to Buy

- [Taobao link for the Nafuture ZhiXi-N1](https://m.tb.cn/h.Vzupfv7?sm=34d8ae)
- [Xianyu link for the programmer](https://market.m.taobao.com/app/idleFish-F2e/widle-taobao-rax/page-detail?wh_weex=true&wx_navbar_transparent=true&id=626032002165&ut_sk=1.X23p8dbHZsEDAI2wCPftXkIY_21407387_1601553035380.Copy.detail.626032002165.3586168982&forceFlush=1)
