# 导入键鼠监听
import keyboard
# 导入 Adafruit_PCA9685 使用pwm
import Adafruit_PCA9685
# 将 Adafruit_PCA9685.PCA9685() 引用地址赋给pwm
pwm = Adafruit_PCA9685.PCA9685()

# 声明全局变量 em_main 电机
em_main = 0
# 声明全局变量 se_left 左舵机
se_left = 90
# 声明全局变量 se_right 右舵机
se_right = 90

# 设置频率为50hz
pwm.set_pwm_freq(50)

# 将舵机角度值转换为数值
def set_servo_angle(channel, angle):
    date = int(4096 * ((angle * 11) + 500) / 20000)
    pwm.set_pwm(channel, 0, date)

# 归零
def zero(all):
    global se_left
    global se_right
    global em_main
    if(all == 'all'):
        set_servo_angle(0, 0)
        set_servo_angle(1, 0)
        set_servo_angle(2, 0)
        em_main = 0
        se_left = 90
        se_right = 90
    else:
        set_servo_angle(1, 0)
        set_servo_angle(2, 0)
        se_left = 90
        se_right = 90
    print('电机速率：',em_main)
    print('舵机角度：',se_left)
    print('舵机角度：',se_right)

# 升降
def up_down(ud):
    global se_left
    global se_right
    if (ud == 'up'):
        se_right += 10
        se_left -= 10
    else:
        se_left += 10
        se_right -= 10
    set_servo_angle(1, se_right)
    set_servo_angle(2, se_left)
    print('舵机角度：',se_left)
    print('舵机角度：',se_right)

# 左转右转
def left_right(orientation):
    global se_right
    global se_left
    if(orientation == 'left'):
        se_left += 10
        se_right += 10
    else:
        se_left -= 10
        se_right -= 10
    set_servo_angle(1, se_right)
    set_servo_angle(2, se_left)
    print('舵机角度：',se_left)
    print('舵机角度：',se_right)

# 转速
def speed(value):
    global em_main
    if(value == 'add'):
        em_main += 1
    else:
        em_main -= 1
    set_servo_angle(0, em_main)
    print('电机速率：',em_main)

keyboard.add_hotkey('r', zero,args = ('se',))
keyboard.add_hotkey('v', zero,args = ('all',))
keyboard.add_hotkey('a', left_right,args = ('left',))
keyboard.add_hotkey('d', left_right,args = ('right',))
keyboard.add_hotkey('q', up_down,args = ('up',))
keyboard.add_hotkey('e', up_down,args = ('down',))
keyboard.add_hotkey('w', speed,args = ('add',))
keyboard.add_hotkey('s', speed,args = (em_main,))