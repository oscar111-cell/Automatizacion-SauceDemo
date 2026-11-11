# 🧪 Proyecto de Testing y Automatización – SauceDemo

## 📌 Descripción del proyecto

Este repositorio contiene el desarrollo de un proyecto de aseguramiento de calidad de software (QA), enfocado en la validación funcional y la automatización de pruebas sobre la aplicación web [SauceDemo](https://www.saucedemo.com/).

El objetivo es aplicar diferentes estrategias de testing para verificar el comportamiento de una aplicación, identificar posibles defectos y documentar los resultados obtenidos durante el proceso de pruebas.

El proyecto está organizado en tres módulos independientes que permiten abordar diferentes áreas del proceso de aseguramiento de calidad.

## 📂 Estructura del repositorio

```text
Automatizacion-SauceDemo/
│
├── modulo-api/
│   └── Pruebas relacionadas con la validación de servicios API.
│
├── modulo-automatizacion/
│   └── Pruebas automatizadas de interfaz de usuario.
│
├── modulo-funcional/
│   └── Documentación y casos de pruebas funcionales.
│
└── README.md
```

## 🧩 Módulos del proyecto

### 1. Módulo de pruebas funcionales

Contiene la documentación relacionada con el análisis y diseño de pruebas funcionales de la aplicación.

Su propósito es verificar que las funcionalidades respondan de acuerdo con los comportamientos esperados.

Actividades principales:

- Identificación de escenarios de prueba.
- Diseño de casos de prueba.
- Validaciones positivas y negativas.
- Documentación de resultados.
- Registro y seguimiento de defectos.

### 2. Módulo de pruebas API

Está destinado a la validación de los servicios y endpoints de la aplicación, permitiendo verificar el intercambio de información y las respuestas de los servicios.

Actividades principales:

- Validación de solicitudes HTTP.
- Verificación de códigos de respuesta.
- Validación de estructuras y datos recibidos.
- Comprobación de respuestas esperadas y manejo de errores.

### 3. Módulo de automatización

Contiene las pruebas automatizadas de interfaz de usuario sobre SauceDemo.

Se utiliza Python con Selenium WebDriver y Behave, aplicando el patrón Page Object Model (POM) para mantener separada la lógica de interacción con la página y la definición de los escenarios de prueba.

**Tecnologías utilizadas:**

- Python 3.9 o superior.
- Selenium WebDriver.
- Behave.
- Google Chrome.
- Page Object Model (POM).
- Gherkin para la definición de escenarios BDD.

## 🚀 Clonar el repositorio

Ejecutar los siguientes comandos desde una terminal:

```bash
git clone https://github.com/oscar111-cell/Automatizacion-SauceDemo.git
```

Ingresar al directorio:

```bash
cd Automatizacion-SauceDemo
```

## ▶️ Ejecución del módulo de automatización

Ingresar al directorio correspondiente:

```bash
cd modulo-automatizacion
```

Crear un entorno virtual:

```bash
python -m venv .venv
```

Activar el entorno virtual en Windows:

```bash
.venv\Scripts\activate
```

Instalar las dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar los escenarios automatizados:

```bash
behave
```

**Nota:** Los comandos anteriores asumen que el módulo contiene un archivo `requirements.txt` y una configuración válida de Behave. Consulta los archivos del módulo para confirmar sus dependencias y comandos disponibles.

## 🛠️ Tecnologías y herramientas

| Tecnología | Utilización |
|---|---|
| Python | Lenguaje de programación |
| Selenium WebDriver | Automatización del navegador |
| Behave | Ejecución de escenarios BDD |
| Gherkin | Descripción de escenarios de prueba |
| Page Object Model | Organización y mantenimiento del código |
| Git | Control de versiones |
| GitHub | Administración y alojamiento del repositorio |
| Postman | Validación de servicios API, cuando aplique |
