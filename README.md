# CareerPath AI — Student & Parent MVP

CareerPath AI helps students discover education and career possibilities beyond the jobs they already know. This first implementation focuses on **students and parents** and supports profile selection for Karnataka State Board, Tamil Nadu State Board, CBSE, ICSE and IGCSE.

## Included in this milestone
- React + Vite frontend with responsive dashboard styling.
- Django REST Framework backend, JWT authentication and SQLite local development.
- Student and parent registration roles.
- Student profile fields for class, state and education board.
- Interest assessment and rule-based career recommendations.
- Interactive career-map prototype with pathways for mathematics/science, biology, commerce, humanities and vocational/skilled work.
- Career exploration catalogue and illustrative routes through degrees, diplomas, ITI and apprenticeships.
- CORS defaults for Vite ports 5173 and 5174.

## Stack
- React + Vite + React Router + Lucide icons
- Django REST Framework + JWT
- SQLite for local development (PostgreSQL can be configured later)

## Prerequisites
- Python 3.11+
- Node.js 20+
- npm

## 1. Start the backend (Windows PowerShell)
```powershell
cd backend
py -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
Copy-Item .env.example .env
python manage.py migrate
python manage.py seed_careers
python manage.py runserver
```
API: http://127.0.0.1:8000/api/  
Django admin: http://127.0.0.1:8000/admin/

## 2. Start the frontend (second terminal)
```powershell
cd frontend
npm install
Copy-Item .env.example .env
npm run dev
```
Open the URL printed by Vite (usually http://localhost:5173).

## Suggested demo flow
1. Register as a student or parent. Choose the relevant state and board.
2. For student accounts, select the current class (8–12).
3. Complete the interest assessment.
4. Open **Career map** and switch between subject/field directions.
5. Expand courses, careers and alternative entry routes; select career examples to preview the detail area.

## Important limitations
- The career map currently uses illustrative frontend sample pathways. It is not yet a complete, board-specific official pathway database and does not claim to cover every career.
- Board-specific Class 11 combinations and course eligibility must be researched and verified for the school, institution and admission year. Do not interpret the map as a guarantee of eligibility.
- Parent accounts can register and explore guidance, but secure parent-to-child linking, consent and private access to a child's assessment data are **not implemented yet**. The parent dashboard explicitly avoids exposing student data until linking is built.
- Assessment matching is an exploration aid, not a validated psychometric test or prediction of success.
- Do not enter real children's personal data until guardian consent, retention/deletion controls, access controls and privacy/legal review are implemented.
- Before production, add saved assessment attempts, versioned assessment questions, verified content with official sources and last-verified dates, audit logging, object-level permission tests, and secure parent-child linking.

## Next implementation milestones
1. Parent-child invitation/linking flow with guardian consent and access-control tests.
2. Structured database models for boards, subject combinations, courses, careers, specialisations, entry routes, sources and validity dates.
3. Board-aware assessment results and a mind map generated from that pathway database.
4. Save and compare pathways; build a roadmap with eligibility and official-source citations.
5. Expand occupation and industry coverage with a review workflow and versioned data.
