# FastAPI_Userguide
# створити та активувати віртуальне середовище
python -m venv .venv
# Windows
.venv\Scripts\Activate.ps1
# macOS/Linux
# source .venv/bin/activate

# встановити залежності
pip install -r requirements.txt
# або (якщо без файлу):
# pip install fastapi==0.115.* uvicorn==0.30.*
uvicorn app.main:app --reload
app/
  __init__.py
  main.py
  first_steps.py
  path_params.py
  query_params.py
  request_body.py
  query_string_validations.py
  path_numeric_validations.py
  query_param_models.py
  body_multiple_params.py
  body_fields.py
  body_nested_models.py
  request_examples.py
  extra_types.py
requirements.txt
.gitignore
README.md
{ "name": "A", "price": 3.5, "is_offer": true }
{
  "user":  { "username": "lisa", "full_name": "Lisa K" },
  "item":  { "name": "Book", "price": 9.99 },
  "notify": true
}
{ "name": "Keyboard", "price": 49.9, "tags": ["usb", "silent"] }
{
  "name": "Alice",
  "address": { "city": "Seoul", "street": "Main 1", "zip_code": "04511" }
}
{
  "created_at": "2025-01-01T12:00:00",
  "author_email": "user@example.com",
  "source_url": "https://example.com",
  "uid": "550e8400-e29b-41d4-a716-446655440000"
}
curl http://127.0.0.1:8000/first-steps/hello
curl http://127.0.0.1:8000/path-params/items/7
curl -X POST http://127.0.0.1:8000/request-body/items ^
  -H "Content-Type: application/json" ^
  -d "{\"name\":\"A\",\"price\":3.5}"
git init
git add .
git commit -m "FastAPI User Guide examples: initial commit"
git branch -M main
git remote add origin https://github.com/<YOUR_USERNAME>/FastAPI_Userguide.git
git push -u origin main
.venv/
__pycache__/
*.pyc
.env
.vscode/
