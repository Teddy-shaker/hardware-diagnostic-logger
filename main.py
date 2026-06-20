import csv
from pathlib import Path

from device import Device


BASE_DIR = Path(__file__).resolve().parent
DATA_FILE = BASE_DIR / "data" / "devices.csv"
TEXT_REPORT_FILE = BASE_DIR / "reports" / "diagnostic_report.txt"
CSV_REPORT_FILE = BASE_DIR / "reports" / "diagnostic_report.csv"


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


def generate_report(devices, text_report_file=TEXT_REPORT_FILE, csv_report_file=CSV_REPORT_FILE):
    text_report_file.parent.mkdir(parents=True, exist_ok=True)
    csv_report_file.parent.mkdir(parents=True, exist_ok=True)

    report_lines = [
        "Hardware Diagnostic Report",
        "==========================",
        "",
    ]
    report_rows = []

    for device in devices:
        result = device.run_diagnostics()
        report_rows.append(result)
        report_lines.append(f"Device Name: {result['name']}")
        report_lines.append(f"Device Type: {result['device_type']}")
        report_lines.append(f"Status: {result['status']}")
        report_lines.append(f"Reason: {result['reason']}")
        report_lines.append("")

    text_report_file.write_text("\n".join(report_lines), encoding="utf-8")

    with open(csv_report_file, mode="w", encoding="utf-8", newline="") as file:
        fieldnames = ("name", "device_type", "status", "reason")
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(report_rows)

    return text_report_file, csv_report_file


def main():
    devices = load_devices()
    if not devices:
        return

    text_report_file, csv_report_file = generate_report(devices)
    print(f"Text diagnostic report saved to {text_report_file}.")
    print(f"CSV diagnostic report saved to {csv_report_file}.")


if __name__ == "__main__":
    main()
