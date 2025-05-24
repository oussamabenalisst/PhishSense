<div align="center">
  <img src="assets/logo.png" alt="PhishSense Logo" width="200" height="200" style="border-radius: 20px; margin: 20px 0;">

# Contributing to PhishSense 🦈

  <p align="center">
    <em>Help us make PhishSense better!</em>
  </p>
</div>

---

First off, thank you for considering contributing to PhishSense! It's people like you that make PhishSense such a great tool.

## 📜 Code of Conduct

By participating in this project, you are expected to uphold our Code of Conduct:

<div align="center">
  <table>
    <tr>
      <td align="center">🎓</td>
      <td>Use the tool for educational and research purposes only</td>
    </tr>
    <tr>
      <td align="center">🔒</td>
      <td>Respect privacy and security guidelines</td>
    </tr>
    <tr>
      <td align="center">💬</td>
      <td>Be constructive and helpful in your communication</td>
    </tr>
    <tr>
      <td align="center">🤝</td>
      <td>Respect different viewpoints and experiences</td>
    </tr>
  </table>
</div>

## How Can I Contribute?

### Reporting Bugs 🐛

Before creating bug reports, please check the existing issues to avoid duplicates. When you create a bug report, include as many details as possible:

- Your operating system and relevant software versions (PHP, Python, XAMPP)
- Step-by-step description to reproduce the issue
- Expected behavior vs actual behavior
- Any relevant screenshots or error messages

### Suggesting Enhancements ✨

We love suggestions! When suggesting enhancements:

- Use a clear and descriptive title
- Provide a detailed description of the proposed functionality
- Explain why this enhancement would be useful
- Include code examples if applicable

### Development Process 🛠️

1. Fork the repository
2. Create a new branch for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Make your changes following our coding standards
4. Test your changes thoroughly
5. Commit your changes:
   ```bash
   git commit -m "Add: brief description of your changes"
   ```
6. Push to your fork:
   ```bash
   git push origin feature/your-feature-name
   ```
7. Open a Pull Request

### Coding Standards 📝

#### Python Code

- Follow PEP 8 style guide
- Use meaningful variable and function names
- Add comments for complex logic
- Include docstrings for functions and classes

#### PHP Code

- Follow PSR-12 coding standards
- Use proper error handling
- Sanitize all user inputs
- Include appropriate security headers

#### JavaScript Code

- Use ES6+ features when appropriate
- Follow camelCase naming convention
- Add error handling for async operations
- Comment complex logic

#### HTML/CSS

- Use semantic HTML5 elements
- Follow BEM naming convention for CSS
- Ensure responsive design
- Maintain dark theme consistency

### File Structure 📁

Please maintain the existing file structure:

<div align="center">
  <table>
    <tr>
      <th colspan="3">Project Structure</th>
    </tr>
    <tr>
      <td><b>Directory</b></td>
      <td><b>File</b></td>
      <td><b>Purpose</b></td>
    </tr>
    <tr>
      <td>assets/</td>
      <td>logo.png</td>
      <td>Project logo and branding</td>
    </tr>
    <tr>
      <td>assets/</td>
      <td>style.css</td>
      <td>UI styling and themes</td>
    </tr>
    <tr>
      <td>scripts/</td>
      <td>analysis.py</td>
      <td>Data analysis tool</td>
    </tr>
    <tr>
      <td>scripts/</td>
      <td>Packages.sh</td>
      <td>Dependencies installer</td>
    </tr>
    <tr>
      <td>scripts/</td>
      <td>scripts.js</td>
      <td>Frontend functionality</td>
    </tr>
    <tr>
      <td>/</td>
      <td>index.html</td>
      <td>Main web interface</td>
    </tr>
    <tr>
      <td>/</td>
      <td>save_to_csv.php</td>
      <td>Data storage backend</td>
    </tr>
    <tr>
      <td>/</td>
      <td>result.csv</td>
      <td>Collected data storage</td>
    </tr>
    <tr>
      <td>/</td>
      <td>typesPages.dat</td>
      <td>Page templates storage</td>
    </tr>
  </table>
</div>

### Testing 🧪

Before submitting your changes:

1. Test the web interface functionality
2. Verify IP detection and logging
3. Test data storage and retrieval
4. Check analysis tool commands
5. Ensure cross-browser compatibility
6. Verify responsive design
7. Test security features

### Documentation 📚

- Update README.md if you add new features
- Document new analysis tool commands
- Add JSDoc comments for JavaScript functions
- Include PHPDoc blocks for PHP functions
- Update Python docstrings as needed

### Security Considerations 🔒

When contributing, ensure your code:

- Sanitizes all user inputs
- Uses proper error handling
- Implements CORS security
- Follows secure coding practices
- Doesn't expose sensitive information

## Pull Request Process

1. Update the README.md with details of any interface changes
2. Update the version numbers in:
   - README.md badges
   - package.json (if added)
   - Any relevant documentation
3. Your PR will be merged once you have the sign-off of at least one maintainer

## Questions? 💭

Feel free to create an issue tagged as 'question' if you need any clarification.

Thank you for contributing to PhishSense! 🙏
