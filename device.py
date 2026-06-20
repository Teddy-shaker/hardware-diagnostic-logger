class Device:
    VOLTAGE_RANGE = (3.0, 5.0)
    TEMPERATURE_LIMITS = (70.0, 85.0)
    CURRENT_LIMIT = 2.5

    def __init__(self, name, device_type, voltage, temperature, current):
        self.name = name
        self.device_type = device_type
        self.voltage = float(voltage)
        self.temperature = float(temperature)
        self.current = float(current)
        self.__status = "NOT RUN"
        self.failure_reason = "Diagnostics have not been run."

    def __set_status(self, status, reason):
        self.__status = status
        self.failure_reason = reason

    def get_status(self):
        return self.__status

    def check_voltage(self):
        minimum_voltage, maximum_voltage = self.VOLTAGE_RANGE
        return minimum_voltage <= self.voltage <= maximum_voltage

    def check_temperature(self):
        warning_temperature, fail_temperature = self.TEMPERATURE_LIMITS

        if self.temperature >= fail_temperature:
            return "FAIL"
        if self.temperature >= warning_temperature:
            return "WARNING"
        return "PASS"

    def _check_current(self):
        return self.current <= self.CURRENT_LIMIT

    def run_diagnostics(self):
        failed_checks = set()
        warning_checks = set()

        if not self.check_voltage():
            failed_checks.add("voltage out of range")

        temperature_result = self.check_temperature()
        if temperature_result == "FAIL":
            failed_checks.add("temperature too high")
        elif temperature_result == "WARNING":
            warning_checks.add("temperature elevated")

        if not self._check_current():
            warning_checks.add("current draw elevated")

        if failed_checks:
            self.__set_status("FAIL", ", ".join(sorted(failed_checks)))
        elif warning_checks:
            self.__set_status("WARNING", ", ".join(sorted(warning_checks)))
        else:
            self.__set_status("PASS", "All diagnostic checks passed.")

        return {
            "name": self.name,
            "device_type": self.device_type,
            "status": self.__status,
            "reason": self.failure_reason,
        }

    def __str__(self):
        return f"{self.name} ({self.device_type}) - {self.__status}: {self.failure_reason}"

    def __eq__(self, other):
        if not isinstance(other, Device):
            return False

        return self.name == other.name and self.device_type == other.device_type
