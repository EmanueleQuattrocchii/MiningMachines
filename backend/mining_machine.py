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