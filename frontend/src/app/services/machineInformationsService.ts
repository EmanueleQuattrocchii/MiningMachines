import { HttpClient } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { machineModel } from "../models/machineModel";
import { Observable } from "rxjs";

@Injectable({
    providedIn: "root"
})

export class machineInformationsService{

    constructor(private http: HttpClient) {}

    getMachineInformations() : Observable<Array<machineModel>> {
        return this.http.get<Array<machineModel>>("http://127.0.0.1:8000/machines/get")
    }  
}
