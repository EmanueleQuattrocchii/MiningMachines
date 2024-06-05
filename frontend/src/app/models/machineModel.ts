export interface machineModel{
    Name: string;
    IPAddress: string;
    SerialNumber: string;
    HashRate: Array<string>;
    MACAddress: string;
    ActiveWorker: string;
    Temps: Array<number>;
}