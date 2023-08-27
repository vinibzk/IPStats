import subprocess
import os
from socket import socket, AF_INET, SOCK_DGRAM
from tabulate import tabulate

class Colors:
    GREEN = '\033[92m'
    RED = '\033[91m'
    YELLOW = '\033[93m'
    BLUE = '\033[94m'
    CYAN = '\033[96m'
    PINK = '\033[95m'
    BOLD = '\033[1m'
    ENDC = '\033[0m'

class DeviceChecker:
    def __init__(self):
        self.history = []

    def clear_screen(self):
        os.system('cls' if os.name == 'nt' else 'clear')

    def display_menu(self):
        self.clear_screen()
        print(f"{Colors.BOLD}{Colors.CYAN}=== Verificador de Dispositivo Online ==={Colors.ENDC}\n")
        print(f"{Colors.GREEN}[1] Verificar Dispositivo Online")
        print(f"{Colors.BLUE}[2] Verificar Múltiplos Dispositivos")
        print(f"{Colors.CYAN}[3] Histórico de Verificações")
        print(f"{Colors.YELLOW}[4] Limpar Histórico")
        print(f"{Colors.PINK}[5] Verificar Portas Abertas")
        print(f"{Colors.YELLOW}[6] Sair{Colors.ENDC}\n")

    def is_device_online(self, ip_address):
        try:
            subprocess.run(['ping', '-c', '1', ip_address], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True)
            return True
        except subprocess.CalledProcessError:
            return False

    def check_multiple_devices(self, ip_list):
        self.clear_screen()
        online_devices = []
        offline_devices = []
        for ip in ip_list:
            if self.is_device_online(ip):
                online_devices.append(ip)
            else:
                offline_devices.append(ip)
        self.clear_screen()
        print(f"{Colors.CYAN}Resultados da Verificação de Múltiplos Dispositivos{Colors.ENDC}\n")
        print(f"{Colors.GREEN}{Colors.BOLD}Dispositivos Online:{Colors.ENDC}")
        for device in online_devices:
            print(f"{Colors.GREEN}{device}{Colors.ENDC}")
        print(f"\n{Colors.RED}{Colors.BOLD}Dispositivos Offline:{Colors.ENDC}")
        for device in offline_devices:
            print(f"{Colors.RED}{device}{Colors.ENDC}")
        self.history.append(f"Verificação de Múltiplos Dispositivos - Online: {online_devices} | Offline: {offline_devices}")

    def display_history(self):
        self.clear_screen()
        if self.history:
            print(f"{Colors.CYAN}Histórico de Verificações{Colors.ENDC}\n")
            for entry in self.history:
                print(entry)
        else:
            print(f"{Colors.YELLOW}Nenhum histórico disponível.{Colors.ENDC}")
        input(f"\n{Colors.BOLD}Pressione Enter para voltar ao menu principal...{Colors.ENDC}")

    def run(self):
        while True:
            self.display_menu()
            choice = input(f"{Colors.BOLD}Escolha uma opção: {Colors.ENDC}")

            if choice == "1":
                self.clear_screen()
                ip_address = input(f"{Colors.GREEN}Digite o endereço IP para verificar: {Colors.ENDC}")
                self.clear_screen()
                if self.is_device_online(ip_address):
                    print(f"{Colors.GREEN}{Colors.BOLD}O dispositivo com o IP {ip_address} está online.{Colors.ENDC}")
                else:
                    print(f"{Colors.RED}{Colors.BOLD}O dispositivo com o IP {ip_address} não está online.{Colors.ENDC}")
                input(f"\n{Colors.BOLD}Pressione Enter para voltar ao menu principal...{Colors.ENDC}")

            elif choice == "2":
                self.clear_screen()
                ip_list = input(f"{Colors.BLUE}Digite a lista de IPs separados por vírgula: {Colors.ENDC}").split(",")
                self.check_multiple_devices(ip_list)
                input(f"\n{Colors.BOLD}Pressione Enter para voltar ao menu principal...{Colors.ENDC}")

            elif choice == "3":
                self.display_history()

            elif choice == "4":
                self.clear_screen()
                self.history = []
                print(f"{Colors.YELLOW}Histórico limpo.{Colors.ENDC}")
                input(f"\n{Colors.BOLD}Pressione Enter para voltar ao menu principal...{Colors.ENDC}")

            elif choice == "5":
                self.clear_screen()
                host = input(f"{Colors.PINK}Digite o endereço IP do host para verificar as portas abertas: {Colors.ENDC}")
                self.clear_screen()
                print(f"{Colors.CYAN}Verificando Portas Abertas para o Host: {Colors.PINK}{host}{Colors.ENDC}\n")
                self.check_open_ports(host)
                input(f"\n{Colors.BOLD}Pressione Enter para voltar ao menu principal...{Colors.ENDC}")

            elif choice == "6":
                self.clear_screen()
                print(f"{Colors.BOLD}{Colors.GREEN}Encerrando o programa. Até logo!{Colors.ENDC}\n")
                break

            else:
                print(f"\n{Colors.RED}{Colors.BOLD}Escolha inválida. Por favor, escolha uma opção válida.{Colors.ENDC}\n")
                input(f"{Colors.BOLD}Pressione Enter para continuar...{Colors.ENDC}")

    def check_open_ports(self, host):
        try:
            result = subprocess.run(['nmap', '-p-', host], stdout=subprocess.PIPE, stderr=subprocess.PIPE, check=True, text=True)
            output = result.stdout
            ports_info = self.parse_ports_info(output)
            if ports_info:
                print(tabulate(ports_info, headers="keys", tablefmt="grid"))
            else:
                print(f"{Colors.YELLOW}Nenhuma porta aberta encontrada para o Host: {Colors.PINK}{host}{Colors.ENDC}")
        except subprocess.CalledProcessError:
            print(f"{Colors.RED}Erro ao verificar portas abertas.{Colors.ENDC}")

    def parse_ports_info(self, output):
        lines = output.splitlines()
        ports_info = []
        for line in lines:
            if "/" in line:
                port_info = line.split()
                if len(port_info) >= 3:
                    port = port_info[0].split("/")[0]
                    protocol = port_info[0].split("/")[1] if len(port_info[0].split("/")) > 1 else ""
                    status = port_info[1]
                    service = port_info[2] if len(port_info) > 2 else ""
                    ports_info.append({"Porta": port, "Protocolo": protocol, "Status": status, "Serviço": service})
        return ports_info

if __name__ == "__main__":
    checker = DeviceChecker()
    checker.run()