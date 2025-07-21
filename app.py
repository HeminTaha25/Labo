from flask import Flask, render_template, request, flash, redirect, url_for
from datetime import datetime
import os

app = Flask(__name__)
app.secret_key = 'medical_lab_secret_key_2024'

# Sample data for the laboratory
lab_info = {
    'name': 'MediCore Laboratory Services',
    'tagline': 'Excellence in Medical Diagnostics',
    'established': 2010,
    'phone': '+1 (555) 123-4567',
    'email': 'info@medicorelab.com',
    'address': '123 Medical Center Drive, Healthcare City, HC 12345',
    'hours': {
        'weekdays': '7:00 AM - 8:00 PM',
        'saturday': '8:00 AM - 6:00 PM',
        'sunday': '9:00 AM - 4:00 PM'
    }
}

services = [
    {
        'name': 'Blood Chemistry Panel',
        'description': 'Comprehensive metabolic panel including glucose, electrolytes, kidney and liver function tests.',
        'turnaround': '24 hours',
        'icon': 'fa-tint'
    },
    {
        'name': 'Hematology',
        'description': 'Complete blood count (CBC) with differential, blood smears, and coagulation studies.',
        'turnaround': '2-4 hours',
        'icon': 'fa-heartbeat'
    },
    {
        'name': 'Microbiology',
        'description': 'Bacterial cultures, sensitivity testing, and identification of infectious organisms.',
        'turnaround': '48-72 hours',
        'icon': 'fa-microscope'
    },
    {
        'name': 'Immunology & Serology',
        'description': 'Antibody testing, autoimmune markers, and infectious disease serology.',
        'turnaround': '24-48 hours',
        'icon': 'fa-shield-alt'
    },
    {
        'name': 'Molecular Diagnostics',
        'description': 'PCR testing, genetic analysis, and molecular pathogen detection.',
        'turnaround': '24-72 hours',
        'icon': 'fa-dna'
    },
    {
        'name': 'Histopathology',
        'description': 'Tissue examination, biopsy analysis, and cytological studies.',
        'turnaround': '3-5 days',
        'icon': 'fa-search'
    }
]

team_members = [
    {
        'name': 'Dr. Sarah Johnson',
        'position': 'Laboratory Director',
        'credentials': 'MD, PhD, FCAP',
        'specialization': 'Clinical Pathology',
        'image': 'team1.jpg'
    },
    {
        'name': 'Dr. Michael Chen',
        'position': 'Chief Medical Technologist',
        'credentials': 'MT(ASCP), PhD',
        'specialization': 'Molecular Diagnostics',
        'image': 'team2.jpg'
    },
    {
        'name': 'Lisa Rodriguez',
        'position': 'Quality Assurance Manager',
        'credentials': 'MT(ASCP), CQM',
        'specialization': 'Laboratory Quality Systems',
        'image': 'team3.jpg'
    },
    {
        'name': 'Dr. James Wilson',
        'position': 'Microbiology Supervisor',
        'credentials': 'PhD, SM(ASCP)',
        'specialization': 'Clinical Microbiology',
        'image': 'team4.jpg'
    }
]

@app.route('/')
def home():
    return render_template('index.html', lab_info=lab_info, services=services[:3])

@app.route('/services')
def services_page():
    return render_template('services.html', services=services, lab_info=lab_info)

@app.route('/about')
def about():
    return render_template('about.html', lab_info=lab_info, team_members=team_members)

@app.route('/contact')
def contact():
    return render_template('contact.html', lab_info=lab_info)

@app.route('/appointment', methods=['GET', 'POST'])
def appointment():
    if request.method == 'POST':
        name = request.form.get('name')
        email = request.form.get('email')
        phone = request.form.get('phone')
        test_type = request.form.get('test_type')
        preferred_date = request.form.get('preferred_date')
        message = request.form.get('message')
        
        # In a real application, you would save this to a database
        flash(f'Thank you, {name}! Your appointment request has been received. We will contact you within 24 hours to confirm your appointment.', 'success')
        return redirect(url_for('appointment'))
    
    return render_template('appointment.html', lab_info=lab_info, services=services)

@app.route('/results')
def results():
    return render_template('results.html', lab_info=lab_info)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)