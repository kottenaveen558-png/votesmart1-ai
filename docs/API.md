# Byte ninja - VoteSmart Pro

All files and folders in the VoteSmart Pro project.

## Quick Navigation

### Backend (`/backend`)
- `app/main.py` - FastAPI application entry point
- `app/config.py` - Configuration and settings
- `app/models/election.py` - Data models (Pydantic)
- `app/routes/elections.py` - API endpoints
- `app/services/election_service.py` - Business logic
- `app/services/google_service.py` - Google APIs integration
- `app/utils/security.py` - Security utilities
- `app/utils/validators.py` - Input validation
- `tests/test_elections.py` - Unit tests
- `requirements.txt` - Python dependencies

### Frontend (`/frontend`)
- `src/App.jsx` - Main React component
- `src/index.jsx` - React entry point
- `src/components/ElectionTimeline.jsx` - Timeline display
- `src/components/ProcessSteps.jsx` - Steps display
- `src/index.css` - Accessible global styles
- `public/index.html` - HTML template
- `vite.config.js` - Vite configuration
- `package.json` - NPM dependencies

### Documentation (`/docs`)
- `API.md` - API documentation

### Configuration
- `.env.example` - Environment template (both backend and frontend)
- `.gitignore` - Git ignore rules
- `README.md` - Project documentation
- `LICENSE` - MIT License

### CI/CD (`.github/workflows`)
- `tests.yml` - Automated testing
- `build.yml` - Build pipeline

## Size Optimization

- Backend directory: ~2 MB
- Frontend directory: ~500 KB
- Total repo: <10 MB (node_modules and venv excluded)
