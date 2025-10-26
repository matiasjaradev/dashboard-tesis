
dash-dashboard/
├─ app/                         # paquete principal
│  ├─ __init__.py               # crea Dash(), expone server
│  ├─ layout.py                 # layout base (navbar, container)
│  ├─ callbacks/                # callbacks separados por tema
│  │  ├─ __init__.py
│  │  ├─ charts.py
│  │  └─ filters.py
│  ├─ components/               # componentes reutilizables (cards, tablas)
│  │  ├─ __init__.py
│  │  └─ kpi_card.py
│  ├─ pages/                    # multipage con dash.pages
│  │  ├─ __init__.py
│  │  ├─ home.py
│  │  └─ analytics.py
│  ├─ services/                 # acceso a datos/APIs, caché
│  │  ├─ __init__.py
│  │  └─ datasource.py
│  ├─ config.py                 # variables de entorno (BASE_PATH, DEBUG, etc.)
│  └─ wsgi.py                   # punto de entrada para gunicorn/IIS/uwsgi
├─ assets/                      # CSS/JS/imágenes (auto-servido por Dash)
│  ├─ styles.css
│  └─ favicon.ico
├─ data/                        # CSV, parquet, o cachés locales (si aplica)
├─ tests/                       # (opcional) pruebas
├─ app.py                       # entrada para desarrollo (python app.py)
├─ requirements.txt
├─ Procfile                     # (PaaS) web: gunicorn app.wsgi:server
├─ Dockerfile                   # (si usas Docker)
├─ .env                         # PORT, DASH_BASE_PATH, SECRET (no subir al repo)
└─ README.md


## NOTE: Install requirements.txt 
**bash**

`
pip install -r requirements.txt
`

