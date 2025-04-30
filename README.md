# Railway Panorama Viewer

A responsive web application for viewing railway panorama images with navigation controls.



## Features

- Fullscreen panorama image viewing
- Navigation between images (Previous/Next)
- Auto-rotate mode (2-second interval)
- Loading indicator during image transitions
- Responsive design for all screen sizes
- Keyboard navigation support


Clone the repository:
   ```bash
   git clone https://github.com/Devilgaurav123/railway-panorama-viewer.git
   cd railway-panorama-viewer


Create and activate a virtual environment:

python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`


Set up your static files:

Place your panorama images in static/images/

Recommended image naming: image1.png, image2.png



Configuration
In settings.py, ensure these settings are configured:

python
STATIC_URL = '/static/'
STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
Add your app to INSTALLED_APPS in settings.py


Usage
Run the development server:

bash
python manage.py runserver
Access the viewer in your browser:


Controls
Previous: Show the previous panorama image

Next: Show the next panorama image

Start Auto-View: Begin automatic rotation (2-second interval)

Stop Auto-View: Stop automatic rotation



Keyboard Shortcuts
Left Arrow: Previous image

Right Arrow: Next image

Space: Toggle Auto-View




File Structure:

panoimage/
├── testapp/
│   ├── static/
│   │   └── images/
│   │       ├── iamge1.png
│   │       ├── image2.png
│   │       └── ... (10 images)
│   ├── templates/
│   │   └── testapp/
│   │       └── index.html
│   ├── admin.py
│   ├── apps.py
│   ├── models.py
│   ├── urls.py
│   ├── views.py
├── panoimage/
│   ├── settings.py
│   ├── urls.py
│   └── ...
└── manage.py



Troubleshooting:
  
  Images not loading:
  
  Verify images are in the correct static/images/ folder
  
  Check console for 404 errors
  
  Run python manage.py collectstatic if in production


  Auto-View not working:
  
  Ensure you have multiple images loaded
  
  Check browser console for JavaScript errors



License :

Contributions are welcome! Please open an issue or submit a pull request.










