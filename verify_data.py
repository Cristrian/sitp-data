# The present script is to verify that all the csv files in the csv_data folder are valid

# We are going to use the polars module
import polars as pl

from pathlib import Path


# The columns should be:
expected_columns = [
    'Dispositivo',
    'Emisor',
    'Estacion_Parada',
    'Fase',
    'Fecha_Clearing',
    'Fecha_Transaccion',
    'Hora_Pico_SN',
    'ID_Vehiculo',
    'Linea',
    'Nombre_Perfil',
    'Numero_Tarjeta',
    'Operador',
    'Ruta',
    'Saldo_Despues_Transaccion',
    'Saldo_Previo_a_Transaccion',
    'Sistema',
    'Tipo_Tarifa',
    'Tipo_Tarjeta',
    'Tipo_Vehiculo',
    'Valor',
    'archivo'
 ]

list_of_files = [f.name for f in Path('csv_data').glob('*.csv')]

for i, file in enumerate(Path('csv_data').glob('*.csv')):
    df = pl.read_csv(file)
    print(f'Verifying {file}. This is file number {i + 1} of {len(list_of_files)}')
    assert df.schema.names() == expected_columns

# df = pl.read_csv('csv_data/20240801.csv')

print(df.describe())

# df.schema.names() para verificar que es la misma columna