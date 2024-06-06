import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { machineModel } from "../models/machineModel";
import { Observable, map } from "rxjs";

@Injectable({
    providedIn: "root"
})

export class machineInformationsService{

    constructor(private http: HttpClient) {}

    getMachineInformations(ipAddress: string) : Observable<Map<String, Map<string, Object | number[] | string[]>>> {
        return this.http.get<Map<String, Map<string, Object | number[] | string[]>>>(`http://127.0.0.1:8000/machines/get?ip_address=${ipAddress}`);
    }  
}
