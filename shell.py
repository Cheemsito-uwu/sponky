from data.pyinclude import colors
from data.pyinclude import temp
import basic

def interpreter():
	while True:
		text = input(colors.color_text('[[blue]]sponky > '))
		if text.strip() == "": continue
		print(colors.color_text("[[blue]]"))
		result, error = basic.run('<stdin>', text)
	
		if error:
			if str(text) == "exit":
				break
				return
			print(colors.color_text("[[red]]ERROR"))
			print(error.as_string())
		elif result:
			if len(result.elements) == 1:
				temp.delete()
				print(colors.color_text("[[green]]---------------------------"))
				print(colors.color_text("[[green]] Code ended with value: "+repr(result.elements[0])))
				print(colors.color_text("[[green]]---------------------------"))
			else:
				print(colors.color_text("[[white]]") + repr(result))

if __name__ == "__main__":
	interpreter()
