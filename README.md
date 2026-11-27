# Agrivision

A smart agriculture management and AI advisory web platform built with **Flask**, **MySQL**, and **Google Gemini AI**. Agrivision connects farmers, agricultural branches (Krishi Bhavans), and administrators in one portal for crop booking, subsidy management, disease detection, and farming guidance.

## Features

- **Farmer Portal**
  - Leaf disease detection from uploaded plant images powered by Google Gemini (`gemini-2.5-flash`)
  - AI Crop Advisor (crop recommendations, expected yield, fertilizers, and cost estimates)
  - AI Farming Guide with step-by-step cultivation instructions
  - Farm registration, crop booking, subsidy requests, branch search, and query/feedback submission
  - Live global & branch-specific alerts and market price updates
- **Branch Portal**
  - Manage farmer registrations and approve/reject farm applications
  - Review and approve/reject crop bookings (with stock deduction) and subsidy requests
  - Answer farmer queries and broadcast local branch alerts
- **Admin Portal**
  - Manage agricultural branches across districts, crops, fertilizers, and subsidy programs
  - View disease prediction analytics and generate/export CSV platform reports
  - Broadcast global weather/agricultural alerts and market prices

## Tech Stack

- **Backend:** Python, Flask
- **Database:** MySQL (`mysql-connector-python`)
- **AI Integration:** Google Gemini API (`gemini-2.5-flash`)
- **Frontend:** HTML, CSS, JavaScript (Jinja2 templates)

## Setup & Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/shonesiby/agrivision.git
   cd agrivision
   ```

2. **Create a virtual environment & install dependencies**
   ```bash
   python -m venv .venv
   # On Windows:
   .venv\Scripts\activate
   # On macOS/Linux:
   source .venv/bin/activate

   pip install -r requirements.txt
   ```

3. **Set up the MySQL database**
   - Import `database/database.sql` into your MySQL server:
     ```bash
     mysql -u root -p < database/database.sql
     ```

4. **Configure environment variables**
   - Copy `.env.example` to `.env`:
     ```bash
     copy .env.example .env   # Windows
     # cp .env.example .env   # macOS/Linux
     ```
   - Fill in your local MySQL credentials, Flask secret key, and Google Gemini API key in `.env`.

5. **Run the application**
   ```bash
   python Home.py
   ```
   Open `http://127.0.0.1:5000` in your browser.

## Default Demo Accounts (`database/database.sql`)

- **Admin:** `admin` / `admin`
- **Branch:** `Krishi` / `branch123`
- **Farmer:** `farmer1` / `demo1234`
