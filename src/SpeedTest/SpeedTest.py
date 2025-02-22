import speedtest as st

def SpeedTest():
    test = st.Speedtest()

    down_speed = test.download()
    down_speed = round(down_speed / 10**6, 2)
    print(f'Velocidade de Download: {down_speed} Mbps')

    up_speed = test.upload()
    up_speed = round(up_speed / 10**6, 2)
    print(f'Velocidade de Upload: {up_speed} Mbps')

    ping = test.results.ping
    print(f'Ping: {ping} ms')   
SpeedTest()