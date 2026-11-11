# MakersPay: Escenarios Gherkin

Escenarios de prueba en lenguaje Gherkin para los tres flujos del producto: inicio de sesión, consulta de saldo y envío de dinero.

## Supuestos (a confirmar con el Product Owner)

- El inicio de sesión se hace con número de celular y contraseña.
- La cuenta se bloquea temporalmente tras 3 intentos fallidos.
- Los montos son en pesos enteros (sin decimales).
- Los límites de monto ($5.000 y $2.000.000) son inclusivos.
- El celular tiene 10 dígitos.

## Contenido

1. [Feature 1: Iniciar sesión](#feature-1-iniciar-sesión)
2. [Feature 2: Ver saldo](#feature-2-ver-saldo)
3. [Feature 3: Enviar dinero](#feature-3-enviar-dinero)

## Etiquetas utilizadas

| Etiqueta | Significado |
|---|---|
| `@humo` | Prueba de humo, se ejecuta tras cada despliegue |
| `@positivo` / `@negativo` | Flujo feliz / flujo de error |
| `@validacion` | Validación de datos de entrada |
| `@limites` | Análisis de valores límite |
| `@seguridad` | Pruebas de seguridad |
| `@integracion` | Consistencia entre módulos (saldo, historial) |
| `@concurrencia` | Operaciones simultáneas o repetidas |
| `@integridad` | Atomicidad de la transacción |

---

## Feature 1: Iniciar sesión

```gherkin
# language: es
@login
Característica: Inicio de sesión en MakersPay
  Como usuario registrado de MakersPay
  Quiero iniciar sesión con mi celular y contraseña
  Para acceder a mi billetera digital

  Antecedentes:
    Dado que el usuario "3001234567" está registrado con la contraseña "Maker$2024"
    Y se encuentra en la pantalla de inicio de sesión

  @humo @positivo
  Escenario: Inicio de sesión exitoso con credenciales válidas
    Cuando ingresa el celular "3001234567" y la contraseña "Maker$2024"
    Y presiona el botón "Iniciar sesión"
    Entonces accede a la pantalla principal de su billetera
    Y visualiza su saldo disponible

  @negativo
  Escenario: Inicio de sesión con contraseña incorrecta
    Cuando ingresa el celular "3001234567" y la contraseña "ClaveErrada1"
    Y presiona el botón "Iniciar sesión"
    Entonces el sistema muestra el mensaje "Celular o contraseña incorrectos"
    Y permanece en la pantalla de inicio de sesión

  @negativo
  Escenario: Inicio de sesión con un celular no registrado
    Cuando ingresa el celular "3205550000" y la contraseña "Maker$2024"
    Y presiona el botón "Iniciar sesión"
    Entonces el sistema muestra el mensaje "Celular o contraseña incorrectos"

  @negativo @validacion
  Escenario: Inicio de sesión con campos vacíos
    Cuando deja vacíos el celular y la contraseña
    Y presiona el botón "Iniciar sesión"
    Entonces el sistema indica que ambos campos son obligatorios

  @negativo @validacion
  Esquema del escenario: Inicio de sesión con formato de celular inválido
    Cuando ingresa el celular "<celular>" y la contraseña "Maker$2024"
    Y presiona el botón "Iniciar sesión"
    Entonces el sistema muestra el mensaje "<mensaje>"

    Ejemplos:
      | celular     | mensaje                          |
      | 300123456   | El celular debe tener 10 dígitos |
      | 30012345678 | El celular debe tener 10 dígitos |
      | 300abc4567  | El celular solo admite números   |

  @seguridad
  Escenario: Bloqueo de la cuenta tras tres intentos fallidos
    Cuando intenta iniciar sesión 3 veces con la contraseña "ClaveErrada1"
    Entonces el sistema bloquea temporalmente la cuenta
    Y muestra el mensaje "Cuenta bloqueada por intentos fallidos"
    Y no permite el acceso ni siquiera con la contraseña correcta

  @seguridad
  Escenario: Acceso a una pantalla protegida sin sesión iniciada
    Dado que el usuario no ha iniciado sesión
    Cuando intenta abrir directamente la URL de "Enviar dinero"
    Entonces el sistema lo redirige a la pantalla de inicio de sesión

  @seguridad
  Escenario: Cierre de sesión
    Dado que el usuario inició sesión correctamente
    Cuando selecciona la opción "Cerrar sesión"
    Entonces vuelve a la pantalla de inicio de sesión
    Y no puede regresar a la billetera con el botón "Atrás" del navegador
```

---

## Feature 2: Ver saldo

```gherkin
# language: es
@saldo
Característica: Consulta de saldo
  Como usuario autenticado
  Quiero ver mi saldo disponible
  Para saber cuánto dinero puedo usar

  Antecedentes:
    Dado que el usuario "3001234567" inició sesión
    Y su saldo es de $500.000 COP

  @humo @positivo
  Escenario: Visualización del saldo al ingresar a la billetera
    Cuando accede a la pantalla principal
    Entonces visualiza el saldo "$500.000"
    Y el valor se muestra en pesos colombianos con separador de miles

  @positivo
  Escenario: Saldo en cero
    Dado que el saldo del usuario es $0
    Cuando accede a la pantalla principal
    Entonces visualiza el saldo "$0"

  @integracion
  Escenario: Actualización del saldo después de enviar dinero
    Cuando envía $50.000 al celular "3109876543"
    Y vuelve a la pantalla principal
    Entonces visualiza el saldo "$450.000"

  @integracion
  Escenario: Actualización del saldo después de recibir dinero
    Cuando el usuario "3109876543" le envía $30.000
    Y consulta su saldo
    Entonces visualiza el saldo "$530.000"

  @seguridad
  Escenario: Un usuario solo puede ver su propio saldo
    Cuando intenta consultar el saldo de otro usuario modificando el identificador en la petición
    Entonces el sistema rechaza la solicitud con acceso denegado

  @seguridad
  Escenario: Consulta de saldo sin sesión activa
    Dado que la sesión del usuario expiró
    Cuando intenta consultar su saldo
    Entonces el sistema lo redirige al inicio de sesión
```

---

## Feature 3: Enviar dinero

```gherkin
# language: es
@envio
Característica: Envío de dinero por número de celular
  Como usuario autenticado de MakersPay
  Quiero enviar dinero a otro usuario usando su celular
  Para realizar transferencias de forma rápida

  Antecedentes:
    Dado que el usuario A con celular "3001234567" inició sesión
    Y el usuario A tiene un saldo de $500.000
    Y el usuario B con celular "3109876543" está registrado con un saldo de $100.000
    Y el usuario A se encuentra en la pantalla "Enviar dinero"

  @humo @positivo
  Escenario: Envío exitoso con datos válidos
    Cuando ingresa el celular "3109876543" y el monto "50000"
    Y confirma el envío
    Entonces el sistema muestra la confirmación de la transacción exitosa
    Y el saldo del usuario A es $450.000
    Y el saldo del usuario B es $150.000
    Y el movimiento aparece en el historial de ambos usuarios

  @limites
  Esquema del escenario: Validación de montos mínimo y máximo
    Dado que el usuario A tiene un saldo de $2.500.000
    Cuando ingresa el celular "3109876543" y el monto "<monto>"
    Y confirma el envío
    Entonces el resultado es "<resultado>"
    Y el sistema muestra "<mensaje>"

    Ejemplos:
      | monto   | resultado | mensaje                                 |
      | 4999    | rechazado | El monto mínimo por envío es $5.000     |
      | 5000    | exitoso   | Envío realizado con éxito               |
      | 5001    | exitoso   | Envío realizado con éxito               |
      | 1999999 | exitoso   | Envío realizado con éxito               |
      | 2000000 | exitoso   | Envío realizado con éxito               |
      | 2000001 | rechazado | El monto máximo por envío es $2.000.000 |

  @saldo
  Escenario: Envío con saldo insuficiente
    Cuando ingresa el celular "3109876543" y el monto "500001"
    Y confirma el envío
    Entonces el sistema muestra el mensaje "Saldo insuficiente"
    Y el saldo del usuario A sigue siendo $500.000
    Y no se registra ningún movimiento en el historial

  @saldo @limites
  Escenario: Envío por el valor exacto del saldo disponible
    Dado que el usuario A tiene un saldo de $300.000
    Cuando ingresa el celular "3109876543" y el monto "300000"
    Y confirma el envío
    Entonces la transacción es exitosa
    Y el saldo del usuario A es $0

  @negativo
  Escenario: Envío al propio número de celular
    Cuando ingresa el celular "3001234567" y el monto "20000"
    Y confirma el envío
    Entonces el sistema muestra el mensaje "No puedes enviarte dinero a ti mismo"
    Y el saldo del usuario A no cambia

  @negativo @seguridad
  Escenario: Envío al propio número usando el prefijo +57
    Cuando ingresa el celular "+573001234567" y el monto "10000"
    Y confirma el envío
    Entonces el sistema rechaza la operación por ser el mismo número del remitente

  @negativo
  Escenario: Envío a un número no registrado
    Cuando ingresa el celular "3205550000" y el monto "20000"
    Y confirma el envío
    Entonces el sistema muestra el mensaje "El número ingresado no está registrado en MakersPay"
    Y el saldo del usuario A no cambia

  @negativo @validacion
  Esquema del escenario: Validación del formato del celular destinatario
    Cuando ingresa el celular "<celular>" y el monto "10000"
    Y confirma el envío
    Entonces el sistema muestra el mensaje "<mensaje>"

    Ejemplos:
      | celular      | mensaje                              |
      |              | El celular es obligatorio            |
      | 310987654    | El celular debe tener 10 dígitos     |
      | 31098765432  | El celular debe tener 10 dígitos     |
      | 310abc6543   | El celular solo admite números       |
      | 310 987 6543 | El celular no debe contener espacios |

  @negativo @validacion
  Esquema del escenario: Validación de datos inválidos en el monto
    Cuando ingresa el celular "3109876543" y el monto "<monto>"
    Y confirma el envío
    Entonces el sistema muestra un mensaje de validación
    Y el saldo del usuario A no cambia

    Ejemplos:
      | monto   |
      |         |
      | 0       |
      | -10000  |
      | abc     |
      | 5000.50 |
      | 1e5     |

  @integracion
  Escenario: Registro del movimiento en el historial de ambos usuarios
    Cuando el usuario A envía $50.000 al celular "3109876543"
    Entonces el historial del usuario A muestra un movimiento de salida de $50.000 hacia "3109876543"
    Y el historial del usuario B muestra un movimiento de entrada de $50.000 desde "3001234567"
    Y ambos movimientos incluyen fecha y hora

  @integridad
  Escenario: Falla de conexión durante la confirmación del envío
    Cuando ingresa el celular "3109876543" y el monto "50000"
    Y la conexión se pierde al confirmar el envío
    Entonces la transacción se completa en ambos lados o no se aplica en ninguno
    Y los saldos de A y B son consistentes

  @concurrencia
  Escenario: Doble clic en el botón Enviar
    Cuando ingresa el celular "3109876543" y el monto "10000"
    Y hace doble clic rápido en "Enviar"
    Entonces se procesa una sola transacción
    Y el saldo del usuario A es $490.000

  @concurrencia
  Escenario: Dos envíos simultáneos que superan el saldo
    Dado que el usuario A tiene un saldo de $100.000
    Cuando realiza dos envíos de $80.000 al mismo tiempo desde dos dispositivos
    Entonces solo uno de los envíos es exitoso
    Y el otro es rechazado por saldo insuficiente
    Y el saldo del usuario A nunca es negativo

  @seguridad
  Escenario: Manipulación del monto en la petición
    Cuando modifica el monto de la petición a "3000000" usando las herramientas del navegador
    Entonces el servidor rechaza la operación
    Y el saldo no cambia

  @seguridad
  Escenario: Sesión expirada antes de confirmar el envío
    Dado que la sesión del usuario A expira mientras diligencia el formulario
    Cuando confirma el envío
    Entonces el sistema lo redirige al inicio de sesión
    Y la transacción no se ejecuta
```
