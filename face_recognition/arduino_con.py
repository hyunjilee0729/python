import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import serial
import time

class ArduinoLEDControl:
    def __init__(self):
        try:
            self.arduino = serial.Serial('COM3', 9600, timeout=1)
            time.sleep(2)
        except:
            messagebox.showerror("오류", "아두이노 연결 실패")
            return

        # LED 상태 변수 추가
        self.red_led_state = False
        self.blue_led_state = False

        self.window = tk.Tk()
        self.window.title("Arduino LED 제어")
        self.window.geometry("400x400")

        # 빨간 LED 제어
        self.red_frame = tk.LabelFrame(self.window, text="빨간 LED 제어", padx=10, pady=10)
        self.red_frame.pack(fill="x", padx=10, pady=5)
        
        self.red_status = tk.Label(self.red_frame, text="빨간 LED 상태: OFF")
        self.red_status.pack()
        
        tk.Button(self.red_frame, text="ON", command=self.red_led_on).pack(side=tk.LEFT, padx=5)
        tk.Button(self.red_frame, text="OFF", command=self.red_led_off).pack(side=tk.LEFT, padx=5)
        
        self.red_scale = ttk.Scale(self.red_frame, from_=0, to=255, orient='horizontal',
                                command=self.red_brightness)
        self.red_scale.pack(fill='x', padx=5)
        self.red_scale.state(['disabled'])

        # 파란 LED 제어
        self.blue_frame = tk.LabelFrame(self.window, text="파란 LED 제어", padx=10, pady=10)
        self.blue_frame.pack(fill="x", padx=10, pady=5)
        
        self.blue_status = tk.Label(self.blue_frame, text="파란 LED 상태: OFF")
        self.blue_status.pack()
        
        tk.Button(self.blue_frame, text="ON", command=self.blue_led_on).pack(side=tk.LEFT, padx=5)
        tk.Button(self.blue_frame, text="OFF", command=self.blue_led_off).pack(side=tk.LEFT, padx=5)
        
        self.blue_scale = ttk.Scale(self.blue_frame, from_=0, to=255, orient='horizontal',
                                command=self.blue_brightness)
        self.blue_scale.pack(fill='x', padx=5)
        self.blue_scale.state(['disabled'])

        self.window.protocol("WM_DELETE_WINDOW", self.on_closing)
        self.window.mainloop()

    def red_brightness(self, value):
        if self.red_led_state:
            brightness = int(float(value))
            self.arduino.write(f'R{brightness}\n'.encode())
            self.red_status.config(text=f"빨간 LED 밝기: {brightness}")

    def blue_brightness(self, value):
        if self.blue_led_state:
            brightness = int(float(value))
            self.arduino.write(f'B{brightness}\n'.encode())
            self.blue_status.config(text=f"파란 LED 밝기: {brightness}")

    def red_led_on(self):
        self.red_led_state = True
        self.red_scale.state(['!disabled'])
        self.red_scale.set(255)
        self.red_brightness(255)
        self.red_status.config(text="빨간 LED 상태: ON")

    def red_led_off(self):
        self.red_led_state = False
        self.red_scale.state(['disabled'])
        self.red_scale.set(0)
        self.arduino.write(f'R0\n'.encode())  # 밝기를 0으로 설정
        self.red_status.config(text="빨간 LED 상태: OFF")

    def blue_led_on(self):
        self.blue_led_state = True
        self.blue_scale.state(['!disabled'])
        self.blue_scale.set(255)
        self.blue_brightness(255)
        self.blue_status.config(text="파란 LED 상태: ON")

    def blue_led_off(self):
        self.blue_led_state = False
        self.blue_scale.state(['disabled'])
        self.blue_scale.set(0)
        self.arduino.write(f'B0\n'.encode())  # 밝기를 0으로 설정
        self.blue_status.config(text="파란 LED 상태: OFF")

    def on_closing(self):
        if hasattr(self, 'arduino') and self.arduino.is_open:
            self.arduino.close()
        self.window.destroy()

if __name__ == "__main__":
    app = ArduinoLEDControl()