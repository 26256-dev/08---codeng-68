import tkinter as tk
from tkinter import messagebox

def convert():
    try:
        amount = float(entry_amount.get())
        currency = choice.get()

        if currency == "EUR":
            thb = amount * 37.0
        elif currency == "USD":
            thb = amount * 34.5
        elif currency == "JPY":
            thb = amount * 0.22
        else:
            messagebox.showerror("Error", "กรุณาเลือกสกุลเงิน")
            return

        result_label.config(text=f"{thb:.2f} บาท")

    except ValueError:
        messagebox.showerror("Error", "กรุณากรอกตัวเลข")

# สร้างหน้าต่างหลัก
root = tk.Tk()
root.title("โปรแกรมแปลงสกุลเงิน")
root.geometry("300x200")

# ตัวเลือกสกุลเงิน
choice = tk.StringVar()
choice.set("EUR")

tk.Label(root, text="เลือกสกุลเงิน").pack()
tk.OptionMenu(root, choice, "EUR", "USD", "JPY").pack()

# ช่องกรอกจำนวนเงิน
tk.Label(root, text="กรอกจำนวนเงิน").pack()
entry_amount = tk.Entry(root)
entry_amount.pack()

# ปุ่มแปลงค่า
tk.Button(root, text="แปลงค่า", command=convert).pack(pady=10)

# แสดงผลลัพธ์
result_label = tk.Label(root, text="0 บาท", font=("Arial", 12))
result_label.pack()

root.mainloop()



