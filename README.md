# Clock, Stopwatch, Timer, and Analog Clock Application

This is a Python-based GUI application built with Tkinter that offers the following features:
- **Digital Clock**
- **Analog Clock**
- **Stopwatch**
- **Timer**

The application provides a user-friendly interface to switch between these functionalities and visually displays the time in various formats.

## Features

1. **Digital Clock**: Displays the current time in a digital format, updating every second.
2. **Analog Clock**: A graphical representation of the current time using an analog-style clock.
3. **Stopwatch**: Start, stop, and reset a stopwatch to measure elapsed time.
4. **Timer**: Set a timer in minutes, which counts down and updates every second.

## Technologies Used

- **Python**: Programming language used to create the application.
- **Tkinter**: A standard Python library for building graphical user interfaces (GUIs).

## Setup Instructions

### Prerequisites

- Python 3.x should be installed on your system. If not, download and install it from [here](https://www.python.org/downloads/).
- No external dependencies are needed, as Tkinter is included in the Python standard library.

### How to Run

1. Clone the repository or copy the script to your local machine.

2. Open a terminal or command prompt and navigate to the folder where the script is located.

3. Run the following command to execute the script:

    ```bash
    python proclock.py
    ```

4. The application window will appear with buttons for switching between the Digital Clock, Analog Clock, Stopwatch, and Timer.

## How to Use

1. **Digital Clock**: Click the "Digital Clock" button to display a digital clock. The time is displayed in HH:MM:SS format.

2. **Analog Clock**: Click the "Analog Clock" button to display an analog clock with moving hour, minute, and second hands.

3. **Stopwatch**: 
    - Click the "Stopwatch" button to switch to the stopwatch interface.
    - Press "Start Stopwatch" to begin counting time.
    - Press "Reset" to reset the stopwatch to zero.

4. **Timer**: 
    - Click the "Timer" button to switch to the timer interface.
    - Enter the desired time in minutes in the input field.
    - Press "Start Timer" to begin the countdown.
    - Press "Reset" to stop the timer and reset it to zero.

## Custom Styling

The digital clock is styled with a sleek, modern look, featuring:
- A dark background (`#333333`)
- Neon-green text (`#00FF00`)
- Bold, large Helvetica font
- 3D groove effect and padding around the text for an enhanced appearance.

You can modify the `style_digital_clock()` function in the script to further customize the appearance.

## Example Screenshot

[Include a screenshot of the application here, if possible]

## Future Enhancements

- Adding sound notifications for the timer completion.
- Custom time formatting options.
- Lap functionality for the stopwatch.
- More detailed user settings for customizing the appearance and behavior of the clocks.

## License

This project is licensed under the MIT License.

---

Enjoy using the Clock, Stopwatch, Timer, and Analog Clock application! Feel free to contribute and improve the project.
