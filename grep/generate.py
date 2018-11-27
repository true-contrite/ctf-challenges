import base64
import random


with open("grep_chal.txt", "w+") as outfile:

	lines = []

	for i in range(0, 20000):
		string = str(base64.b64encode(bytes(str(random.randint(1,101)) + 'CTF{'+ str(i/3.33) + '__7h15_15_N07_7H3_flA9_'+ str(i+42) +'y0u_Ar3_l00k1n9_F0r_' + str(i**2/3) +'}', 'utf-8')))
		lines.append(string[2:-1] + "\n")

	flag = str(base64.b64encode(bytes('CTF{7hi5_I5_7H3_fl4G_my_N4M3_J3ff_Ch3f}', 'utf-8')))
	flag = flag[2:-1] + "\n"

	#flag appears 4 times

	lines.insert(2500, flag)
	lines.insert(798, flag)
	lines.insert(4675, flag)
	lines.insert(1234, flag)
	
	outfile.writelines(lines)
		
		