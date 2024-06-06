import json

class MiningMachine:
    hostname: str
    ip_address: str
    hash_rates: list
    mac: str
    in_temps: list
    out_temps: list
    temps: list
    serial_number: str | None
    active_worker: str | None

    def __init__(self, ip_address: str, hostname: str, mac: str, in_temps: list, out_temps: list, temps: list, hash_rates: list) -> None:
        self.hostname = hostname
        self.ip_address = ip_address
        self.serial_number = ""
        self.hash_rates = hash_rates
        self.mac = mac
        self.in_temps = in_temps
        self.out_temps = out_temps
        self.temps = temps
        self.active_worker = ""

    def to_dict(self) -> dict:
        return {
            "ip_address": self.ip_address,
            "hostname": self.hostname,
            "mac": self.mac,
            "in_temps": self.in_temps,
            "out_temps": self.out_temps,
            "temps": self.temps,
            "hash_rates": self.hash_rates,
            "serial_number": self.serial_number,
            "active_worker": self.active_worker,
        }