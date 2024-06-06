export class machineModel{
    hostname: string;
    ip_address: string;
    serial_number: string;
    hash_rates: Array<string>;
    mac: string;
    active_worker: string;
    temps: Array<number>;
    in_temps: Array<number>;
    out_temps: Array<number>;

    constructor(hostname: string,
        ip_address: string,
        serial_number: string,
        hash_rates: Array<string>,
        mac: string,
        active_worker: string,
        temps: Array<number>,
        in_temps: Array<number>,
        out_temps: Array<number>)
        {
            this.ip_address = ip_address,
            this.hostname = hostname,
            this.serial_number = serial_number,
            this.hash_rates = hash_rates,
            this.mac = mac,
            this.active_worker = active_worker,
            this.temps = temps,
            this.in_temps = in_temps,
            this.out_temps = out_temps
    }
    static mapper(dict: Map<string,Object | string[] | number[]>){
        return new machineModel(
            `${dict.get("hostname")}`,
            `${dict.get("ip_address")}`,
            `${dict.get("serial_number")}`,
            dict.get("hash_rates")! as string[],
            `${dict.get("mac")}`,
            `${dict.get("active_woker")}`,
            dict.get("temps") as number[],
            dict.get("in_temps") as number[],
            dict.get("out_temps") as number[],

        );
    }
}

