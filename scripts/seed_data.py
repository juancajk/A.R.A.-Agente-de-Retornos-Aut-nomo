import sqlite3
import csv
import os
from config.settings import DB_PATH

def poblar():
    os.makedirs('data', exist_ok=True)
    conn = sqlite3.connect(DB_PATH)
    
    # Tabla de pedidos
    conn.execute('''CREATE TABLE IF NOT EXISTS pedidos (
                    pedido_id TEXT, cliente_id TEXT, fecha_compra TEXT, monto REAL, categoria TEXT)''')
    conn.execute('DELETE FROM pedidos') # Limpiar antes de poblar
    
    with open('data/pedidos.csv', 'r', encoding='utf-8') as f:
        reader = csv.DictReader(f)
        for row in reader:
            conn.execute('INSERT INTO pedidos VALUES (?,?,?,?,?)', 
                         (row['pedido_id'], row['cliente_id'], row['fecha_compra'], row['monto'], row['categoria']))
            
    
    conn.execute('''CREATE TABLE IF NOT EXISTS historial_cliente (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    cliente_id TEXT, pedido_id TEXT, fecha TEXT, decision TEXT, monto REAL, motivo TEXT)''')
    conn.commit()
    conn.close()
    print("Base de datos techstore.db creada y poblada con éxito.")

if __name__ == '__main__':
    poblar()