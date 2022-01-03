import screen_brightness_control as sbc

current_brightness = sbc.get_brightness()
print(current_brightness)

sbc.set_brightness(100)