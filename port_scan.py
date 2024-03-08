import sys, socket

def port_scanner(ip):
    try:
        print(f"{ip} => {socket.gethostbyname(ip)}")
        for i in range(1, 65535):
            scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            if scan.connect_ex((ip, i)) == 0:
                scan.connect((ip,i))
                message = scan.recv(1024)
                print(f"[+] Porta: {i} => [ABERTA] -- {message}")
                scan.close()
    except Exception:
        print("Ocorreu um erro durante a execução do programa.")
        
        
if __name__ == '__main__':
    port_scanner(sys.argv[1])