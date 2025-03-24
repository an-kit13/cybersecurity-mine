import socket
import threading
from queue import Queue
import time

class PortScanner:
    def __init__(self, target, start_port, end_port, threads=100):
        self.target = target
        self.start_port = start_port
        self.end_port = end_port
        self.threads = threads
        self.queue = Queue()
        self.results = []
        
    def port_scan(self, port):
        try:
            sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            sock.settimeout(1)
            result = sock.connect_ex((self.target, port))
            if result == 0:
                service = "unknown"
                try:
                    service = socket.getservbyport(port)
                except:
                    pass
                self.results.append((port, service))
            sock.close()
        except:
            pass
            
    def worker(self):
        while True:
            port = self.queue.get()
            if port is None:
                break
            self.port_scan(port)
            self.queue.task_done()
            
    def run(self):
        thread_list = []
        
        # Fill the queue with ports
        for port in range(self.start_port, self.end_port + 1):
            self.queue.put(port)
            
        # Start threads
        for _ in range(self.threads):
            thread = threading.Thread(target=self.worker)
            thread_list.append(thread)
            thread.start()
            
        # Wait for all ports to be scanned
        self.queue.join()
        
        # Stop threads
        for _ in range(self.threads):
            self.queue.put(None)
        for thread in thread_list:
            thread.join()
            
        return sorted(self.results)

def main():
    print("=== Simple Port Scanner ===")
    print("\nEnter 'quit' to exit the program")
    
    while True:
        target = input("\nEnter target IP address or hostname: ")
        if target.lower() == 'quit':
            break
            
        try:
            start_port = int(input("Enter start port (1-65535): "))
            end_port = int(input("Enter end port (1-65535): "))
            
            if not (1 <= start_port <= 65535 and 1 <= end_port <= 65535):
                print("Invalid port range! Ports must be between 1 and 65535.")
                continue
                
            print(f"\nScanning {target} from port {start_port} to {end_port}")
            print("This may take a while...\n")
            
            start_time = time.time()
            scanner = PortScanner(target, start_port, end_port)
            open_ports = scanner.run()
            
            if open_ports:
                print("\nOpen ports found:")
                print("PORT\tSERVICE")
                print("-" * 30)
                for port, service in open_ports:
                    print(f"{port}\t{service}")
            else:
                print("\nNo open ports found in the specified range.")
                
            print(f"\nScan completed in {time.time() - start_time:.2f} seconds")
            
        except ValueError:
            print("Please enter valid port numbers!")
        except socket.gaierror:
            print("Hostname could not be resolved!")
        except KeyboardInterrupt:
            print("\nScan interrupted by user.")
        except Exception as e:
            print(f"An error occurred: {str(e)}")
            
        print("\n" + "="*50)

main()