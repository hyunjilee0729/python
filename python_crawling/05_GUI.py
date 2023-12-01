import tkinter as tk
from tkinter.scrolledtext import ScrolledText
import webbrowser

def show_youtube():
    user_birthday = entry.get()
    if user_birthday:
        search_query = f"https://www.youtube.com/results?search_query={user_birthday}"
        result_text.delete(1.0, tk.END)  # 이전 내용 삭제
        result_text.insert(tk.END, f"유튜브 검색 결과: {search_query}")
        webbrowser.open(search_query)

# Tkinter 윈도우 생성
window = tk.Tk()
window.title("생년월일로 YouTube 검색")

# 레이블과 Entry 위젯 추가
label = tk.Label(window, text="생년월일(YYYYMMDD):")
label.pack()

entry = tk.Entry(window)
entry.pack()

# 결과를 표시할 텍스트 박스 추가
result_text = ScrolledText(window, height=10, width=40, wrap=tk.WORD)
result_text.pack(pady=10)

# 확인 버튼 추가
confirm_button = tk.Button(window, text="확인", command=show_youtube)
confirm_button.pack(pady=10)

# GUI 실행
window.mainloop()
