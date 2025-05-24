# 🦈 PhishSense

<h3><em>This application is for educational purposes.</em></h3>

<div align="center">
  <img src="assets/logo.png" alt="PhishSense Logo" width="500" height="500" style="border-radius: 20px; margin: 20px 0;">

  <p align="center">
    <em>Next-Generation Phishing Detection & Analysis Platform</em>
  </p>
  
  <p align="center">
    <img src="https://img.shields.io/badge/version-1.0.0-blue.svg" alt="version"/>
    <img src="https://img.shields.io/badge/python-3.x-green.svg" alt="python"/>
    <img src="https://img.shields.io/badge/php-7.x-purple.svg" alt="php"/>
    <img src="https://img.shields.io/badge/license-MIT-red.svg" alt="license"/>
  </p>
</div>

---

## 🎯 What is PhishSense?

PhishSense is a comprehensive security research platform designed for simulating and analyzing phishing attempts in a controlled environment. It combines modern web technologies with powerful analysis tools to help security professionals understand phishing tactics and improve defense strategies.

## 🚀 Key Features

- 🌐 **Modern Web Interface**

  - Sleek, responsive design with dark theme
  - Real-time form validation
  - Animated UI elements
  - Cross-platform compatibility

- 🔒 **Security Features**

  - Automated IP detection and logging
  - Secure data handling
  - Cross-Origin Resource Sharing (CORS) support
  - Input sanitization and validation

- 📊 **Advanced Analysis Tools**

  - Command-line data management interface
  - Real-time data filtering and cleaning
  - Multiple page template support
  - Comprehensive search capabilities

- 💾 **Data Management**
  - CSV-based storage system
  - Record modification and deletion
  - Bulk data operations
  - Template management system

## 🛠️ Technical Architecture

### Frontend (`index.html`, `assets/style.css`, `scripts/scripts.js`)

- Modern, responsive UI with dark theme
- Asynchronous data submission
- Dynamic IP address detection
- Real-time form validation

### Backend (`save_to_csv.php`)

- RESTful API endpoint
- CORS-enabled
- Secure data handling
- CSV data storage

### Analysis Tool (`scripts/analysis.py`)

- Interactive CLI interface
- Data manipulation features
- Template management
- Record filtering and searching

### Data Storage

- `result.csv`: Structured data storage
- `typesPages.dat`: Page template storage

## 🔧 Requirements

### Server Requirements

- XAMPP or similar web server stack
- PHP 7.x or higher
- Python 3.x

### Python Dependencies

- pandas: Data manipulation
- pyfiglet: CLI formatting
- colorama: Terminal colors
- rich: Enhanced terminal output

## ⚙️ Installation

1. Clone the repository:

```bash
git clone https://github.com/yourusername/phishsense.git
cd phishsense
```

2. Install Python dependencies:

```bash
cd scripts
bash Packages.sh
```

3. Configure web server to serve the application at your desired URL

## 📖 Usage

### Web Interface

Access the web interface through your configured web server URL. The interface provides:

- User input collection
- Automatic IP detection
- Real-time data submission

### Add a Web Page

How to run any page and what things should be added

- Use `-Ap` to add page web in data type
- Add script src to your Code `<script src="./scripts/scripts.js"></script>`
- Change user input id to `id=usernamefi`
- Change passwd input id to `id=passwordfi`
- Change type of button to `type = "button"`
- add onclick in button `onclick="addtocsv(type, url)"`<br> type= name page <br> url = When you click where does it go?

### Analysis Tool Commands

Run the tool using: `python scripts/analysis.py`

Data Management:

- `-a`: View all records
- `-A`: Add new record
- `-M`: Modify record
- `-S`: Delete record
- `-Sa`: Reset database
- `-f`: Filter/clean data
- `-s`: Save changes

Page Management:

- `-Cp`: Change page content
- `-Ap`: Add new page
- `-ap`: List page types
- `-Sp`: Delete page type

Utility Commands:

- `-RE`: Restart application
- `-c`: Clear screen
- `-h`: Show help
- `-q`: Exit

## 🔐 Security Considerations

This tool is designed for:

- Educational purposes
- Security research
- Authorized testing only

**Important:** Always obtain proper authorization before conducting any security tests.

## 👥 Contributing

We welcome contributions! Please read [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) for guidelines.

## ⚠️ Disclaimer

This tool is intended for educational and research purposes only. Users must:

- Obtain proper authorization before testing
- Use in controlled environments only
- Accept responsibility for their actions

The authors are not responsible for any misuse or damage.

## ✍️ Author

Oussama Benali
