import json

class MiningMachine:
    ip_address: str
    hostname: str
    mac: str
    temps: list
    hash_rates: list
    serial_number: str | None
    active_worker: str | None

    def __init__(self, ip_address: str, hostname: str, mac: str, temps: list, hash_rates: list) -> None:
        self.ip_address = ip_address
        self.hostname = hostname
        self.mac = mac
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