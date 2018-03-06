import json
import psutil
import time


class Monitor:
    """docstring for Monitor."""
    mbites = float(1 << 20)
    snapCount = 1  # SNAPSHOT counter
    json_key = {}  # Output dict

    def __init__(self, output, interval=5):
        self.interval = interval  # Interval of snapshots
        self.output = output  # Type of file to output

    def CPULoad(self):
        Monitor.json_key["CPU_Usage"] = str(psutil.cpu_percent(interval=1))

    def TotalMemory(self):
        Monitor.json_key["Total_Memory"] = str(psutil.virtual_memory().total / Monitor.mbites)

    def MemoryUsage(self):
        Monitor.json_key["Memory_Used"] = str(psutil.virtual_memory().used / Monitor.mbites)

    def DiskIO(self):
        IO_stats = psutil.disk_io_counters()
        Monitor.json_key["IO_Stats"] = {
            "Read_Stats": str(IO_stats.read_bytes / Monitor.mbites),
            "Write_Stats": str(IO_stats.write_bytes / Monitor.mbites)}

    def NetInfo(self):
        NetInfo = psutil.net_io_counters()
        Monitor.json_key["Network"] = {
            "Mbytes_Sent": str(NetInfo.bytes_sent / Monitor.mbites),
            "Mbytes_Recived": str(NetInfo.bytes_recv / Monitor.mbites)}

    def WriteFile(self, data):
        if self.output == "txt":
            f = open("log.txt", "a")
            res = json.dumps(data)
            for ch in ['{', '}', '"', ',']:
                res = res.replace(ch, "")
            f.write(res + "\n")
            f.close()
        elif self.output == "json":
            with open('log.json', 'a') as json_file:
                json.dump(data,
                          json_file,
                          sort_keys=False,
                          indent=5,
                          ensure_ascii=False)

    def start(self):
        f = open("log.txt", "w")  # Rewrite txt file if it exist or create if not
        f.close
        json_file = open('log.json', 'w')  # Rewrite json file if it exist or create if not
        json_file.close()
        while True:
            Monitor.json_key["SNAPSHOT"] = Monitor.snapCount
            Monitor.json_key["TIMESTAMP"] = time.strftime("%H:%M:%S %d-%m-%Y")
            self.CPULoad()
            self.TotalMemory()
            self.MemoryUsage()
            self.DiskIO()
            self.NetInfo()
            self.WriteFile(Monitor.json_key)
            Monitor.snapCount += 1
            time.sleep(self.interval*60)  # Multiply by 60 to get time in seconds
