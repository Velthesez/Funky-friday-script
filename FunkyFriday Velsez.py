import pyautogui
import keyboard
import time


positions = {
    (681, 942): {'color': (1, 255, 0), 'key': 'Z'},
    (801, 936): {'color': (1, 255, 0), 'key': 'X'},
    (923, 940): {'color': (255, 255, 255), 'key': 'N'},
    (1033, 940): {'color': (255, 255, 255), 'key': 'M'}
}


color_tolerance = 10


def is_color_similar(captured_color, target_color, tolerance=color_tolerance):
    for i in range(min(len(captured_color), len(target_color))):
        if not (target_color[i] - tolerance <= captured_color[i] <= target_color[i] + tolerance):
            return False
    return True


while True:
    for position, data in positions.items():
        x, y = position
        captured_color = pyautogui.pixel(x, y)

       
        if is_color_similar(captured_color, data['color']):
            print(f"Key pressed: {data['key']}")
            keyboard.press_and_release(data['key'])

    time.sleep(0.02)  