# components/xra2413mt/sensor.py

import esphome.codegen as cg
import esphome.config_validation as cv
from esphome.components import sensor, uart
from esphome.const import (
    CONF_ID,
    UNIT_EMPTY,
    DEVICE_CLASS_EMPTY,
    STATE_CLASS_MEASUREMENT,
    ICON_EMPTY,
)

DEPENDENCIES = ["uart"]

xra2413mt_ns = cg.esphome_ns.namespace("xra2413mt")
XRA2413MT = xra2413mt_ns.class_("XRA2413MT", cg.Component, uart.UARTDevice)

# 为每个 sensor 定义单独的变量（可选，但推荐，便于后续扩展）
CONF_MAX_MOVE_DISTANCE = "max_move_distance"
CONF_MAX_STATIC_DISTANCE = "max_static_distance"
CONF_UNATTENDED_DURATION = "unattended_duration"
CONF_MOVE_SENSITIVITY = "move_sensitivity"
CONF_STATIC_SENSITIVITY = "static_sensitivity"

# 主组件的 CONFIG_SCHEMA（用户在 YAML 中配置这个）
CONFIG_SCHEMA = cv.All(
    cv.Schema(
        {
            cv.GenerateID(): cv.declare_id(XRA2413MT),
            cv.Required("uart_id"): cv.use_id(uart.UARTComponent),
            # 可选：在这里添加其他配置参数（目前你的类没有额外参数）
            cv.Optional(CONF_MAX_MOVE_DISTANCE): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_EMPTY,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_MAX_STATIC_DISTANCE): sensor.sensor_schema(
                unit_of_measurement=UNIT_EMPTY,
                icon=ICON_EMPTY,
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_UNATTENDED_DURATION): sensor.sensor_schema(
                unit_of_measurement="s",
                icon="mdi:timer-sand",
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_MOVE_SENSITIVITY): sensor.sensor_schema(
                unit_of_measurement="%",
                icon="mdi:motion-sensor",
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
            cv.Optional(CONF_STATIC_SENSITIVITY): sensor.sensor_schema(
                unit_of_measurement="%",
                icon="mdi:account-sensor",
                accuracy_decimals=0,
                device_class=DEVICE_CLASS_EMPTY,
                state_class=STATE_CLASS_MEASUREMENT,
            ),
        }
    )
    .extend(cv.COMPONENT_SCHEMA)
    .extend(uart.UART_DEVICE_SCHEMA)
)


async def to_code(config):
    var = cg.new_Pvariable(config[CONF_ID])
    await cg.register_component(var, config)
    await uart.register_uart_device(var, config)

    # 为每个 sensor 创建并注册（如果用户在 YAML 中定义了该 sensor）
    if CONF_MAX_MOVE_DISTANCE in config:
        sens = await sensor.new_sensor(config[CONF_MAX_MOVE_DISTANCE])
        cg.add(var.set_max_move_distance_sensor(sens))  # 需要在 C++ 中添加 setter

    if CONF_MAX_STATIC_DISTANCE in config:
        sens = await sensor.new_sensor(config[CONF_MAX_STATIC_DISTANCE])
        cg.add(var.set_max_static_distance_sensor(sens))

    if CONF_UNATTENDED_DURATION in config:
        sens = await sensor.new_sensor(config[CONF_UNATTENDED_DURATION])
        cg.add(var.set_unattended_duration_sensor(sens))

    if CONF_MOVE_SENSITIVITY in config:
        sens = await sensor.new_sensor(config[CONF_MOVE_SENSITIVITY])
        cg.add(var.set_move_sensitivity_sensor(sens))

    if CONF_STATIC_SENSITIVITY in config:
        sens = await sensor.new_sensor(config[CONF_STATIC_SENSITIVITY])
        cg.add(var.set_static_sensitivity_sensor(sens))