
from eHooke.interface import Interface
import skimage
import matplotlib

app = Interface()
app.main_window.protocol("WM_DELETE_WINDOW", app.on_closing)
app.main_window.mainloop()

