# 🇮🇳 অসমীয়া প্ৰগ্ৰামিং প্লেটফৰ্ম (Assamese Programming Platform)

A web-based platform that enables programming in Assamese language. Write code in your mother tongue and see it transpile to Python in real-time!

![Platform Demo](https://img.shields.io/badge/Language-Assamese-brightgreen) ![Python](https://img.shields.io/badge/Python-3.8+-blue) ![Flask](https://img.shields.io/badge/Flask-3.0+-lightgrey)

## ✨ Features

- 🔄 **Real-time Transpilation** - Assamese code → Python code → Execution
- 📝 **Beautiful Code Editor** - Clean, modern interface for writing code
- 🎯 **4 Built-in Examples** - Hello World, Calculator, Loops, Conditionals
- ⚡ **Instant Execution** - See output immediately after running code
- 🌐 **Web-Based** - No installation needed, runs in browser
- 🎨 **Modern UI** - Gradient design with responsive layout

## 🚀 Live Demo

[View Live Demo](#) *(Add your deployed URL here)*

## 📸 Screenshots

*(Add screenshots of your platform here)*

## 🛠️ Installation

### Prerequisites
- Python 3.8 or higher
- pip (Python package manager)

### Setup

1. **Clone the repository**
```bash
git clone https://github.com/yourusername/assamese-programming-platform.git
cd assamese-programming-platform
```

2. **Install dependencies**
```bash
pip install -r requirements.txt
```

3. **Run the application**
```bash
python app.py
```

4. **Open in browser**
```
http://localhost:5000
```

## 📦 Project Structure

```
assamese-programming-platform/
│
├── app.py                      # Flask application
├── transpiler.py               # Core transpilation engine
├── assamese_keywords.json      # Assamese to Python keyword mappings
├── requirements.txt            # Python dependencies
│
├── templates/
│   └── index.html             # Web interface
│
└── README.md                  # Documentation
```

## 🔤 Supported Keywords

### Control Flow
- **যদি** → if
- **নহলে** → else
- **নহলে যদি** → elif
- **যেতিয়ালৈকে** → while
- **প্ৰতিটোৰ বাবে** → for

### Functions
- **প্ৰিণ্ট** → print
- **ইনপুট** → input
- **পৰিসৰ** → range
- **দৈৰ্ঘ্য** → len

### Operators
- **আৰু** → and
- **বা** → or
- **নহয়** → not
- **ভিতৰত** → in

### Numbers
- **০-৯** → 0-9 (Assamese numerals)

*[View complete keyword list](assamese_keywords.json)*

## 📝 Example Code

### Hello World
```assamese
প্ৰিণ্ট("নমস্কাৰ পৃথিৱী!")
প্ৰিণ্ট("অসমীয়া ভাষাত প্ৰগ্ৰামিং!")
```

### Calculator
```assamese
x = ১০
y = ৫
প্ৰিণ্ট("যোগফল:", x + y)
প্ৰিণ্ট("বিয়োগফল:", x - y)
```

### Loop
```assamese
প্ৰতিটোৰ বাবে i ভিতৰত পৰিসৰ(১, ৬):
    প্ৰিণ্ট("সংখ্যা:", i)
```


## 🔧 Technology Stack

- **Backend**: Python 3.8+, Flask
- **Frontend**: HTML5, CSS3, JavaScript
- **Transpilation**: Custom Python engine with regex-based parsing
- **Data Storage**: JSON for keyword mappings

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. Fork the repository
2. Create a new branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution
- Add more Assamese keywords
- Improve transpilation accuracy
- Add syntax highlighting
- Create more example programs
- Add support for other regional languages

## 📋 Roadmap

- [ ] Add syntax error highlighting
- [ ] Support for functions and classes
- [ ] File upload/download capability
- [ ] User accounts and code saving
- [ ] Mobile app version
- [ ] Support for other Indian languages (Bengali, Hindi, Tamil, etc.)
- [ ] Code sharing functionality
- [ ] Online IDE features (autocomplete, debugging)

## 🐛 Known Issues

- Indentation must be consistent (spaces or tabs)
- Complex nested structures may need manual review
- Some Python built-in functions not yet mapped


## 👨‍💻 Author

**Your Name**
- GitHub: https://github.com/vetrivelan999/Assamese-to-Python-Transpiler-Prototype
- Email: godofwarvetri999@gmail.com

## 🙏 Acknowledgments

- Inspired by the need for regional language programming in India
- Thanks to the Assamese language community
- Built with ❤️ for making programming accessible to everyone

## 📞 Support

If you have any questions or need help:
- Open an (https://github.com/vetrivelan999/Assamese-to-Python-Transpiler-Prototype)
- Email: godofwarvetri999@gmail.com

---

**Made with ❤️ in India** 🇮🇳

