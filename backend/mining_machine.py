class MiningMachine:
    ip_address: str
    hostname: str
    mac: str
    temps: list
    hash_rates: list

    def __init__(self, ip_address: str, hostname: str, mac: str, temps: list, hash_rates: list) -> None:
        self.ip_address = ip_address
        self.hostname = hostname
        self.mac = mac
        self.temps = temps
        self.hash_rates = hash_rates
