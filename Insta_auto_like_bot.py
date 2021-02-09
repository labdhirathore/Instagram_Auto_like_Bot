import time
import pyautogui

# Give some time before it runs this file
time.sleep(3)


# Liking By heart symbol below a post
# the heart is located at x=70, y=694
#  x=76, y=757   38, 38, 38

class GuiCommands:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def navigate_to_heart(self, speed):
        position = pyautogui.locateOnScreen("save.png", confidence=0.8)
        # going all the way to the left of bookmark because we have a heart above too
        self.x = position[0]-800
        self.y = position[1]+10
        pyautogui.moveTo(self.x, self.y, duration=speed)
        print("Navigating to heart")
        time.sleep(5)

commands = GuiCommands(0, 0)

# commands.navigate_to_heart(1)
for i in range(3):
    try:
        commands.navigate_to_heart(1)
        if pyautogui.pixelMatchesColor(pyautogui.position().x, pyautogui.position().y, (237, 73, 86), tolerance=10):
            pyautogui.scroll(-1200)
            time.sleep(3)
        else:
            pyautogui.click()
            # print("Liking the post")
            time.sleep(3)

    except Exception as e:
        print(e)
        pyautogui.scroll(-1200)
        time.sleep(5)







