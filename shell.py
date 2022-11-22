from data.pyinclude import colors
from data.pyinclude import temp
from data import config

import colorama
from colorama import Fore, Style
import basic
import os

def interpreter():
	while True:
		colorama.init(autoreset=True)

		text = input(Fore.BLUE + 'sponky > ' + Fore.CYAN)
		if text.strip() == "": continue
		print(Fore.WHITE)
		result, error = basic.run('<stdin>', text)
	
		if error:
			match str(text):
				case "config":
					config.opn()
					continue

				case "exit" | "quit":
					break
				
				case _:
					if os.path.exists(str(text)):
						basic.run_program(str(text))
						continue


			print(Fore.RED + error.as_string())
		elif result:
			if len(result.elements) == 1:
				temp.delete()
				print(Fore.GREEN + "---------------------------")
				print(Fore.GREEN + " Code ended with value: "+repr(result.elements[0]))
				print(Fore.GREEN + "---------------------------")
			else:
				print(Fore.GREEN + repr(result))

if __name__ == "__main__":
	interpreter()