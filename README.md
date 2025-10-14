🧠 Sistema Experto de Soporte Técnico (Data Science & IA)
Este proyecto implementa un Sistema Experto basado en reglas para diagnosticar problemas de software, drivers y sistema operativo. Incluye un desafío superador: la implementación de un Módulo de Patrones (IA) que aprende de las fallas del usuario para mejorar los diagnósticos futuros.

⚙️ Arquitectura del Proyecto
El proyecto sigue una arquitectura modular y utiliza un stack moderno:

Frontend: index.html (HTML + JavaScript + Tailwind CSS)

Una interfaz de asistente guiado, estable y con estética Dark Mode.

Backend: main.py (FastAPI)

Sirve los endpoints para el diagnóstico y registra el feedback del usuario.

Motor Experto: experto_soporte/engine.py

Contiene la base de conocimientos (Hechos y Reglas SI... ENTONCES...) con lógica priorizada.

✨ Desafío Superador (Módulo de Patrones)
El archivo main.py implementa la función buscar_patrones para gestionar el historial de sesiones.

¿Cómo funciona?

Si un usuario reporta un conjunto de síntomas y la solución sugerida falla (el usuario hace clic en "NO, Falló") dos o más veces, el sistema interpreta que la solución superficial no es suficiente.

En el siguiente intento, el sistema experto genera una ALERTA DE PATRÓN (IA) en la interfaz, sugiriendo una acción más drástica (ej., restauración de sistema) en lugar de un simple reinicio.

🚀 Cómo Ejecutar el Proyecto
1. Configuración del Entorno Python
# 1. Crear y activar entorno virtual (venv)
python -m venv venv
# Windows: .\venv\Scripts\activate
# Linux/Mac: source venv/bin/activate

# 2. Instalar dependencias
pip install -r requirements.txt

2. Iniciar el Servidor FastAPI
Asegúrate de estar en la carpeta raíz y ejecuta:

uvicorn main:app --reload

3. Acceder al Frontend
Mientras el servidor esté corriendo, abre el archivo index.html directamente en tu navegador.