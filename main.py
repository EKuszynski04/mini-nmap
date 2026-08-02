import socket;
from controller.controller import ScanController

def main():
    controller = ScanController()
    controller.run()

if __name__ == "__main__":
    main()
    