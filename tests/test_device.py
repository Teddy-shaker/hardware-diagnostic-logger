import unittest
from pathlib import Path
import sys

PROJECT_ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(PROJECT_ROOT))

from device import Device


class TestDevice(unittest.TestCase):
    def test_device_passes_all_diagnostics(self):
        device = Device("Controller-A", "Microcontroller", 3.3, 42.5, 1.1)
        same_device = Device("Controller-A", "Microcontroller", 3.3, 42.5, 1.1)

        result = device.run_diagnostics()

        assert result["status"] == "PASS"
        assert device.get_status() == "PASS"
        assert "Controller-A" in str(device)
        assert device == same_device

    def test_device_fails_when_voltage_is_out_of_range(self):
        device = Device("Motor-Driver-B", "Motor Driver", 5.2, 66.0, 2.2)

        result = device.run_diagnostics()

        assert result["status"] == "FAIL"
        assert result["reason"] == "voltage out of range"


if __name__ == "__main__":
    unittest.main()
