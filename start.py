import configparser as conf
import Monitor as M

config = conf.ConfigParser()
config.read("settings.ini")
common = config['common']
output = common['output']
interval = int(common['interval'])

mon = M.Monitor(output,interval)
mon.start()
