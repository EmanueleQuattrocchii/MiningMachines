import json

class MiningMachine:
    hostname: str
    ip_address: str
    SerialNumber: str
    hash_rates: list
    mac: str
    ActiveWorker: str
    temps: list

    def __init__(self,hostname: str,
    ip_address: str,
    SerialNumber: str,
    hash_rates: list,
    mac: str,
    ActiveWorker: str,
    temps: list,) -> None:
        self.ip_address = ip_address
        self.SerialNumber = ""
        self.hash_rates = hash_rates
        self.mac = mac
        self.ActiveWorker = ""
        self.temps = temps

    def toJSON(self):
        return json.dumps(
            self,
            default=lambda o: o.__dict__,
            indent=2
        )