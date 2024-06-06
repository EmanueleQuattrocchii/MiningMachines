import { Component, OnInit } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { machineInformationsService } from '../services/machineInformationsService';
import { machineModel } from '../models/machineModel';
import { CommonModule } from '@angular/common';
import { HttpClientModule } from '@angular/common/http';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule, HttpClientModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})

export class AppComponent implements OnInit {
  constructor(public mis: machineInformationsService) { }
  
  title: string = "frontend";
  machinesInformations: Array<machineModel> = [];
  tempsModalIsViewMode: boolean = false;
  miTemps: Array<number> = [];
  ipAddress: string = "192.168.1.1"

  ngOnInit(): void {
    console.log(this.machinesInformations);
    this.getMachineInformations(this.ipAddress);
  }

  toggleTempsModalIsViewMode() {
    this.tempsModalIsViewMode = !this.tempsModalIsViewMode
  }
  
  showTemps(mi: machineModel) {
    this.miTemps = mi.temps;
  }

  getMachineInformations(ipAddress: string) {
    this.mis.getMachineInformations(ipAddress).subscribe({
      next: (result) => {
        console.log(result)
        console.log(result.get("machines"))
        console.log(typeof result)
        result.forEach((m) => this.machinesInformations.push(machineModel.mapper(m)));
        console.log(this.machinesInformations);
      },
      error: (error) => {
        console.error(error);
      }
    });
  }
}


