###############          ##########        #######   #######        #########      #######       #
#              #        #          #             #         #       #         #           #
#               #       #          #            #         #        #         #          #        #
#              #        #          #           #         #         #         #         #         #
###############         ############          #         #          ###########        #          #
#              #        #          #         #         #           #         #       #           #
#               #       #          #        #         #            #         #      #            #
#              #        #          #       #         #             #         #     #             #
###############         #          #      #######    #######       #         #    #######        #

# Developer: Mohammad Ali Bazzazi (me)

########################### START ###########################

import time, win32api, win32con, pyautogui, keyboard


def clicker(x, y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

# black 0,0,0
time.sleep(2)

# پیکسل ها را باید خودتان با توجه به روشی که در ویدیو گفتم پیدا کنید
while not keyboard.is_pressed('q'):
    try:
        if pyautogui.pixel(771, 442)[2] == 0:
            clicker(771, 442)
            
        if pyautogui.pixel(896, 442)[2] == 0:
            clicker(896, 442)

        if pyautogui.pixel(1022, 442)[2] == 0:
            clicker(1022, 442)

        if pyautogui.pixel(1152, 442)[2] == 0:
            clicker(1152, 442)
    except:
        pass
     
 ########################### END ###########################
