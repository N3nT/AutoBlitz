import wmi
import subprocess

f = wmi.WMI()

def check_if_lol_is_running():
	for process in f.Win32_Process():
		if "LeagueClient.exe" == process.Name:
			global flag
			flag = 1
			break


def check_if_blitz_running():
	for process in f.Win32_Process():
		if "Blitz.exe" == process.Name:
			global blitz
			blitz = 1
			break

def main():
	check_if_lol_is_running()
	check_if_blitz_running()
	if(flag == 0):
		print("Nie ma lola")
		if blitz == 1:
			subprocess.call("TASKKILL /F /IM Blitz.exe", shell=True)
			print("Nie ma blitza")
	else:
		print("Jest lol")
		if blitz == 0:
			subprocess.Popen(["C:/Users/bar55/AppData/Local/Programs/Blitz/Blitz.exe"])
			print('Jest blitz')


while True:
	blitz = 0
	flag = 0
	main()
