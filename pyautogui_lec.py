import sys
# # print(sys.path)
# sys.path.append('/Users/ryotamiyake/opt/anaconda3/condabin')
import pyautogui as pag

# from time import sleep
# import sys
# import time
# screen_x,screen_y = pag.size()
# curmus_x,curmus_y = pag.position()
# print (u"printについてる[u]はunicodeにするのuでマルチバイト表記が化けるときにつけるよ")
# print (u"画面サイズ [" + str(screen_x) + "]/[" + str(screen_y) + "]")

print(pag.size())

# scr_w, scr_h = pag.size()
# print('スクリーンの幅:', scr_w, 'スクリーンの高さ:', scr_h)

# cent_x = scr_w/2
# cent_y = scr_h/2
# print('画面中央 x:', cent_x, 'y:', cent_y)

# print(pag.position())

# m_posi_x, m_posi_y = pag.position()
# print('現在のマウスの位置 x:', m_posi_x, 'y:', m_posi_y)

# try:
#     while True:
#         m_posi_x, m_posi_y = pag.position()
#         print('x:', m_posi_x, 'y:', m_posi_y)
#         sleep(1)
# except KeyboardInterrupt:
#     print('/n') # ctrl + C で終了

# pag.moveTo(200, 500)

# m_posi_x, m_posi_y = pag.position()
# pag.moveTo(m_posi_x+100, m_posi_y+100, 1)

# pag.move(100, 100, 1)

# m_posi_x, m_posi_y = pag.position()
# pag.dragTo(m_posi_x+100, m_posi_y+100, 1, button='left')

# pag.drag(100, 100, 1, button='left')

# pag.click()
# pag.click(button='right')

# pag.click(clicks=2, interval=0.1)
# pag.doubleClick()

# pag.click(button='right', clicks=3, interval=10)

# pag.mouseDown()
# pag.mouseUp()

# pag.mouseDown(); pag.mouseUp()

# pag.scroll(1000, 100, 200)


# x, y  = pag.position()
# pag.moveTo(1061, 394)
# pag.click()
# pag.write("Hello PyautoGUI!", interval=0.25)

# pag.press('enter')
# pag.press(['enter', 'enter', 'enter'])

# pag.moveTo(1046, 382)
# pag.click()
# pag.press('enter', presses=3, interval=0.25)

# print(pag.KEYBOARD_KEYS)

# pag.hotkey('command', 'shift', '5')

# img = pag.screenshot('screenshot.png', region=(0, 0, 200, 200))

# icon_loc = pag.locateOnScreen('icon.PNG')
# print(icon_loc)

# pag.alert(text='テストです', title='alert BOX', button='OK')

# pag.confirm(text='Activity Test', title='comfirm BOX', buttons=['OK', 'cancel'])

# test = pag.prompt(text='Test', title='Activity Test BOX', default='')
# print(test)

# test = pag.password(text='Test', title='Activity Test', default='', mask='*')
# print(test)