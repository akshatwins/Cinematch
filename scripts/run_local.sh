#!/usr/bin/env bash
set -e
cd backend
python -m uvicorn app.main:app --reload
