# aviationstack-api-tests
Automated API testing with Python - target API (aviationstack)
[https://aviationstack.com/?utm_source=Github&utm_medium=Referral&utm_campaign=Public-apis-repo-Best-sellers]

## How to run locally (will be updated)
1. Clone repository
2. Create virtualenv (`python -m venv .venv`) and activate venv
3. Install dependencies (`pip install -r requirements.txt`)
4. Get free API key (https://aviationstack.com/signup/free)
5. Copy `.env.example` -> `.env` and set `AVIATIONSTACK_ACCESS_KEY`
6. Run: `pytest -m api`