from module import get_rssi

if __name__ == '__main__':
    while True:
        rssi = get_rssi()
        print(rssi)