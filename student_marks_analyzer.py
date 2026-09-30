import tkinter as tk

x=tk.Tk()
x.title("Student Marks Analyzer")
x.geometry("500x700")

heading=tk.Label(x,text="Student Marks Analyzer")
heading.pack(pady=20)

label=tk.Label(x,text="Number of Students")
label.pack()

Entry=tk.Entry(x)
Entry.pack()

entries=[]

def get_students():
    n=int(Entry.get())

    for i in range(n):
        label=tk.Label(x,text=f"Student {i+1} Marks")
        label.pack()

        mark_entry=tk.Entry(x)
        mark_entry.pack()

        entries.append(mark_entry)

    calculate_button=tk.Button(x,text="Calculate",command=calculate)
    calculate_button.pack(pady=10)


def calculate():
    marks=[]

    for entry in entries:
        marks.append(int(entry.get()))

    average=sum(marks)/len(marks)
    highest=max(marks)
    lowest=min(marks)

    passed=0
    failed=0

    for mark in marks:
        if mark>=40:
            passed=passed+1
        else:
            failed=failed+1

    result_label.config(
        text=f"Average: {average}\n"
             f"Highest: {highest}\n"
             f"Lowest: {lowest}\n"
             f"Passed: {passed}\n"
             f"Failed: {failed}" )

button=tk.Button(x,text="Enter",command=get_students)
button.pack(pady=10)

result_label=tk.Label(x,text="",font=("Times New Roman",14))
result_label.pack(pady=10)

x.mainloop()
