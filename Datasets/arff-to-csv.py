import pandas as pd
from scipy.io import arff

def arff_to_csv(input_file, output_file):
    # Leer el archivo .arff
    data, meta = arff.loadarff(input_file)
    
    # Convertir a un DataFrame de pandas
    df = pd.DataFrame(data)
    
    # Guardar el DataFrame como un archivo .csv
    df.to_csv(output_file, index=False)
    
    print(f"Archivo convertido y guardado en {output_file}")

# Ejemplo de uso
input_file = '/home/diego/VSProjects/Pruebas/Airlines/Airplanes2000.arff'
output_file = '/home/diego/VSProjects/Pruebas/Airlines/Airplanes2000.csv'
arff_to_csv(input_file, output_file)
