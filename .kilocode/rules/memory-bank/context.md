# Active Context: SYRA Medical ID Platform

## Current State

**Project Status**: ✅ Django project created

SYRA is a hybrid medical identification platform for the Egyptian market with NFC/QR-enabled physical devices.

## Recently Completed

- [x] Created Django project structure (syra core)
- [x] Created Accounts app with SyraUser model (14-digit Egyptian National ID)
- [x] Created Profiles app with MedicalProfile, Medication, EmergencyContact, MedicalEvent models
- [x] Implemented Fernet encryption for insurance images at rest
- [x] Created emergency scan view (public UUID-based access)
- [x] Created DRF API endpoints with JWT authentication
- [x] Created template views for patient dashboard
- [x] Created UI templates for profile management

## Current Structure

| Directory | Purpose |
|-----------|---------|
| `syra/` | Django project settings, URLs, WSGI |
| `accounts/` | User authentication with Egyptian National ID |
| `profiles/` | Medical profiles, medications, contacts, events |
| `templates/` | HTML templates for web interface |

## Key Features Implemented

1. **Accounts App**: Extended Django User with 14-digit Egyptian National ID validation
2. **Profiles App**: Medical profiles with UUID for NFC/QR scanning
3. **Encryption**: Fernet encryption for insurance card images
4. **Emergency View**: Public endpoint (`/api/profiles/scan/<uuid>/`) - excludes insurance data
5. **Max 2 Contacts**: Enforced at both API and template level
6. **JWT Auth**: DRF SimpleJWT for API authentication

## API Endpoints

- `POST /api/accounts/register/` - User registration
- `POST /api/accounts/login/` - Login with National ID
- `GET /api/accounts/profile/` - Get/Update profile
- `GET /api/profiles/scan/<uuid>/` - Emergency scan (public)
- `GET/POST /api/profiles/profiles/` - Medical profile CRUD
- `GET/POST /api/profiles/medications/` - Medications CRUD
- `GET/POST /api/profiles/contacts/` - Emergency contacts CRUD
- `GET/POST /api/profiles/events/` - Medical events CRUD

## Web URLs

- `/dashboard/` - Patient dashboard
- `/profile/edit/` - Edit medical profile
- `/medications/` - Manage medications
- `/contacts/` - Manage emergency contacts (max 2)
- `/events/` - View medical history

## To Run

```bash
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

## Session History

| Date | Changes |
|------|---------|
| 2026-03-10 | Created SYRA Django project with all apps |
