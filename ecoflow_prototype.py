import time
import random

class EnergyAgent:
    def __init__(self, name, machinery_load):
        self.name = name
        self.load = machinery_load # kW
        self.status = "OFF"

    def decide(self, energy_price, limit):
        if energy_price < limit:
            self.status = "ON"
            return self.load
        else:
            self.status = "OFF"
            return 0

def simulate_optimization():
    agents = [
        EnergyAgent("Prensa_Hidraulica_1", 150),
        EnergyAgent("Horno_Induccion_A", 400),
        EnergyAgent("Robot_Soldadura_B2", 50),
        EnergyAgent("Sistema_Climatizacion", 80)
    ]

    print("--- Simulación EcoFlow AI Optimizer ---")
    print("Objetivo: Minimizar costes encendiendo cargas pesadas en horas valle.\n")

    for hour in range(8, 20): # Horario laboral
        price = random.uniform(0.1, 0.5) # €/kWh
        threshold = 0.3 # Límite de precio para activar agentes pesados
        
        total_consumption = 0
        active_list = []
        
        for agent in agents:
            consumption = agent.decide(price, threshold)
            total_consumption += consumption
            if agent.status == "ON":
                active_list.append(agent.name)

        print(f"[Hora {hour:02d}:00] Precio Luz: {price:.2f} €/kWh | Consumo Activo: {total_consumption} kW")
        print(f"Agentes en Marcha: {active_list if active_list else 'NINGUNO (Ahorro Energético)'}")
        print("-" * 50)
        time.sleep(0.5)

if __name__ == "__main__":
    simulate_optimization()
