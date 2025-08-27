# Spinfood Landing Page

A modern, conversion-focused landing page for Spinfood Running Dinner Events built with FastHTML and inspired by MonsterUI design principles.

## Features

- **Responsive Design**: Mobile-first approach with full responsiveness
- **Brand Colors**: Uses Spinfood's signature pink (#E91E63) and teal (#00BFA5) colors
- **Conversion Optimized**: Clear CTAs, progressive disclosure, and trust signals
- **Modern Animations**: Smooth scrolling, fade-in effects, and hover animations
- **Complete Sections**:
  - Hero with "Food. Fun. Friends." tagline
  - Problem-Solution flow
  - 3-step process visualization
  - Benefits cards
  - Events listing for German university cities
  - Testimonials
  - FAQ section with collapsibles
  - Team section
  - Footer with links

## Installation

### Option 1: Using Conda (Recommended)

1. Install Anaconda or Miniconda if not already installed:
   - Download from: https://www.anaconda.com/products/distribution
   - Or Miniconda: https://docs.conda.io/en/latest/miniconda.html

2. Create the conda environment:
```bash
conda env create -f environment_dev.yml
```

3. Activate the environment:
```bash
conda activate landingpage_spinfood
```

4. The environment includes all necessary packages (FastHTML, uvicorn, etc.)

### Option 2: Using pip

1. Install Python 3.7+ if not already installed

2. Install pip if not available:
```bash
# On Ubuntu/Debian
sudo apt-get update
sudo apt-get install python3-pip

# On macOS
python3 -m ensurepip --upgrade

# On Windows
python -m ensurepip --upgrade
```

3. Install dependencies:
```bash
pip install -r requirements.txt
# or
python3 -m pip install -r requirements.txt
```

## Running the Application

### With Conda Environment:
```bash
# Make sure the environment is activated
conda activate landingpage_spinfood

# Run the application
python app.py
```

### Without Conda:
```bash
python3 app.py
```

Then open your browser and navigate to:
```
http://localhost:8000
```

## Project Structure

```
website-landing/
├── app.py              # Main FastHTML application
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## Technologies Used

- **FastHTML**: Python web framework for building modern web apps
- **Uvicorn**: ASGI server for running the application
- **Font Awesome**: Icons throughout the site
- **Pure CSS**: Custom styling with CSS variables for theming

## Customization

### Colors
Edit the CSS variables in `app.py` to change the color scheme:
```css
--primary-pink: #E91E63;
--primary-green: #00BFA5;
```

### Content
Update the following data structures in `app.py`:
- `events`: List of upcoming Running Dinner events
- `testimonials`: Customer testimonials
- `faqs`: Frequently asked questions

## Deployment

For production deployment:

1. Use a production ASGI server:
```bash
uvicorn app:app --host 0.0.0.0 --port 8000 --workers 4
```

2. Consider using a reverse proxy (nginx/Apache) for better performance

3. Enable HTTPS with SSL certificates

## License

Created for Spinfood - Running Dinner Events

## Support

For questions or issues, contact: hello@spinfood.de