# ❤️ When You Fall for a Programmer

A small Python animation that uses the **Turtle graphics library** and mathematical equations to draw a beautiful animated heart.

During the heart animation, the program displays the message:

> **"When you fall for a programmer"** ❤️

The project is a simple and fun demonstration of **Python Turtle graphics, mathematical equations, animation, and text rendering**.

---

## ✨ Features

* ❤️ Animated heart drawing
* 🐍 Built completely with Python
* 🎨 Uses Turtle graphics
* 🖤 Black background
* 💗 Pink/red heart animation
* ✍️ Displays text during the animation
* 📐 Uses mathematical equations to generate the heart shape
* ⏱️ Controlled drawing speed
* 🖥️ Simple graphical window

---

## 🛠️ Technologies Used

* **Python 3**
* **Turtle**
* **Math**
* **Time**

The project does not require any external Python packages.

---

## 📁 Project Structure

```text
programmer-heart/
│
├── main.py
├── README.md
└── .gitignore
```

---

## ⚙️ Requirements

You need:

* Python 3.x
* Tkinter/Turtle graphics support

Turtle is included with standard Python installations, so normally no additional package installation is required.

### Check Python

```bash
python --version
```

or:

```bash
python3 --version
```

---

## 🚀 How to Run

### Clone the repository

```bash
git clone https://github.com/namankarna0/Programmer-Heart.git
```

### Enter the project

```bash
cd programmer-heart
```

### Run the program

```bash
python main.py
```

On Linux:

```bash
python3 main.py
```

---

## ❤️ How It Works

The heart is generated using a mathematical parametric equation.

```python
x = scale * 16 * math.sin(math.radians(i)) ** 3

y = scale * (
    13 * math.cos(math.radians(i))
    - 5 * math.cos(math.radians(2 * i))
    - 2 * math.cos(math.radians(3 * i))
    - math.cos(math.radians(4 * i))
)
```

The program calculates an `(x, y)` coordinate for every angle from `0` to `359` degrees.

Turtle then moves between these points to draw the heart.

---

## 🎨 Animation

The program first draws the main heart:

```python
heart(15, "#ff4d6d", show_text=True)
```

While the heart is being drawn, the text appears halfway through the animation:

```text
When you fall for a programmer
```

Afterwards, additional smaller heart layers are drawn to create a darker outline/shadow effect.

---

## 🧠 Concepts Demonstrated

This project demonstrates:

* Python functions
* Turtle graphics
* Mathematical equations
* Trigonometry
* `sin()` and `cos()`
* Coordinate systems
* Loops
* Conditional statements
* Animation timing
* Text rendering
* Color handling
* Basic graphical programming

---

## 🖥️ Expected Output

The program opens a Turtle graphics window with:

```text
        ❤️
        
When you fall for a programmer
```

The heart is drawn progressively rather than appearing instantly.

---

## 🔮 Possible Improvements

Some ideas for future versions:

* 💕 Add animated floating hearts
* ✨ Add particle effects
* 🎵 Add background music
* 💗 Add multiple heart colors
* 💬 Add customizable messages
* 🌟 Add glowing effects
* 🎞️ Create a smoother animation
* 🖱️ Add mouse interaction
* ⌨️ Allow the user to enter a custom message
* 🎉 Add an ending animation

---

## 👨‍💻 Author

**Naman Karna**

Made with ❤️ and Python.

---

## 📄 License

This project is intended for **educational, personal, and fun purposes**.
