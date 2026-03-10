# SYRA Medical ID Platform

A hybrid medical identification platform for the Egyptian market with NFC/QR-enabled physical devices. SYRA allows users to store their medical information securely and access it instantly in emergencies via QR codes or NFC tags.

## Features

### 👤 User Authentication
- Registration with Egyptian National ID (14-digit validation)
- Secure login with JWT authentication
- Profile management

### 🏥 Medical Profile Management
- Personal medical information storage
- Blood type, allergies, chronic conditions
- Height and weight tracking

### 💊 Medication Tracking
- Add, edit, and delete medications
- Dosage and frequency tracking
- Active/inactive status

### 👨‍👩‍👧‍👦 Emergency Contacts
- Up to 2 emergency contacts per profile
- Quick access during emergencies

### 📋 Medical History
- Track medical events (surgeries, hospitalizations)
- Date and description logging

### 🔒 Security
- Fernet encryption for sensitive data (insurance images)
- JWT-based API authentication
- UUID-based public emergency access (no authentication required for emergency scans)

### 📱 Emergency Access
- **HTML View**: `/emergency/<uuid>/` - View medical profile via QR/NFC in browser
- **API Endpoint**: `/api/profiles/scan/<uuid>/` - JSON data for scanning apps

## Tech Stack

| Technology | Purpose |
|------------|---------|
| Python 3.x | Backend language |
| Django 5.x | Web framework |
| Django REST Framework | API development |
| SimpleJWT | JWT authentication |
| Fernet | Encryption for sensitive data |
| SQLite | Database (default) |

## Project Structure

```
syra/                    # Django project settings
├── settings.py          # Main configuration
├── urls.py              # Root URL configuration
├── wsgi.py              # WSGI entry point
├── asgi.py              # ASGI entry point
accounts/                # User authentication app
├── models.py            # SyraUser model (National ID)
├── views.py             # API & template views
├── serializers.py       # DRF serializers
├── urls.py              # URL routing
profiles/                # Medical profiles app
├── models.py            # MedicalProfile, Medication, EmergencyContact, MedicalEvent
├── views.py             # API views
├── template_views.py    # HTML template views
├── serializers.py       # DRF serializers
templates/               # HTML templates
├── accounts/            # Login, Register
├── profiles/            # Dashboard, Profile, Medications, Contacts, Events, Emergency
```

## Installation

### 1. Clone the repository
```bash
git clone <repository-url>
cd <project-directory>
```

### 2. Create virtual environment (optional but recommended)
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Run migrations
```bash
python manage.py migrate
```

### 5. Start the development server
```bash
python manage.py runserver
```

## API Endpoints

### Authentication
| Method | Endpoint | Description |
|--------|----------|-------------|
| POST | `/api/accounts/register/` | Register new user |
| POST | `/api/accounts/login/` | Login with National ID |
| POST | `/api/accounts/logout/` | Logout (blacklist token) |
| GET | `/api/accounts/profile/` | Get user profile |
| PUT | `/api/accounts/profile/` | Update user profile |

### Medical Profiles
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/profiles/profiles/` | Get user's medical profile |
| POST | `/api/profiles/profiles/` | Create medical profile |
| PUT | `/api/profiles/profiles/` | Update medical profile |

### Medications
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/profiles/medications/` | List user's medications |
| POST | `/api/profiles/medications/` | Add medication |
| PUT | `/api/profiles/medications/<id>/` | Update medication |
| DELETE | `/api/profiles/medications/<id>/` | Delete medication |

### Emergency Contacts
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/profiles/contacts/` | List emergency contacts |
| POST | `/api/profiles/contacts/` | Add contact (max 2) |
| PUT | `/api/profiles/contacts/<id>/` | Update contact |
| DELETE | `/api/profiles/contacts/<id>/` | Delete contact |

### Medical Events
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/profiles/events/` | List medical events |
| POST | `/api/profiles/events/` | Add event |
| PUT | `/api/profiles/events/<id>/` | Update event |
| DELETE | `/api/profiles/events/<id>/` | Delete event |

### Emergency Scan (Public)
| Method | Endpoint | Description |
|--------|----------|-------------|
| GET | `/api/profiles/scan/<uuid>/` | Get profile data (JSON) |
| GET | `/emergency/<uuid>/` | View profile (HTML) |

## Web URLs

| Path | Description |
|------|-------------|
| `/` or `/login/` | Login page |
| `/register/` | Registration page |
| `/logout/` | Logout |
| `/dashboard/` | Patient dashboard |
| `/profile/edit/` | Edit medical profile |
| `/medications/` | Manage medications |
| `/contacts/` | Manage emergency contacts |
| `/events/` | View medical history |
| `/emergency/<uuid>/` | Public emergency scan page |

## Configuration

### Environment Variables (Optional)
Create a `.env` file in the project root:
```env
SECRET_KEY=your-secret-key
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
```

### Fernet Key for Encryption
The Fernet key is automatically generated on first run and stored in the database. For production, set a static key in settings.

## Security Notes

- Insurance card images are encrypted at rest using Fernet symmetric encryption
- Emergency scan endpoint excludes sensitive insurance data
- JWT tokens are used for API authentication
- Maximum 2 emergency contacts per profile (enforced at API and UI level)

## Usage

### Register a New User
1. Navigate to `/register/`
2. Enter Egyptian National ID (14 digits)
3. Enter password and confirm
4. Fill in personal details

### Create Medical Profile
1. After login, navigate to `/profile/edit/`
2. Fill in medical information (blood type, allergies, etc.)
3. Save profile

### Emergency Access
First responders can access medical info by:
1. Scanning QR code or tapping NFC tag
2. Visiting `/emergency/<uuid>/`
3. Using the API: `/api/profiles/scan/<uuid>/`

## License

This project is for demonstration purposes.
