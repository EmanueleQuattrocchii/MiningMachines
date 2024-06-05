import json
import ping3
import subprocess
from flask import Flask, render_template
import ping3

from getmac import get_mac_address
from mining_machine import MiningMachine

def get_data_from_network(ip_address: str, debugging: bool | None) -> list:
    machines = [MiningMachine(ip_address="ip_to_try", hostname="hostname", mac="mac", temps=["a"], hash_rates=["s"])]

    if(debugging):
        return machines

    if "." not in ip_address:
        print("Wrong IP -> You didn't set any dot.")
        return
    elif len(ip_address.split(".")) != 4:
        print("Wrong IP -> The IP must have 4 numbers separated by dots.")
        return
    
    network = ip_address.split(".")[:3]

    for num in network:
        try:
            if (int(num) < 0 or int(num) > 255):
                print("Wrong IP -> The IP cannot have numbers < 0 or > 255")
                return 
        except ValueError:
             print("Wrong IP -> The IP must have 4 numbers separated by dots.")
             return

    network_to_str = ".".join(network)

    for i in range(1, 20):
        ip_to_try = f"{network_to_str}.{i}"
        response = ping3.ping(dest_addr=ip_to_try, timeout=1, unit="s")

        if response == None or response == False:
            message = f"Don't getting any response from '{ip_to_try}'"
            print(message)
            continue
        
        message = f"Took {response:.2f} ms to get a response from '{ip_to_try}'"
        mac = get_mac_address(ip=ip_to_try)
        
        # Getting hostname
        command = " ".join(["""echo '{"id":"info"}'""", "|", f"ncat.exe {ip_to_try} 4111"])
        result = subprocess.run(["powershell.exe", command], capture_output=True, text=True)
        if result.returncode != 0:
            continue
        hostname = json.loads(result.stdout)["ret"]["softver1"]

        # Getting temperatures & hash rates
        command_2 = " ".join(["""echo '{"id":"board"}'""", "|", f"ncat.exe {ip_to_try} 4111"])
        result_2 = subprocess.run(["powershell.exe", command_2], capture_output=True, text=True)
        if result_2.returncode != 0:
            continue

        result_2_dict =  json.loads(result_2.stdout)
        boards = result_2_dict["ret"]["boards"]
        temps = []
        hash_rates = []

        for board in boards:
            temps.append(board["intmp"])
            hash_rates.append(board["rtpow"])

        machines.append(MiningMachine(ip_address=ip_to_try, hostname=hostname, mac=mac, temps=temps, hash_rates=hash_rates))
        print(message)
    
    return machines

