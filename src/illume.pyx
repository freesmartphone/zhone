cdef extern from "illume_kbd.c":
    void illume_kbd_show()
    void illume_kbd_hide()

def kbd_show():
    illume_kbd_show()

def kbd_hide():
    illume_kbd_hide()
