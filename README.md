# esphome-configs

用于家庭自动化领域的 ESPHome 设备配置文件集合，基于 ESP32-C3 / ESP8266 平台。

## 设备清单

### 485 智能照明模块

通过 TTL/RS485 与主控通信，支持多路继电器控制、环境亮度监测、光敏触发、火警/门磁信号。

| 文件 | 设备 | 芯片 | 说明 |
|------|------|------|------|
| [SmartLightingModule-Illuminance-16.yaml](SmartLightingModule-Illuminance-16.yaml) | 智能照明16 | ESP32-C3 | 16路继电器+亮度监测+光敏触发，最新版本 |
| [LightingModule-Illuminance-16.yaml](LightingModule-Illuminance-16.yaml) | 智能照明16路模块 | ESP32-C3 | 重写版本，增加亮度查询和光敏触发支持 |
| [485-Illuminance-16.yaml](485-Illuminance-16.yaml) | 4路照明模块 | ESP32-C3 | 精简版，4路继电器控制 |

### 毫米波雷达人体存在传感器

基于 Hi-Link LD2412 / LD2410C / LD2402 毫米波雷达，集成 BH1750 光照传感器和 AHT30 温湿度传感器，用于人体存在检测、移动/静止状态识别。

| 文件 | 设备 | 传感器 | 说明 |
|------|------|--------|------|
| [esp32-c3-ld2412.yaml](esp32-c3-ld2412.yaml) | 阳台人存传感器 | LD2412 + BH1750 + AHT30 | 集成光照和温湿度 |
| [esp32-c3-ld2412-bh1750-.yaml](esp32-c3-ld2412-bh1750-.yaml) | 人体环境传感器 | LD2412 + BH1750 | 带 Web Server |
| [esp32-c3-ld2412-kt.yaml](esp32-c3-ld2412-kt.yaml) | LD2412 传感器 (KT) | LD2412 | 另一个部署版本 |
| [ld2412-esp32-c3.yaml](ld2412-esp32-c3.yaml) | 人体雷达传感器 | LD2412 | 基础版 |
| [ld2412-esp32-c3-0.yaml](ld2412-esp32-c3-0.yaml) | LD2412 传感器 | LD2412 | 另一配置 |
| [esp32-c3-ld2410c.yaml](esp32-c3-ld2410c.yaml) | LD2410C 传感器 | LD2410C | - |
| [esp32-c3-ld2410c-2.yaml](esp32-c3-ld2410c-2.yaml) | LD2410C 传感器 v2 | LD2410C | 第二版本 |
| [esp32-c3-ld2402.yaml](esp32-c3-ld2402.yaml) | LD2402 传感器 | LD2402 | - |
| [ld2410-presence-sensor.yaml](ld2410-presence-sensor.yaml) | 存在传感器 | LD2410 | 基础存在检测 |

### 智能开关 / 继电器

支持断电记忆、上电状态选择、物理按键控制、电能计量等功能。

| 文件 | 设备 | 芯片 | 说明 |
|------|------|------|------|
| [8266-3.8.yaml](8266-3.8.yaml) | 磁保继电器插座 | ESP8266 | 断电记忆+电能计量 |
| [esp-8266-2222.yaml](esp-8266-2222.yaml) | 上电状态继电器 | ESP8266 | 上电状态记忆 |
| [esp-8266-kt.yaml](esp-8266-kt.yaml) | ESP8266 通用 | ESP8266 | 通用开关配置 |
| [esp-8266-2.yaml](esp-8266-2.yaml) | ESP8266 开关 | ESP8266 | - |
| [esp8266-1.yaml](esp8266-1.yaml) | ESP8266 开关 | ESP8266 | - |

### 红外控制器

用于红外信号收发的设备，可控制电视、空调、茶吧等红外设备。

| 文件 | 设备 | 芯片 | 说明 |
|------|------|------|------|
| [esp8266-ct30w-kt.yaml](esp8266-ct30w-kt.yaml) | 智能茶吧控制器 | ESP8266 | 红外发射+接收，温度显示，出水倒计时 |
| [esp8266-ct30w-2.yaml](esp8266-ct30w-2.yaml) | 红外发射接收器 | ESP8266 | 支持自定义 IR 服务 (raw/NEC) |

### 其他设备

| 文件 | 设备 | 芯片 | 说明 |
|------|------|------|------|
| [esp-8266-ck.yaml](esp-8266-ck.yaml) | 门禁控制器 | ESP8266 | 继电器+蜂鸣器+物理按钮 |
| [8266-433.yaml](8266-433.yaml) | 433MHz 射频接收器 | ESP8266 | EV1527/PT2262 协议解码 |
| [esp32-c3-dj.yaml](esp32-c3-dj.yaml) | 电调控制器 | ESP32-C3 | 电机电调控制 |
| [esp32-c3-beee.yaml](esp32-c3-beee.yaml) | BLE 蓝牙设备 | ESP32-C3 | 蓝牙 4.2 通信 |
| [c3-.yaml](c3-.yaml) | ESP32-C3 通用 | ESP32-C3 | 通用模板 |

### 参考文档

| 文件 | 说明 |
|------|------|
| [照明时控模块全局设置协议-寄存器位置-.xlsx](照明时控模块全局设置协议-寄存器位置-.xlsx) | 照明时控模块 485 寄存器协议 |
| [键值对应开关.xlsx](键值对应开关.xlsx) | 键值-开关映射表 |
| [esphome_components_list.txt](esphome_components_list.txt) | ESPHome 可用组件列表 |

## 使用方式

1. 安装 [ESPHome](https://esphome.io/)
2. 将 `secrets.yaml` 中的 `wifi_ssid` 和 `wifi_password` 替换为你的 WiFi 信息
3. 编译并烧录：
   ```bash
   esphome run <配置文件名>.yaml
   ```
4. 设备会自动接入 Home Assistant（通过 API 加密连接）

## 硬件平台

- **ESP32-C3** (esp32-c3-devkitm-1, ESP-IDF 框架)
- **ESP8266** (esp01_1m)

## 通用特性

- Home Assistant API 加密通信
- OTA 无线升级
- WiFi 断线自动回连 + 配置热点 (captive portal)
- Web Server（部分设备）
