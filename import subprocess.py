import subprocess

def dig_short(domain, record_type, server):
    try:
        result = subprocess.run(['dig', '+short', '@'+server, domain, record_type], capture_output=True, text=True, check=True)
        return result.stdout.strip()
    except subprocess.CalledProcessError as e:
        return f"Error: {e}"

def main():
    file_path = input("Por favor, introduce la ruta del archivo que contiene los dominios: ")

    with open(file_path, 'r') as file:
        domains = file.readlines()

    record_type = input("Por favor, introduce el tipo de registro a consultar (A, MX, CNAME, etc.): ")
    server = input("Por favor, introduce el servidor DNS a consultar: ")

    for domain in domains:
        domain = domain.strip()
        print(f"Consultando registros {record_type} para {domain}: ", end='')
        print(dig_short(domain, record_type, server))

if __name__ == "__main__":
    main()