import tkinter as tk
from time import strftime, time, localtime
from math import pi, cos, sin


def style_digital_clock(label):
    label.config(
        font=('Helvetica', 60, 'bold'),   
        background='#333333',             
        foreground='#00FF00',             
        borderwidth=10,                   
        relief="groove",                  
        padx=20,                          
        pady=20                           
    )

class ClockApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Clock, Stopwatch, and Timer")

        # Main frame for holding clock and controls
        self.frame = tk.Frame(self.root)
        self.frame.pack(expand=True, fill='both')

        # Create the buttons for switching between views
        self.clock_button = tk.Button(self.frame, text="Digital Clock", command=self.show_digital_clock)
        self.analog_button = tk.Button(self.frame, text="Analog Clock", command=self.show_analog_clock)
        self.stopwatch_button = tk.Button(self.frame, text="Stopwatch", command=self.show_stopwatch)
        self.timer_button = tk.Button(self.frame, text="Timer", command=self.show_timer)

        # Display buttons below the clock
        self.clock_button.pack(side='left', padx=10, pady=10)
        self.analog_button.pack(side='left', padx=10, pady=10)
        self.stopwatch_button.pack(side='left', padx=10, pady=10)
        self.timer_button.pack(side='left', padx=10, pady=10)

        # Digital Clock setup
        self.digital_label = tk.Label(self.frame, font=('calibri', 40, 'bold'), background='black', foreground='white')

        # Analog Clock setup
        self.canvas_size = 400
        self.canvas = tk.Canvas(self.frame, width=self.canvas_size, height=self.canvas_size, bg='white')

        # Stopwatch and Timer setup
        self.stopwatch_time = 0
        self.timer_time = 0
        self.running_stopwatch = False
        self.running_timer = False
        self.stopwatch_label = tk.Label(self.frame, font=('calibri', 40, 'bold'))
        self.timer_label = tk.Label(self.frame, font=('calibri', 40, 'bold'))

        self.timer_input = tk.Entry(self.frame)
        self.timer_start_button = tk.Button(self.frame, text="Start Timer", command=self.start_timer)
        self.stopwatch_start_button = tk.Button(self.frame, text="Start Stopwatch", command=self.start_stopwatch)

        self.reset_button = tk.Button(self.frame, text="Reset", command=self.reset)

        # Initially, show the digital clock by default
        self.show_digital_clock()

    def show_digital_clock(self):
        self.clear_widgets()
        self.digital_label.pack(pady=20)
        style_digital_clock(self.digital_label)  # Add this line to style the clock
        self.update_digital_clock()

    def update_digital_clock(self):
        current_time = strftime('%H:%M:%S %p')
        self.digital_label.config(text=current_time)
        self.digital_label.after(1000, self.update_digital_clock)

    def show_analog_clock(self):
        self.clear_widgets()
        self.canvas.pack(pady=20)
        self.update_analog_clock()

    def update_analog_clock(self):
        self.canvas.delete("hands")
        now = localtime()
        sec_angle = (pi / 2) - (2 * pi / 60) * now.tm_sec
        min_angle = (pi / 2) - (2 * pi / 60) * now.tm_min
        hour_angle = (pi / 2) - (2 * pi / 12) * (now.tm_hour % 12 + now.tm_min / 60)

        clock_center = self.canvas_size // 2
        clock_radius = clock_center - 20

        # Draw hands
        self.draw_hand(sec_angle, clock_radius - 20, "red", 1)
        self.draw_hand(min_angle, clock_radius - 40, "blue", 2)
        self.draw_hand(hour_angle, clock_radius - 60, "black", 3)

        # Schedule next update
        self.root.after(1000, self.update_analog_clock)

    def draw_hand(self, angle, length, color, width):
        x_center = self.canvas_size // 2
        y_center = self.canvas_size // 2
        x_end = x_center + length * cos(angle)
        y_end = y_center - length * sin(angle)
        self.canvas.create_line(x_center, y_center, x_end, y_end, fill=color, width=width, tags="hands")

    def show_stopwatch(self):
        self.clear_widgets()
        self.stopwatch_label.pack(pady=20)
        self.stopwatch_start_button.pack(side='left', padx=10)
        self.reset_button.pack(side='left', padx=10)
        self.update_stopwatch()

    def start_stopwatch(self):
        self.running_stopwatch = True

    def update_stopwatch(self):
        if self.running_stopwatch:
            self.stopwatch_time += 1
        formatted_time = self.format_time(self.stopwatch_time)
        self.stopwatch_label.config(text=formatted_time)
        self.stopwatch_label.after(1000, self.update_stopwatch)

    def show_timer(self):
        self.clear_widgets()
        self.timer_label.pack(pady=20)
        self.timer_input.pack(side='left', padx=10)
        self.timer_start_button.pack(side='left', padx=10)
        self.reset_button.pack(side='left', padx=10)
        self.update_timer()

    def start_timer(self):
        try:
            self.timer_time = int(self.timer_input.get()) * 60
            self.running_timer = True
        except ValueError:
            pass

    def update_timer(self):
        if self.running_timer and self.timer_time > 0:
            self.timer_time -= 1
        formatted_time = self.format_time(self.timer_time)
        self.timer_label.config(text=formatted_time)
        self.timer_label.after(1000, self.update_timer)

    def reset(self):
        self.stopwatch_time = 0
        self.timer_time = 0
        self.running_stopwatch = False
        self.running_timer = False

    def format_time(self, secs):
        mins = secs // 60
        secs = secs % 60
        return f'{mins:02}:{secs:02}'

    def clear_widgets(self):
        # Clear all widgets (except buttons) to switch between modes
        for widget in self.frame.winfo_children():
            if widget not in [self.clock_button, self.analog_button, self.stopwatch_button, self.timer_button]:
                widget.pack_forget()

if __name__ == "__main__":
    root = tk.Tk()
    app = ClockApp(root)
    root.mainloop()
