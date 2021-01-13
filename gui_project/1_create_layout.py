import os
import tkinter.ttk as ttk
from tkinter import *
import time

root = Tk()
root.title("Gwanghyun GUI")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x")

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가")
btn_add_file.pack(side="left")

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 삭제")
btn_del_file.pack(side="right")

# 리스트 프레임
list_frame = Frame(root)
list_frame.pack(fill="both")

scrollbar = Scrollbar(list_frame)
scrollbar.pack(side="right", fill="y")

list_file = Listbox(list_frame, selectmode="extended", height=15, yscrollcommand=scrollbar)
list_file.pack(side="left", fill="both", expand=True)
scrollbar.config(command=list_file.yview)

# 저장 경로 프레임
save_path_frame = LabelFrame(root, text="저장경로")
save_path_frame.pack(fill="x")

e = Entry(save_path_frame)   #높이 변경
e.pack(side="left", fill="x", expand=True, ipady=4)

btn_search_file = Button(save_path_frame, width=10, text="찾아보기")
btn_search_file.pack(side="right")

# 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack()

label_opt_1 = Label(option_frame, width=8, text="가로넓이")
label_opt_1.pack(side="left")

list_opt_1_values = ["원본유지", "1024", "800", "640"]
list_opt_1 = ttk.Combobox(option_frame, width=10, state="readonly", values=list_opt_1_values)
list_opt_1.current(0)
list_opt_1.pack(side="left")

label_opt_2 = Label(option_frame, width=8, text="간격")
label_opt_2.pack(side="left")

list_opt_2_values = ["없음", "좁게", "보통", "넓게"]
list_opt_2 = ttk.Combobox(option_frame, width=10, state="readonly", values=list_opt_2_values)
list_opt_2.current(0)
list_opt_2.pack(side="left")

label_opt_3 = Label(option_frame, width=8, text="포맷")
label_opt_3.pack(side="left")

list_opt_3_values = ["PNG", "JPG", "BMP"]
list_opt_3 = ttk.Combobox(option_frame, width=10, state="readonly", values=list_opt_3_values)
list_opt_3.current(0)
list_opt_3.pack(side="left")

# 진행상황 프레임
progress_frame = LabelFrame(root, text="진행상황")
progress_frame.pack(fill="both")

p_var = DoubleVar()
progressbar = ttk.Progressbar(progress_frame, maximum=100, mode="determinate", variable=p_var)
# progressbar.start()
progressbar.pack(fill="x")

# 실행 프레임
btn_frame = Frame(root)
btn_frame.pack(fill="x")

btn_end = Button(btn_frame, padx=5, pady=5, width=12, text="닫기", command=root.quit)
btn_end.pack(side="right")

btn_start = Button(btn_frame, padx=5, pady=5, width=12, text="시작")
btn_start.pack(side="right")

root.resizable(False, False)    # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()