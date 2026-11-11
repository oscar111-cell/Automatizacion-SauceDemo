# Automatizacion-SauceDemo
Desarrollo del modulo de automatizacion.
# Automatizacion-SauceDemo

## Descripción

Proyecto de automatización de pruebas funcionales para el sitio web [SauceDemo](https://www.saucedemo.com/).

Se implementa un **Smoke Test del proceso de inicio de sesión (Login)** utilizando Python, Selenium y Behave, aplicando el patrón de diseño **Page Object Model (POM)** para organizar y mantener el código de automatización.

El objetivo es validar los escenarios principales de autenticación y demostrar conocimientos en automatización de pruebas, desarrollo de scripts y diseño de frameworks de testing.

## Tecnologías y versiones

| Tecnología | Versión / Uso |
|---|---|
| Python | 3.14.0 |
| Behave | 1.3.3 |
| Selenium | Versión definida en `requirements.txt` |
| WebDriver Manager | Versión definida en `requirements.txt` |
| Google Chrome | Navegador para ejecución de pruebas |
| Visual Studio Code | Entorno de desarrollo |
| Git y GitHub | Control de versiones y repositorio |

**Nota:** Las versiones de Selenium y WebDriver Manager deben coincidir con las registradas en el archivo `requirements.txt`.

## Estructura del proyecto

```text
Automatizacion-SauceDemo/
│
├── modulo-automatizacion/
│   ├── features/
│   │   ├── steps/
│   │   │   └── login_steps.py
│   │   │
│   │   ├── environment.py
│   │   └── login.feature
│   │
│   ├── pages/
│   │   ├── login_page.py
│   │   └── inventory_page.py
│   │
│   └── requirements.txt
│
├── behave.ini
├── requirements.txt
└── README.md
```

## Instalación y configuración

### 1. Clonar el repositorio

```powershell
git clone https://github.com/oscar111-cell/Automatizacion-SauceDemo.git
```

Ingresar a la carpeta del proyecto:

```powershell
cd Automatizacion-SauceDemo
```

### 2. Crear el entorno virtual

```powershell
python -m venv .venv
```

### 3. Instalar las dependencias

Desde la raíz del proyecto:

```powershell
pip install -r requirements.txt
```

### 4. Verificar las versiones instaladas

```powershell
python --version
python -m behave --version
pip show selenium
pip show webdriver-manager
```

Versiones verificadas durante el desarrollo:

- Python: 3.14.0
- Behave: 1.3.3

## Configuración de Behave

El archivo `behave.ini` permite establecer la configuración de ejecución del framework.

Configuración esperada desde la raíz del repositorio:

```ini
[behave]
paths = modulo-automatizacion/features
stdout_capture = no
stderr_capture = no
log_capture = no
language = en
```

**Importante:** El nombre de la carpeta debe coincidir exactamente con el nombre real del directorio del proyecto.

## Ejecución de las pruebas

Activa primero el entorno virtual y, desde la raíz del repositorio, ingresa al módulo de automatización:

```powershell
cd .\modulo-automatizacion
```

Ejecuta los escenarios con:

```powershell
python -m behave -f pretty
```

Behave identificará los archivos `.feature`, cargará los pasos definidos en `steps` y ejecutará las pruebas automatizadas.

Para ejecutar un escenario específico:

```powershell
python -m behave features/login.feature
```

## Escenarios de prueba implementados

El proyecto contempla los siguientes escenarios para validar el proceso de autenticación:

1. **Login exitoso:** verifica el acceso al sistema utilizando credenciales válidas.
2. **Login fallido:** comprueba que el sistema rechace el acceso cuando se proporciona una contraseña incorrecta.
3. **Validación de campos obligatorios:** verifica el comportamiento del formulario cuando el usuario y/o la contraseña están vacíos.

## Patrón de diseño POM

Se implementa el patrón **Page Object Model (POM)** para separar la lógica de interacción con la interfaz web de los pasos de prueba.

- `login_page.py`: contiene los elementos y métodos relacionados con el formulario de inicio de sesión.
- `inventory_page.py`: contiene los elementos y métodos asociados a la página de inventario.
- `login_steps.py`: define las acciones y validaciones de los escenarios Behave.
- `login.feature`: describe los escenarios de prueba utilizando lenguaje Gherkin.
- `environment.py`: administra la configuración y el ciclo de vida del navegador.

Esta organización facilita el mantenimiento, la reutilización de código y la escalabilidad del proyecto.

## Gestión del navegador

El proyecto utiliza Selenium WebDriver para interactuar con Google Chrome.

La gestión automática del controlador del navegador se realiza mediante `webdriver-manager`, de acuerdo con la configuración implementada en el proyecto.

Para ejecutar las pruebas en modo headless, se puede habilitar la siguiente opción en la configuración de Chrome dentro de `environment.py`:

```python
options.add_argument("--headless=new")
```

Esto permite ejecutar las pruebas sin mostrar la ventana del navegador.

**Tecnologías principales:** Python | Selenium | Behave | Gherkin | POM | Git | GitHub
