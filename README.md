# 🔌 Industrial Voltage Sensor Calibration System

## 📋 Project Overview

A high-precision voltage sensing and calibration system designed for industrial applications, capable of measuring voltages in the range of **0-1000V DC**. The system features dual polarity support, precision calibration, and STM32-based data acquisition with ADC processing.

## 🎯 Problem Statement

Industrial environments require accurate voltage monitoring across a wide range (0-1000V) with:
- High precision and reliability
- Dual polarity support (positive/negative voltages)
- Real-time data acquisition
- Robust calibration system
- Industrial-grade safety standards

## 💡 Solution Architecture

### System Components
- **Voltage Divider Network**: Precision resistors for safe voltage scaling
- **Signal Conditioning**: Amplification and filtering circuits
- **ADC Interface**: High-resolution analog-to-digital conversion
- **STM32 Controller**: Real-time processing and calibration algorithms
- **Dual Polarity Support**: Configurable via zero-ohm resistor placement

### Block Diagram
```
High Voltage Input (0-1000V) → Voltage Divider → Signal Conditioning → Amplifier → ADC → STM32 Controller
                                      ↓
                              Polarity Selection (Zero-Ohm Resistor)
```

## 🛠️ Technical Specifications

| Parameter | Specification |
|-----------|---------------|
| **Voltage Range** | 0 - 1000V DC |
| **Polarity** | Configurable (±) |
| **Accuracy** | ±0.1% FSR |
| **Resolution** | 12-bit ADC |
| **Response Time** | < 10ms |
| **Operating Temperature** | -20°C to +70°C |
| **Safety Rating** | CAT III 1000V |

## 🔧 Hardware Design

### Key Features
- **Precision Voltage Divider**: Custom-designed resistor network
- **Amplifier Stage**: Low-noise, high-precision operational amplifiers
- **Protection Circuits**: Overvoltage and reverse polarity protection
- **Isolation**: Optical isolation for safety
- **Configurable Polarity**: Hardware-selectable via zero-ohm resistor

### PCB Design
- **Layers**: Multi-layer PCB for noise reduction
- **Components**: Industrial-grade components with appropriate voltage ratings
- **Layout**: Optimized for minimal noise and maximum accuracy
- **Safety**: Proper creepage and clearance distances maintained

## 💻 Software Implementation

### STM32 Firmware Features
- **ADC Configuration**: High-resolution 12-bit ADC with DMA
- **Calibration Algorithm**: Multi-point calibration for linearization
- **Data Processing**: Real-time filtering and averaging
- **Communication**: UART/I2C interface for external systems
- **Error Handling**: Comprehensive fault detection and reporting

### Key Functions
```c
// Core functionality (implementation details proprietary)
void voltage_sensor_init(void);
float read_calibrated_voltage(void);
void perform_calibration(float reference_voltages[], int num_points);
void configure_polarity(polarity_t polarity);
```

## 📊 Calibration Process

1. **Multi-point Calibration**: Using precision voltage references
2. **Linearization**: Polynomial curve fitting for accuracy
3. **Temperature Compensation**: Thermal drift correction
4. **Validation**: Verification against traceable standards

## 🔒 Safety Features

- **Galvanic Isolation**: Complete electrical isolation
- **Overvoltage Protection**: Hardware-based protection circuits
- **Fault Detection**: Continuous monitoring and error reporting
- **Emergency Shutdown**: Immediate disconnection capability

## 📈 Performance Results

| Test Condition | Target | Achieved |
|----------------|---------|----------|
| **Accuracy @ 100V** | ±0.1% | ±0.08% |
| **Accuracy @ 500V** | ±0.1% | ±0.09% |
| **Accuracy @ 1000V** | ±0.1% | ±0.1% |
| **Repeatability** | ±0.05% | ±0.04% |
| **Temperature Drift** | <50ppm/°C | 35ppm/°C |

## 🏭 Industrial Applications

- **Power Quality Monitoring**
- **Motor Drive Systems**
- **Industrial Automation**
- **Test & Measurement Equipment**
- **Renewable Energy Systems**

## 📁 Repository Structure

```
industrial-voltage-sensor-calibration/
├── docs/
│   ├── block-diagrams/
│   ├── pcb-layouts/
│   └── calibration-procedures/
├── firmware/
│   ├── src/
│   ├── inc/
│   └── config/
├── hardware/
│   ├── schematics/
│   ├── pcb-files/
│   └── bom/
├── calibration/
│   ├── procedures/
│   └── test-results/
└── images/
    ├── hardware-photos/
    └── test-setup/
```

## 🚀 Future Enhancements

- **Wireless Communication**: IoT connectivity for remote monitoring
- **Multi-channel Support**: Simultaneous monitoring of multiple voltages
- **Advanced Analytics**: Machine learning for predictive maintenance
- **Cloud Integration**: Data logging and analysis platform

## 🔗 Related Projects

- [STM32 Cooling System](../stm32-cooling-system-firmware) - Advanced temperature control
- [Custom PCB Designs](../custom-pcb-collection) - Hardware design portfolio
- [Industrial IoT Systems](../industrial-iot-portfolio) - Complete automation solutions

## 📞 Contact

**Rivindu Ranasinghe**  
Senior Electronics & Telecommunications Engineer  
📧 [rivindurana@gmail.com]  
🔗 [https://www.linkedin.com/in/rivindu-ranasinghe-150910234/]

---

⚠️ **Note**: This project contains proprietary industrial designs. Specific IC details and complete schematics are not disclosed due to confidentiality agreements. Block diagrams and general implementation details are provided for portfolio demonstration purposes.

⭐ **If you find this project interesting, please give it a star!**
