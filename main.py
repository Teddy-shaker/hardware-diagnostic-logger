import csv
from pathlib import Path

from device import Device


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "devices.csv"
REPORT_FILE = BASE_DIR / "reports" / "diagnostic_report.txt"


def load_devices(csv_file=DATA_FILE):
    devices = []
    required_fields = ("device_name", "device_type", "voltage", "temperature", "current")

    try:
        with open(csv_file, mode="r", encoding="utf-8", newline="") as file:
            reader = csv.DictReader(file)
            for row in reader:
                if not all(field in row and row[field] for field in required_fields):
                    raise ValueError(f"Missing required device data: {row}")

                device_info = {
                    "name": row["device_name"],
                    "device_type": row["device_type"],
                    "voltage": row["voltage"],
                    "temperature": row["temperature"],
                    "current": row["current"],
                }
                devices.append(Device(**device_info))
    except (FileNotFoundError, ValueError) as error:
        print(f"Could not load devices: {error}")
    else:
        print(f"Loaded {len(devices)} devices from {csv_file}.")

    return devices


def generate_report(devices, report_file=REPORT_FILE):
    report_file.parent.mkdir(parents=True, exist_ok=True)

    report_lines = [
        "Hardware Diagnostic Report",
        "==========================",
        "",
    ]

    for device in devices:
        result = device.run_diagnostics()
        report_lines.append(f"Device Name: {result['name']}")
        report_lines.append(f"Device Type: {result['device_type']}")
        report_lines.append(f"Status: {result['status']}")
        report_lines.append(f"Reason: {result['reason']}")
        report_lines.append("")

    report_file.write_text("\n".join(report_lines), encoding="utf-8")
    return report_file


def main():
    devices = load_devices()
    if not devices:
        return

    report_file = generate_report(devices)
    print(f"Diagnostic report saved to {report_file}.")


if __name__ == "__main__":
    main()
