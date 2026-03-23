#include "esphome/core/component.h"
#include "esphome/components/uart/uart.h"
#include "esphome/components/sensor/sensor.h"

#include <vector>

namespace xra2413mt {

class XRA2413MT : public esphome::Component, public esphome::uart::UARTDevice {
 public:
  XRA2413MT() = default;  // 无需显式传 parent，UARTDevice 会通过 register_uart_device 设置

  void setup() override {
    // 可选：初始化一些东西
  }

  void loop() override {
    while (available() > 0) {
      bytes_.push_back(read());

      if (bytes_.size() < 8) continue;

      if (bytes_[0] != 0xFD) {
        bytes_.clear();
        continue;
      }

      // 等待完整帧（假设固定长度 34 字节）
      if (bytes_.size() < 34) continue;

      if (bytes_.size() == 34) {
        // 简单校验：检查命令字 0x61 0x01（读取配置响应）
        if (bytes_[6] == 0x61 && bytes_[7] == 0x01) {
          // 发布数据（如果 sensor 指针有效）
          if (max_move_distance_sensor_) {
            max_move_distance_sensor_->publish_state(bytes_[12]);
          }
          if (max_static_distance_sensor_) {
            max_static_distance_sensor_->publish_state(bytes_[13]);
          }
          if (move_sensitivity_sensor_) {
            move_sensitivity_sensor_->publish_state(bytes_[14]);
          }
          if (static_sensitivity_sensor_) {
            static_sensitivity_sensor_->publish_state(bytes_[23]);
          }
          if (unattended_duration_sensor_) {
            uint16_t duration = (bytes_[29] << 8) | bytes_[28];  // 大端序假设，根据实际协议调整
            unattended_duration_sensor_->publish_state(duration);
          }
        }
        bytes_.clear();
      } else {
        // 帧太长，清空
        bytes_.clear();
      }
    }
  }

  // Setter 方法（必须 public）
  void set_max_move_distance_sensor(esphome::sensor::Sensor *sensor) {
    max_move_distance_sensor_ = sensor;
  }
  void set_max_static_distance_sensor(esphome::sensor::Sensor *sensor) {
    max_static_distance_sensor_ = sensor;
  }
  void set_unattended_duration_sensor(esphome::sensor::Sensor *sensor) {
    unattended_duration_sensor_ = sensor;
  }
  void set_move_sensitivity_sensor(esphome::sensor::Sensor *sensor) {
    move_sensitivity_sensor_ = sensor;
  }
  void set_static_sensitivity_sensor(esphome::sensor::Sensor *sensor) {
    static_sensitivity_sensor_ = sensor;
  }

 protected:
  std::vector<uint8_t> bytes_;

  esphome::sensor::Sensor *max_move_distance_sensor_{nullptr};
  esphome::sensor::Sensor *max_static_distance_sensor_{nullptr};
  esphome::sensor::Sensor *unattended_duration_sensor_{nullptr};
  esphome::sensor::Sensor *move_sensitivity_sensor_{nullptr};
  esphome::sensor::Sensor *static_sensitivity_sensor_{nullptr};
};

}  // namespace xra2413mt