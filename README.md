# MediCore Laboratory Services - Profile Website

A professional, modern website for medical laboratory services built with Python Flask. This website provides comprehensive information about laboratory services, online appointment booking, and secure result access.

## Features

### 🏥 Professional Medical Laboratory Website
- **Modern Design**: Clean, professional interface with medical industry styling
- **Responsive Layout**: Fully responsive design that works on all devices
- **Accessibility**: WCAG compliant with proper semantic HTML

### 🔬 Core Functionality
- **Home Page**: Laboratory overview with featured services and statistics
- **Services Page**: Comprehensive listing of all laboratory tests and services
- **About Page**: Laboratory history, team information, and certifications
- **Contact Page**: Contact information, operating hours, and contact form
- **Appointment Booking**: Online appointment scheduling system
- **Results Portal**: Secure patient results access (demo implementation)

### 🎨 Design Features
- **Professional Color Scheme**: Medical blue primary color with green accents
- **Modern Typography**: Clean, readable Inter font family
- **Interactive Elements**: Hover effects, smooth transitions, and animations
- **Icon Integration**: Font Awesome icons throughout the interface
- **Bootstrap Framework**: Responsive grid system and components

### 🛡️ Security & Compliance
- **HIPAA Considerations**: Privacy-focused design and data handling
- **Secure Forms**: CSRF protection and form validation
- **Patient Privacy**: Secure result access with authentication
- **Data Protection**: Industry-standard security measures

## Technology Stack

- **Backend**: Python 3.x with Flask framework
- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Bootstrap 5.3.0 with custom CSS
- **Icons**: Font Awesome 6.0.0
- **Fonts**: Google Fonts (Inter)
- **Server**: Gunicorn WSGI server

## Installation & Setup

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Quick Start

1. **Clone or download the project files**
   ```bash
   # If using git
   git clone <repository-url>
   cd medical-lab-website
   
   # Or simply ensure all files are in your project directory
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   
   # Activate virtual environment
   # On Windows:
   venv\Scripts\activate
   # On macOS/Linux:
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**
   ```bash
   python app.py
   ```

5. **Access the website**
   Open your browser and navigate to `http://localhost:5000`

### Production Deployment

For production deployment, use Gunicorn:

```bash
gunicorn -w 4 -b 0.0.0.0:5000 app:app
```

## Project Structure

```
medical-lab-website/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── README.md             # Project documentation
├── templates/            # HTML templates
│   ├── base.html         # Base template with navigation and footer
│   ├── index.html        # Home page
│   ├── services.html     # Services listing page
│   ├── about.html        # About us page
│   ├── contact.html      # Contact page
│   ├── appointment.html  # Appointment booking page
│   └── results.html      # Patient results portal
└── static/              # Static files (created automatically)
    ├── css/             # Custom CSS files
    ├── js/              # Custom JavaScript files
    └── img/             # Image files
```

## Key Pages & Features

### Home Page (`/`)
- Hero section with laboratory branding
- Key statistics and achievements
- Featured services showcase
- Why choose us section
- Call-to-action buttons

### Services Page (`/services`)
- Complete service catalog
- Detailed test descriptions
- Turnaround times
- Pricing information
- Interactive service accordion

### About Page (`/about`)
- Laboratory history and mission
- Team member profiles
- Certifications and accreditations
- Quality assurance information
- Core values presentation

### Contact Page (`/contact`)
- Contact information and hours
- Interactive contact form
- Location map placeholder
- Accessibility information
- Emergency contact details

### Appointment Booking (`/appointment`)
- Comprehensive patient information form
- Test type selection
- Insurance information collection
- Date and time scheduling
- Special instructions handling

### Results Portal (`/results`)
- Secure login simulation
- Patient result access
- Help and support information
- FAQ section
- Demo implementation with notifications

## Customization

### Laboratory Information
Edit the `lab_info` dictionary in `app.py` to customize:
- Laboratory name and tagline
- Contact information
- Operating hours
- Address details

### Services
Modify the `services` list in `app.py` to add/edit:
- Service names and descriptions
- Turnaround times
- Service icons

### Team Members
Update the `team_members` list in `app.py` to include:
- Staff names and positions
- Credentials and specializations
- Profile information

### Styling
- Custom CSS can be added to `static/css/`
- Color scheme variables are defined in `base.html`
- Bootstrap classes can be modified throughout templates

## Form Handling

The application includes form handling for:
- **Contact Form**: Processes inquiries and displays confirmation
- **Appointment Form**: Collects patient information and scheduling preferences
- **Results Access**: Demo authentication system

All forms include:
- Client-side validation
- CSRF protection
- Flash message feedback
- Responsive design

## Security Considerations

### Current Implementation
- Flask secret key for session security
- Form validation and sanitization
- XSS protection through Jinja2 templating
- Basic input validation

### Production Recommendations
- Use environment variables for sensitive configuration
- Implement proper database integration
- Add SSL/TLS encryption
- Implement proper authentication and authorization
- Add rate limiting and CAPTCHA
- Regular security audits

## Browser Support

- Chrome 90+
- Firefox 88+
- Safari 14+
- Edge 90+
- Mobile browsers (iOS Safari, Chrome Mobile)

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Support

For support and questions:
- Check the documentation
- Review the code comments
- Open an issue for bugs or feature requests

## Acknowledgments

- Bootstrap team for the responsive framework
- Font Awesome for the icon library
- Google Fonts for typography
- Flask community for the excellent framework

---

**Note**: This is a demonstration website. For production use in a medical environment, ensure compliance with HIPAA, HITECH, and other relevant healthcare regulations. Implement proper security measures, database integration, and user authentication systems.