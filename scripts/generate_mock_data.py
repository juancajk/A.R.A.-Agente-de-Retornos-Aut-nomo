import csv
import random
import os
from datetime import datetime, timedelta

def generar():
    os.makedirs('data', exist_ok=True)
    with open('data/pedidos.csv', 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['pedido_id', 'cliente_id', 'fecha_compra', 'monto', 'categoria'])
        
        
        for i in range(2, 41):
            if i == 15: 
                continue
            fecha = datetime(2025, 10, 15) - timedelta(days=random.randint(1, 20))
            writer.writerow([
                f'PED-{i:03d}', f'CLI-{random.randint(10, 99)}', 
                fecha.strftime('%Y-%m-%d'), random.randint(10000, 150000), 'electronica'
            ])
            
        # Insertar los pedidos exactos que necesitan los tests
        writer.writerow(['PED-015', 'CLI-99', '2025-01-01', 50000, 'electronica']) # Fuera de plazo
        writer.writerow(['PED-001', 'CLI-01', '2025-10-10', 80000, 'electronica']) # Válido

if __name__ == '__main__':
    generar()