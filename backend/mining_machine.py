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

    def to_dict(self) -> dict:
        return {
            "ip_address": self.ip_address,
            "hostname": self.hostname,
            "mac": self.mac,
            "temps": self.temps,
            "hash_rates": self.hash_rates,
            "serial_number": self.serial_number,
            "active_worker": self.active_worker,
        }