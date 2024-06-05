from fastapi.middleware.cors import CORSMiddleware
from fastapi import FastAPI
from fastapi.responses import JSONResponse
from ip_scanner import get_data_from_network

app = FastAPI()
app.title = "Mining dashboard"
app.version = "0.1"
app.add_middleware(
    CORSMiddleware,
    allow_origins = ["*"],
    allow_credentials = True,
    allow_methods = ["*"],
)

@app.get("/", tags=["Get"])
def get_data():
    machines = get_data_from_network(ip_address="192.168.1.0", debugging=True)
    print(machines)
    machines_to_json = []
    for machine in machines:
        machines_to_json.append(machine.to_dict())

    return JSONResponse(content={"machines" : machines_to_json}, status_code=201)

