import tkinter as tk

H, W = 600, 800

def graf(data):
    win = tk.Tk()
    cv = tk.Canvas(win, width=W, height=H, bg="white"); cv.pack()

    step = W / (len(data) - 1)
    mx = max(data)

    pts = [(i * step, (H+50) - (v / mx) * H) for i, v in enumerate(data)]

    for a, b in zip(pts, pts[1:]):
        cv.create_line(a[0], a[1], b[0], b[1], width=2)

    win.mainloop()
