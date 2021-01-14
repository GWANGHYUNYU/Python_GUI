import os
import tkinter.ttk as ttk
from tkinter import *  # __all__
from tkinter import filedialog
import tkinter.messagebox as msgbox
from PIL import Image
import time

root = Tk()
root.title("Gwanghyun GUI")

# 파일 프레임 (파일 추가, 선택 삭제)
file_frame = Frame(root)
file_frame.pack(fill="x")


# 파일 추가
def add_file():
    files = filedialog.askopenfilenames(title="이미지 파일을 선택하세요",
                                        filetypes=(("PNG 파일", "*.png"), ("모든 파일", "*.*")),
                                        initialdir=os.getcwd())  # 최초에 C:/ 경로를 보여줌
    # 사용자가 선택한 파일 목록
    for file in files:
        list_file.insert(END, file)


# 파일 삭제
def del_file():
    # print(list_file.curselection())
    for index in reversed(list_file.curselection()):
        list_file.delete(index)


# 저장 경로
def browse_path():
    folder_selected = filedialog.askdirectory(initialdir=os.getcwd())
    if folder_selected == '':  # 사용자가 취소를 누를 때
        return
    # print(folder_selected)
    e.delete(0, END)
    e.insert(0, folder_selected)

def merge_image():
    # print("가로넓이 : ", list_opt_1.get())
    # print("간격 : ", list_opt_2.get())
    # print("포맷 : ", list_opt_3.get())
    try:
        # 가로넓이
        img_width = list_opt_1.get()
        if img_width == "원본유지":
            img_width = -1  # -1 일때는 원본 기준으로
        else:
            img_width = int(img_width)

        # 간격
        img_space = list_opt_2.get()
        if img_space == "좁게":
            img_space = 30
        elif img_space == "보통":
            img_space = 60
        elif img_space == "넓게":
            img_space = 90
        else: # 없음
            img_space = 0

        # 포맷
        img_format = list_opt_3.get().lower()

        images = [Image.open(x) for x in list_file.get(0, END)]

        # 이미지 사이즈 리스트에 넣어서 하나씩 처리
        image_sizes = []    # (width1, height1), (width2, height2), ...]
        if img_width > -1:
            image_sizes = [(int(img_width), int(img_width * x.size[1] / x.size[0])) for x in images]
        else:
            # 원본 사이즈 사용
            image_sizes = [(x.size[0], x.size[1]) for x in images]



        # size -> size[0] : width, size[1] : height
        widths, heights = zip(*image_sizes)

        # 최대 넓이, 전체 높이 구해옴
        max_width, total_height = max(widths), sum(heights)

        # 스케치북 준비
        if img_space > 0:   # 이미지 간격 옵션 적용
            total_height += (img_space * (len(images) - 1))

        result_img = Image.new("RGB", (max_width, total_height), (255, 255, 255))   # 배경
        y_offset = 0    # y 위치

        for idx, img in enumerate(images):
            # width가 원본유지가 아닐 때에는 이미지 크기 조정
            if img_width > -1:
                img = img.resize(image_sizes[idx])

            result_img.paste(img, (0, y_offset))
            y_offset += (img.size[1] + img_space)  # height 값 + 사용자가 지정한 간격

            progress = (idx + 1) / len(images) * 100    # 실제 % 정보 저장
            p_var.set(progress)
            progressbar.update()

        # 포맷 옵션 처리
        file_name = "이미지 합치기." + img_format
        dest_path = os.path.join(e.get(), file_name)
        result_img.save(dest_path)
        msgbox.showinfo("알림", "작업이 완료되었습니다.")
    except Exception as err:
        msgbox.showerror("에러", err)

# 시작
def start():
    # 파일 목록 확인
    if list_file.size() == 0:
        msgbox.showwarning("경고", "이미지 파일을 추가하세요")
        return

    if len(e.get()) == 0:
        msgbox.showwarning("경고", "저장 경로를 설정하세요")
        return

    # 이미지 통합 작업
    merge_image()

btn_add_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 추가", command=add_file)
btn_add_file.pack(side="left", padx=5, pady=5)

btn_del_file = Button(file_frame, padx=5, pady=5, width=12, text="파일 삭제", command=del_file)
btn_del_file.pack(side="right", padx=5, pady=5)

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
save_path_frame.pack(fill="x", ipady=5)

e = Entry(save_path_frame)  # 높이 변경
e.pack(side="left", fill="x", expand=True, padx=5, pady=5, ipady=4)

btn_search_file = Button(save_path_frame, width=10, text="찾아보기", command=browse_path)
btn_search_file.pack(side="right", padx=5, pady=5)

# 옵션 프레임
option_frame = LabelFrame(root, text="옵션")
option_frame.pack(ipady=5)

label_opt_1 = Label(option_frame, width=8, text="가로넓이")
label_opt_1.pack(side="left", padx=5, pady=5)

list_opt_1_values = ["원본유지", "1024", "800", "640"]
list_opt_1 = ttk.Combobox(option_frame, width=10, state="readonly", values=list_opt_1_values)
list_opt_1.current(0)
list_opt_1.pack(side="left", padx=5, pady=5)

label_opt_2 = Label(option_frame, width=8, text="간격")
label_opt_2.pack(side="left", padx=5, pady=5)

list_opt_2_values = ["없음", "좁게", "보통", "넓게"]
list_opt_2 = ttk.Combobox(option_frame, width=10, state="readonly", values=list_opt_2_values)
list_opt_2.current(0)
list_opt_2.pack(side="left", padx=5, pady=5)

label_opt_3 = Label(option_frame, width=8, text="포맷")
label_opt_3.pack(side="left", padx=5, pady=5)

list_opt_3_values = ["PNG", "JPG", "BMP"]
list_opt_3 = ttk.Combobox(option_frame, width=10, state="readonly", values=list_opt_3_values)
list_opt_3.current(0)
list_opt_3.pack(side="left", padx=5, pady=5)

# 진행상황 프레임
progress_frame = LabelFrame(root, text="진행상황")
progress_frame.pack(fill="both", ipady=5)

p_var = DoubleVar()
progressbar = ttk.Progressbar(progress_frame, maximum=100, mode="determinate", variable=p_var)
# progressbar.start()
progressbar.pack(fill="x", padx=5, pady=5)

# 실행 프레임
btn_frame = Frame(root)
btn_frame.pack(fill="x", padx=5, pady=5)

btn_end = Button(btn_frame, padx=5, pady=5, width=12, text="닫기", command=root.quit)
btn_end.pack(side="right", padx=5, pady=5)

btn_start = Button(btn_frame, padx=5, pady=5, width=12, text="시작", command=start)
btn_start.pack(side="right")

root.resizable(False, False)  # x(너비), y(높이) 값 변경 불가 (창 크기 변경 불가)
root.mainloop()