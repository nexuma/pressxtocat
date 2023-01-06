import requests
import re
import pyperclip
import customtkinter
import random
import threading
from tkinter import *

# State variable
active=False

# Defaults and constants
MAX_AMOUNT = 500
copy_interval = 1000
OW_LIMIT = 200
factAmount = MAX_AMOUNT

# Facts
facts = []
facts_limited = []

# Filters for quality facts and safety
def has_url(text):
	return bool(re.search(r"(?i)\b((?:https?://|www\d{0,3}[.]|[a-z0-9.\-]+[.][a-z]{2,4}/)(?:[^\s()<>]+|\(([^\s()<>]+|(\([^\s()<>]+\)))*\))+(?:\(([^\s()<>]+|(\([^\s()<>]+\)))*\)|[^\s`!()\[\]{};:'\".,<>?«»“”‘’]))", text))

def has_script(text):
	return bool(re.search(r"<script>", text))

def filter_fact(fact):
	"""Filter logic, returns true if fact is acceptable"""
	if has_url(fact) or has_script(fact) :
		return False
	return True

def clean_fact(fact):
	"""Cleans the fact, basically adds punctuation and remove weird substrings"""
	factToClean = fact
	if not factToClean.endswith('.') and not factToClean.endswith('!'):
				factToClean += '.'
	temp = re.sub('."""',"",factToClean)
	temp = re.sub('."','"',factToClean)
	factToClean = temp
	return factToClean

def copy_to_clipboard():
	"""Copy a random fact to clipboard, by default the function repeats itself each copy_interval variable amount in ms"""
	if active:
		if check_var.get() == 1:
			pyperclip.copy(random.choice(facts_limited))
		else:
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

def len_limit_checkbox_event():
	pass

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
	global facts, factAmount
	"""Gets facts from API and generates list"""
	facts=[]
	progressbar.configure(mode="indeterminate")
	progressbar.start()
	try:
		response = requests.get(f"https://catfact.ninja/facts?limit={MAX_AMOUNT}")
		data = response.json()
		progressbar.stop()
		progressbar.configure(mode = "determinate")
		factAmount = data["total"]
		progressbar.configure(determinate_speed=50/factAmount)
		for i, el in enumerate(data["data"]):
			fact = data["data"][i]["fact"]
			progressbar.step()
			if filter_fact(fact):
				fact = clean_fact(fact)
				facts.append(fact)
				if data["data"][i]["length"] <= OW_LIMIT:
					facts_limited.append(fact)
	except Exception as e: #Creates error alert window
		window = customtkinter.CTkToplevel()
		window.geometry("400x200")
		window.title("Error")
		label = customtkinter.CTkLabel(window, text=f"An error has occured while fetching the facts from the api. Error message: {e}", wraplength=300)
		label.pack(side="top", fill="both", expand=True)
		facts.append("My cat fact machine is broken")
		
	#refresh_button.configure(state="normal")
	activate_button.configure(state="normal")
	len_limit_checkbox.configure(state="normal")
	progressbar.set(1)
	
	

def refresh_facts():
	activate_button.configure(state="disabled")
	len_limit_checkbox.configure(state="disabled")
	#refresh_button.configure(state="disabled")
	threading.Thread(target=generate_facts_list).start()
	


# def resource_path(relative_path):
# 	""" Get absolute path to resource, works for dev and for PyInstaller """
# 	try:
# 		# PyInstaller creates a temp folder and stores path in _MEIPASS
# 		base_path = sys._MEIPASS
# 	except Exception:
# 		base_path = os.path.abspath(".")

# 	return os.path.join(base_path, relative_path)


###Start of customtkinter layout	
if __name__ == '__main__':
	root = customtkinter.CTk()

	check_var = IntVar(value=1)

	customtkinter.set_appearance_mode("system")
	customtkinter.set_default_color_theme("blue")

	root.minsize(220, 430)

	root.title("")
	root.iconbitmap("logo.ico") 
	# root.iconbitmap(resource_path("logo.ico"))

	frame = customtkinter.CTkFrame(master=root)
	frame.pack(pady=0, padx=0, fill="both", expand=True)
	

	
	title_label = customtkinter.CTkLabel(master=frame, text="Press x to Cat", font=("Roboto", 24))
	title_label.pack(pady=(12,0), padx=10)

	

	animal_label = customtkinter.CTkLabel(frame, text="Animal", font=("Roboto", 14))
	animal_label.pack(padx=20, pady=(30, 0),)

	animal_optionemenu = customtkinter.CTkOptionMenu(frame, values=["Cat", "more incoming"], state="disabled")
	animal_optionemenu.pack(padx=20, pady=(0, 30))



	slider_label = customtkinter.CTkLabel(frame, text=f"Copy interval: 1 s", font=("Roboto", 14))
	slider_label.pack()

	slider = customtkinter.CTkSlider(master=frame, from_=0, to=10000, command=slider_event, number_of_steps=10000)
	slider.set(copy_interval)
	slider.pack(padx=20, pady=(0, 0))

	activate_button = customtkinter.CTkButton(master=frame, text="Activate", command=activate, fg_color=("#16A500","#14A007"), hover_color="#043100", font=("Roboto", 14))
	activate_button.pack(pady=(5,10), padx=10)

	len_limit_checkbox = customtkinter.CTkCheckBox(master=frame, text="Limit length for game chat", command=len_limit_checkbox_event,
												variable=check_var, onvalue=1, offvalue=0, checkbox_width=20, checkbox_height=20)
	len_limit_checkbox.pack(padx=20, pady=(0,10))
	
	progressbar = customtkinter.CTkProgressBar(master=frame, mode="indeterminate", determinate_speed=(50/(factAmount)), indeterminate_speed=2)
	progressbar.pack(padx=10, pady=(0, 15), side="bottom")
	progressbar.set(0)

	appearance_mode_optionemenu = customtkinter.CTkOptionMenu(frame, values=["System","Dark","Light"], 
		command=change_appearance_mode_event, height=5, font=("Roboto",10), button_color=("#3b8ed0","#1f6aa5"), button_hover_color=("#3b8ed0","#1f6aa5"))
	appearance_mode_optionemenu.pack(padx=20, pady=(0, 10), side="bottom")
	
	appearance_mode_label = customtkinter.CTkLabel(frame, text="Appearance", font=("Roboto", 11))
	appearance_mode_label.pack(padx=20, pady=(10, 0), side="bottom")
	
	#generate initial list
	refresh_facts()
	root.mainloop()

	


	
	
	










