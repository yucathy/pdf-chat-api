#!/bin/bash

curl -X POST http://localhost:8000/ask \
  -H "Content-Type: application/json" \
  -d '{
        "question": "what kind of way they use to speed up the investigation?",
        "pdf_path": "app/can_ai_solve_crime.pdf"
      }'