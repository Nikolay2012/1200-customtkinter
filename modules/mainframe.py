import customtkinter
from .read_json import read_json
import json

main_frame = customtkinter.CTk(fg_color= ('#FE2EF7'))

config = read_json(name_json= 'config.json')
# print(json.dumps(config, indent= 4))
#
WIDTH = config['mainframe']['width']
HEIGHT = config['mainframe']['height']
#
main_frame.geometry(f'{WIDTH}x{HEIGHT}')
