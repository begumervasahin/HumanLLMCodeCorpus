import tkinter as tk
def fibSeq():
    getNum = int(numEntry.get())
    seqNum = [0, 1]
    for sNum in range(2, getNum + 1):
        calNum = seqNum[-1] + seqNum[-2]
        seqNum.append(calNum)
    if getNum == 0:
        result = 0
    elif getNum == 1:
        result = 1
    else:
        result = seqNum[-1]
    resLbl.config(text=f"{getNum}th term is: {result}")
mw = tk.Tk()
mw.title("Fibonacci Sequence")
numEntry = tk.Entry(mw)
numEntry.grid(row=0, column=0, padx=5, pady=5)
numEntry.focus()
calBtn = tk.Button(mw, text="Find Fibonacci Term Sequence", command=fibSeq)
calBtn.grid(row=0, column=1, padx=5, pady=5)
resLbl = tk.Label(mw, text="Result")
resLbl.grid(row=1, column=0, sticky="w", padx=5, pady=5)
mw.mainloop()