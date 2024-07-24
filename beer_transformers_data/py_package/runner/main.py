# py_package/runner/main.py

from py_package.transformation.capture import fetch_beer_data
from py_package.transformation.processing import normalize_beer_data
from py_package.transformation.output_write import export_to_csv

def main():
    # Extração dos dados
    data = fetch_beer_data()
    
    # Normalização dos dados
    normalized_data = normalize_beer_data(data)
    
    # Exportação dos dados
    output_file = export_to_csv(normalized_data)
    
    print(f"Dados exportados para {output_file}")

if __name__ == "__main__":
    main()
