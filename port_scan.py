import sys, socket

def port_scanner(ip, porta=None):
    try:
        scan = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        if porta:
            print(f"{ip} => {socket.gethostbyname(ip)}:{porta}")
            if scan.connect_ex((ip, porta)) == 0:
                print(f"[+] Porta: {porta} => [ABERTA]")
                scan.close()
            else:
                print(f"Porta {porta} Fechada")
        else:
            print(f"{ip} => {socket.gethostbyname(ip)}")
            for i in range(1, 65535):
                if scan.connect_ex((ip, i)) == 0:
                    print(f"[+] Porta: {i} => [ABERTA]")
                    scan.close()
    except Exception as e:
        print(e)
        print("Ocorreu um erro durante a execução do programa.")


if __name__ == '__main__':
    if len(sys.argv) == 3:
        port_scanner(sys.argv[1], int(sys.argv[2]))
    else:
        port_scanner(sys.argv[1])

