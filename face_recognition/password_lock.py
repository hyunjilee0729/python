import serial
import time
import tkinter as tk
from tkinter import messagebox

class PasswordLock:
    def __init__(self, port='COM4', baudrate=9600):
        self.arduino = serial.Serial(port=port, baudrate=baudrate, timeout=1)
        time.sleep(2)
        self.password = None
        
    def set_password(self, new_password):
        if len(new_password) >= 4:
            self.password = new_password
            return True
        return False
        
    def check_password(self, input_password):
        if self.password == input_password:
            self.arduino.write(f"{input_password}\n".encode())
            response = self.arduino.readline().decode().strip()
            return response == "SUCCESS"
        return False
        
    def close(self):
        self.arduino.close()

class PasswordGUI:
    def __init__(self):
        self.lock = PasswordLock()
        self.root = tk.Tk()
        self.root.title("비밀번호 시스템")
        self.root.geometry("300x450")
        self.setup_password_window()

    def setup_password_window(self):
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # 비밀번호 입력 필드
        self.new_password = tk.Entry(self.frame, show="*", justify='center')
        self.new_password.grid(row=0, column=0, columnspan=3, pady=10)

        # 상태 메시지 표시 Label
        self.status_label = tk.Label(self.frame, text="초기 비밀번호를 설정하세요", fg="black")
        self.status_label.grid(row=1, column=0, columnspan=3, pady=5)

        # 숫자 버튼 생성
        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            'C', '0', '확인'
        ]
        
        row = 2
        col = 0
        for button in buttons:
            if button == 'C':
                cmd = lambda: self.new_password.delete(0, tk.END)
            elif button == '확인':
                cmd = self.set_new_password
            else:
                cmd = lambda x=button: self.new_password.insert(tk.END, x)
            
            tk.Button(self.frame, text=button, width=5, height=2,
                     command=cmd).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

    def check_password_window(self):
        self.frame.destroy()
        self.frame = tk.Frame(self.root)
        self.frame.pack(pady=20)

        # 비밀번호 입력 필드
        self.password_entry = tk.Entry(self.frame, show="*", justify='center')
        self.password_entry.grid(row=0, column=0, columnspan=3, pady=10)

        # 상태 메시지 표시 Label
        self.status_label = tk.Label(self.frame, text="비밀번호를 입력하세요", fg="black")
        self.status_label.grid(row=1, column=0, columnspan=3, pady=5)

        buttons = [
            '7', '8', '9',
            '4', '5', '6',
            '1', '2', '3',
            'C', '0', '확인'
        ]
        
        row = 2
        col = 0
        for button in buttons:
            if button == 'C':
                cmd = lambda: self.password_entry.delete(0, tk.END)
            elif button == '확인':
                cmd = self.verify_password
            else:
                cmd = lambda x=button: self.password_entry.insert(tk.END, x)
            
            tk.Button(self.frame, text=button, width=5, height=2,
                     command=cmd).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 2:
                col = 0
                row += 1

    def set_new_password(self):
        new_pw = self.new_password.get()
        if len(new_pw) < 4:
            self.status_label.config(text="비밀번호는 최소 4자리 이상이어야 합니다!", fg="red")
            self.root.after(2000, lambda: self.status_label.config(text="초기 비밀번호를 설정하세요", fg="black"))
            return

        if self.lock.set_password(new_pw):
            self.status_label.config(text="비밀번호가 설정되었습니다!", fg="green")
            self.root.after(2000, self.check_password_window)
        else:
            self.status_label.config(text="비밀번호 설정에 실패했습니다!", fg="red")
            self.root.after(2000, lambda: self.status_label.config(text="초기 비밀번호를 설정하세요", fg="black"))

    def verify_password(self):
        password = self.password_entry.get()
        if self.lock.check_password(password):
            self.status_label.config(text="비밀번호가 일치합니다!", fg="green")
            self.root.after(4000, lambda: self.status_label.config(text="비밀번호를 입력하세요", fg="black"))
        else:
            self.status_label.config(text="비밀번호가 일치하지 않습니다!", fg="red")
            self.root.after(2000, lambda: self.status_label.config(text="비밀번호를 입력하세요", fg="black"))
        self.password_entry.delete(0, tk.END)

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = PasswordGUI()
    app.run()