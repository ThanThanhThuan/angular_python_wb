## World Bank Development Indicators Portal
**1. Project Overview**

A full-stack web application designed to visualize, analyze, and forecast economic indicators (GDP, Literacy, etc.) using data from the World Bank. 
The system features Role-Based Access Control (RBAC), serving different interfaces to Students, Researchers, and Policymakers.
**2. Technology Stack**
Frontend (Client-Side)

    Framework: Angular 19+ (Modern "Standalone" Architecture).

    Naming Convention: Simplified (app.ts, app.html).

    Visualization: Highcharts v5.2+ (implemented via HighchartsChartComponent).

    Language: TypeScript.

    Styling: CSS/SCSS.

Backend (Server-Side)

    Framework: Django 5.x & Django REST Framework (DRF).

    Language: Python 3.10+.

    Data Analysis: Pandas & Statsmodels (for forecasting).

    Database: MySQL.

    Authentication: JWT (JSON Web Tokens) - Planned.

**Quick Start Guide for VSCode:**
cd backend
# 1. Activate Virtual Environment (Git Bash)
source venv/Scripts/activate
# OR (Command Prompt) -> venv\Scripts\activate

# 2. Run Server
python manage.py runserver

cd frontend
npm start
<img width="1887" height="1035" alt="image" src="https://github.com/user-attachments/assets/2b2b77f0-3e41-4194-9bc3-541485b30ebb" />


    
