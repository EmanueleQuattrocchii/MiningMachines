class MiningMachine:
    hostname: str
    ip_address: str
    SerialNumber: str
    hash_rates: list
    mac: str
    ActiveWorker: str
    temps: list
    
    def __init__(self, hostname: str,
    ip_address: str,
    SerialNumber: str,
    hash_rates: list,
    mac: str,
    ActiveWorker: str,
    temps: list) -> None:
        self.hostname = hostname
        self.ip_address = ip_address
        self.SerialNumber = SerialNumber
        self.hash_rates = hash_rates
        self.mac = mac
        self.ActiveWorker = ActiveWorker
        self.temps = temps
