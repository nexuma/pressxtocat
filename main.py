import requests
import re
import pyperclip
import customtkinter
import random
import threading

# State variable
active=False

# Defaults and constants
copy_interval = 300
AMOUNT = 100
 
# Facts
facts = []
 
# Filters for quality facts and safety
def has_url(text):
	return bool(re.search(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", text))

def has_script(text):
	return bool(re.search(r"<script>", text))

def has_repeat_caracter(text):
	return bool(re.search(r"(.)\1{4,}", text))

def too_short(text):
	return len(text) < 7

# Animal filters, more to come
def has_cat(text):
	return bool(re.search(r"cat|kitten|meow|feline", text, re.I))
	
def has_dog():
	pass
	
def has_horse():
	pass

def filter_fact(fact):
	"""Filter logic, returns true if fact is acceptable"""
	if has_url(fact) or has_script(fact) or has_repeat_caracter(fact) or too_short(fact) or has_repeat_caracter(fact):
		return False
	if has_cat(fact):
		return True
	return False

def copy_to_clipboard():
	"""Copy a random fact to clipboard, by default the function repeats itself each copy_interval variable amount in ms"""
	if active:
		pyperclip.copy(random.choice(facts))
		root.after(int(slider.get()), copy_to_clipboard)
		
def slider_event(value):
	"""Slider function for modifying actual copy interval"""
	global copy_interval
	copy_interval = value
	if slider.get() < 1000:
		slider.configure(from_=100, to=10000, number_of_steps=1000)
		slider_label.configure(text=f"Copy interval: {round(slider.get())} ms")
	else:
		slider_label.configure(text=f"Copy interval: {round(slider.get()/1000, 1)} s")
	
def activate():
	"""Switch state function, also sets color of button depending on state"""
	global active
	active = False if active else True
	if active:
		activate_button.configure(text="Deactivate", fg_color=("#AE0006","#B80006"), hover_color="#4E0003")
		copy_to_clipboard()
	else:
		activate_button.configure(text="Activate", fg_color=("#16A500","#14A007"), hover_color="#043100")
	
def change_appearance_mode_event(new_appearance_mode: str):
	"""Theme changer"""
	customtkinter.set_appearance_mode(new_appearance_mode)
	
def generate_facts_list():
	global facts
	"""Gets facts from API and generates list"""
	facts=[]
	progressbar.configure(mode="indeterminate")
	progressbar.start()
	try:
	
		response = requests.get(f"https://cat-fact.herokuapp.com/facts/random?animal_type=cat&amount={AMOUNT}")
		data = response.json()
		progressbar.stop()
		progressbar.configure(mode = "determinate")
		for i, el in enumerate(data):
			fact = data[i]["text"]
			progressbar.step()
			if filter_fact(fact):
				facts.append(fact)
				
	except Exception as e: #Creates error alert window
		window = customtkinter.CTkToplevel()
		window.geometry("400x200")
		window.title("Error")
		label = customtkinter.CTkLabel(window, text=f"An error has occured while fetching the facts from the api. Error message: {e}", wraplength=300)
		label.pack(side="top", fill="both", expand=True)
		facts.append("My cat fact machine is broken")
		
	refresh_button.configure(state="normal")
	activate_button.configure(state="normal")
	progressbar.set(1)
	
	

def refresh_facts():
	activate_button.configure(state="disabled")
	refresh_button.configure(state="disabled")
	threading.Thread(target=generate_facts_list).start()
	

"""
def resource_path(relative_path):
	\""" Get absolute path to resource, works for dev and for PyInstaller \"""
	try:
		# PyInstaller creates a temp folder and stores path in _MEIPASS
		base_path = sys._MEIPASS
	except Exception:
		base_path = os.path.abspath(".")

	return os.path.join(base_path, relative_path)
"""

###Start of customtkinter layout	
if __name__ == '__main__':
	root = customtkinter.CTk()

	customtkinter.set_appearance_mode("system")
	customtkinter.set_default_color_theme("blue")

	root.minsize(170, 430)

	root.title("")
	root.iconbitmap("logo.ico") #resource_path("logo.ico")

	frame = customtkinter.CTkFrame(master=root)
	frame.pack(pady=0, padx=0, fill="both", expand=True)
	

	
	title_label = customtkinter.CTkLabel(master=frame, text="Press x to Cat", font=("Roboto", 24))
	title_label.pack(pady=12, padx=10)

	animal_label = customtkinter.CTkLabel(frame, text="Animal", font=("Roboto", 14))
	animal_label.pack(padx=20, pady=(0, 0),)

	animal_optionemenu = customtkinter.CTkOptionMenu(frame, values=["Cat", "more incoming"], state="disabled")
	animal_optionemenu.pack(padx=20, pady=(0, 30))

	slider_label = customtkinter.CTkLabel(frame, text=f"Copy interval: {copy_interval} ms", font=("Roboto", 14))
	slider_label.pack()

	slider = customtkinter.CTkSlider(master=frame, from_=0, to=10000, command=slider_event, number_of_steps=10000)
	slider.set(300)
	slider.pack(padx=20, pady=(0, 0))

	activate_button = customtkinter.CTkButton(master=frame, text="Activate", command=activate, fg_color=("#16A500","#14A007"), hover_color="#043100", font=("Roboto", 14))
	activate_button.pack(pady=(5,25), padx=10)

	refresh_label = customtkinter.CTkLabel(frame, text="Get new facts", font=("Roboto", 14))
	refresh_label.pack(pady=(20,0), padx=10)
	refresh_button = customtkinter.CTkButton(master=frame, text="Refresh", command=refresh_facts,  font=("Roboto", 14))
	refresh_button.pack(pady=(0,10), padx=10)
	
	progressbar = customtkinter.CTkProgressBar(master=frame, mode="indeterminate", determinate_speed=(50/(AMOUNT)), indeterminate_speed=2)
	progressbar.pack(padx=10, pady=(0, 0))
	progressbar.set(0)

	appearance_mode_label = customtkinter.CTkLabel(frame, text="Appearance", font=("Roboto", 14))
	appearance_mode_optionemenu = customtkinter.CTkOptionMenu(frame, values=["System","Dark","Light"], command=change_appearance_mode_event)
	appearance_mode_optionemenu.pack(padx=20, pady=(10, 10), side="bottom")
	appearance_mode_label.pack(padx=20, pady=(10, 0), side="bottom")
	
	
	
	#generate initial list
	refresh_facts()
	root.mainloop()

	


	
	
	










