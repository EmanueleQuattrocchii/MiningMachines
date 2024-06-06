import json
import ping3
import subprocess
from flask import Flask, render_template
import ping3

from getmac import get_mac_address
from mining_machine import MiningMachine

def is_ip_correct(ip_address: str) -> bool:
    if "." not in ip_address:
        return False
    elif len(ip_address.split(".")) != 4:
        return False
    
    network = ip_address.split(".")[:3]

    for num in network:
        try:
            if (int(num) < 0 or int(num) > 255):
                return False
        except ValueError:
             return False
    return True

def get_data_from_network(ip_address: str, debugging: bool) -> list[MiningMachine] | list[str]:
    machines = []

    if debugging:
        machines.append(
            MiningMachine(
                ip_address="ip",
                hostname="hostname", 
                mac="mac", 
                temps=["temp1", 
                       "temp2", 
                       "temp3"],
                hash_rates=[
                    "hash_rate1",
                    "hash_rate2"],
                out_temps=["61", "36"],
                in_temps=["611", "3643"],
                    )
                )
        return machines
    
    if not is_ip_correct(ip_address=ip_address):
        return [f"{ip_address} is an invalid IP"]

    network: list[str] = ip_address.split(".")
    network.pop()
    network_to_str = ".".join(network)

    for i in range(1, 11):
        in_temps = []
        out_temps = []
        hash_rates = []
        temps = []

        ip_to_try = f"{network_to_str}.{i}"
        ping_response = ping3.ping(dest_addr=ip_to_try, timeout=0.5, unit="s")
        mac = get_mac_address(ip=ip_to_try)

        print(f"Trying with {ip_to_try}")

        if(type(ping_response) == float):
            message = f"Took {ping_response:.2f} ms to get a response from '{ip_to_try}'"
        
        # Getting hostname
        command = " ".join(["""echo '{"id":"info"}'""", "|", f"ncat {ip_to_try} 4111"])
        result = subprocess.run(["powershell.exe", command], capture_output=True, text=True)
        if result.returncode != 0:
            print("Continued 1")
            continue

        hostname = json.loads(result.stdout)["ret"]["softver1"]

        # Getting in/out temperatures & hash rates
        command_2 = " ".join(["""echo '{"id":"board"}'""", "|", f"ncat {ip_to_try} 4111"])
        result_2 = subprocess.run(["powershell.exe", command_2], capture_output=True, text=True)
        if result_2.returncode != 0:
            print("Continued 2")
            continue

        result_2_dict =  json.loads(result_2.stdout)
        boards = result_2_dict["ret"]["boards"]
        
        for board in boards:
            in_temps.append(board["intmp"])
            out_temps.append(board["outtmp"])
            hash_rates.append(board["rtpow"])

        # Getting temperatures 
        command_3 = " ".join(["""echo '{"id":"getchipinfo"}'""", "|", f"ncat {ip_to_try} 4111"])
        result_3 = subprocess.run(["powershell.exe", command_3], capture_output=True, text=True)
        if result_3.returncode != 0:
            print("Continued 3")
            continue
        
        chips = json.loads(result_3.stdout)["ret"]["chips"]

        for chip in chips:
            temps.append(chip["temp"])
        
        machines.append(MiningMachine(ip_address=ip_to_try, hostname=hostname, mac=mac, in_temps=in_temps, out_temps=out_temps, temps=temps, hash_rates=hash_rates))
        print(message)
    
    return machines

