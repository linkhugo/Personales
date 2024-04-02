from dns import resolver

def dns_query(domain, record_type, server):
    try:
        resolver_obj = resolver.Resolver()
        resolver_obj.nameservers = [server]
        answer = resolver_obj.resolve(domain, record_type)
        return [str(r) for r in answer]
    except resolver.NXDOMAIN:
        return "Error: El dominio no existe."
    except Exception as e:
        return f"Error: {e}"

def main():
    file_path = input("Por favor, introduce la ruta del archivo que contiene los dominios: ")
    record_type = input("Por favor, introduce el tipo de registro a consultar (A, MX, CNAME, etc.): ")
    server = input("Por favor, introduce el servidor DNS a consultar: ")

    with open(file_path, 'r') as file:
        domains = file.readlines()

    for domain in domains:
        domain = domain.strip()
        result = dns_query(domain, record_type, server)
        print(f"Resultados de la consulta para {domain}: {result}")

if __name__ == "__main__":
    main()