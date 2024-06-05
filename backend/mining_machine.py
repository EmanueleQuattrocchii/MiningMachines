import json

class MiningMachine:
    hostname: str
    ip_address: str
    SerialNumber: str
    hash_rates: list
    mac: str
    ActiveWorker: str
    temps: list
    hash_rates: list

    def __init__(self, ip_address: str, hostname: str, mac: str, temps: list, hash_rates: list) -> None:
        self.ip_address = ip_address
        self.SerialNumber = SerialNumber
        self.hash_rates = hash_rates
        self.mac = mac
        self.ActiveWorker = ActiveWorker
        self.temps = temps
        self.hash_rates = hash_rates
        self.serial_number = ""
        self.active_worker = ""

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            indent=2
        )