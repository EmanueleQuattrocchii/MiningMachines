import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { machineInformationsService } from '../services/machineInformationsService';
import { machineModel } from '../models/machineModel';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  constructor(public mis: machineInformationsService){}

  machinesInformations: Array<machineModel> = [];

  ngOnInit(): void {
    this.getMachineInformations();
  }

  getMachineInformations(){
    this.mis.getMachineInformations().subscribe({
      next: (result) => {
         this.machinesInformations = result;
      },
      error: (error) =>{
        null;
      }
    })
  }
}
