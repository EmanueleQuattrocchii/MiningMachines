import { HttpClient, HttpHeaders } from "@angular/common/http";
import { Injectable } from "@angular/core";
import { machineModel } from "../models/machineModel";
import { Observable } from "rxjs";

@Injectable({
    providedIn: "root"
})

export class machineInformationsService{

    constructor(private http: HttpClient, private as: machineInformationsService) {}

    getMachineInformations() : Observable<Array<machineModel>> {
        return this.http.get<Array<machineModel>>("http://localhost:5000/")
    }  
}