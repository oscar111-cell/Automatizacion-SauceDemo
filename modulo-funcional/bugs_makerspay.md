# Reporte de Bugs: MakersPay

**Requerimiento:** Un usuario autenticado puede enviar dinero a otro usuario registrado usando su número de celular.

## Datos de prueba (ficticios)

- **Ambiente:** QA, web en Chrome 130 y app Android 14
- **Usuario A (emisor):** celular 911111111, saldo inicial $100.000
- **Usuario B (receptor):** celular 922222222, saldo inicial $50.000

## Resumen

| ID | Título | Severidad | Prioridad | Técnica de prueba |
|---|---|---|---|---|
| BUG-001 | Permite enviar un monto mayor al saldo disponible | Crítica | Alta | Valores límite |
| BUG-002 | Envío a un número no registrado se muestra exitoso y descuenta saldo | Crítica | Alta | Partición de equivalencia |
| BUG-003 | Se puede enviar dinero con la sesión expirada | Crítica | Alta | Prueba de seguridad |
| BUG-004 | Doble clic en "Enviar" duplica la transferencia | Alta | Alta | Prueba exploratoria |

---

# Bug Report – ID 001

**Título:** Permite enviar un monto mayor al saldo disponible

**Descripción:** El sistema permite enviar un monto mayor al saldo disponible del emisor, lo que deja el saldo en negativo.

**Severidad:** Crítica  
**Prioridad:** Alta  
**Estado:** Abierto

## Entorno

- QA, web en Chrome 130 y app Android 14

## Precondiciones:

1. Usuario A (emisor) autenticado, celular 911111111, saldo $100.000
2. Usuario B (receptor) registrado con celular 922222222

## Pasos:

1. Ir a "Enviar dinero"
2. Ingresar celular "922222222"
3. Ingresar monto "$100.001"
4. Presionar "Enviar"

## Resultado esperado:

- Se bloquea el envío con el mensaje "Saldo insuficiente"
- El saldo no cambia

## Resultado actual:

- La transferencia se procesa
- El saldo del emisor queda en -$1

## Evidencia

Captura de pantalla/console log

## Notas:

- **Módulo:** Enviar dinero
- **Tipo de prueba:** Funcional (negativa)
- **Técnica:** Análisis de valores límite
- **Regla de negocio:** El monto a enviar no puede superar el saldo disponible

---

# Bug Report – ID 002

**Título:** Envío a un número no registrado se muestra exitoso y descuenta saldo

**Descripción:** El sistema muestra como exitosa una transferencia a un número que no está registrado en MakersPay y descuenta el saldo del emisor, aunque el dinero no llega a ninguna cuenta.

**Severidad:** Crítica  
**Prioridad:** Alta  
**Estado:** Abierto

## Entorno

- QA, web en Chrome 130 y app Android 14

## Precondiciones:

1. Usuario A (emisor) autenticado, celular 911111111, saldo $100.000
2. El celular 933333333 no está registrado en MakersPay

## Pasos:

1. Ir a "Enviar dinero"
2. Ingresar celular "933333333"
3. Ingresar monto "$10.000"
4. Presionar "Enviar"

## Resultado esperado:

- Aparece el mensaje "El número no está registrado en MakersPay"
- No se descuenta saldo

## Resultado actual:

- Aparece el mensaje "Transferencia exitosa"
- El saldo del emisor baja a $90.000
- El dinero no llega a ninguna cuenta

## Evidencia

Captura de pantalla/console log

## Notas:

- **Módulo:** Enviar dinero
- **Tipo de prueba:** Funcional
- **Técnica:** Partición de equivalencia
- **Regla de negocio:** Solo se puede enviar dinero a usuarios registrados

---

# Bug Report – ID 003

**Título:** Se puede enviar dinero con la sesión expirada

**Descripción:** El sistema procesa una transferencia después de que la sesión del usuario expiró, porque el backend no valida el token vencido.

**Severidad:** Crítica  
**Prioridad:** Alta  
**Estado:** Abierto

## Entorno

- QA, web en Chrome 130 y app Android 14

## Precondiciones:

1. Usuario A (emisor) autenticado, celular 911111111
2. Usuario B (receptor) registrado con celular 922222222
3. El tiempo de expiración de la sesión está configurado en 5 minutos

## Pasos:

1. Ir a "Enviar dinero"
2. Ingresar celular "922222222" y monto "$5.000"
3. Esperar 6 minutos sin interactuar
4. Presionar "Enviar"

## Resultado esperado:

- Se redirige al login con el mensaje "Tu sesión expiró"
- La transferencia no se procesa

## Resultado actual:

- La transferencia se procesa con éxito
- El backend no valida el token vencido

## Evidencia

Captura de pantalla/console log

## Notas:

- **Módulo:** Enviar dinero / Autenticación
- **Tipo de prueba:** Seguridad (no funcional)
- **Técnica:** Transición de estados
- **Regla de negocio:** Solo un usuario autenticado puede enviar dinero

---

# Bug Report – ID 004

**Título:** Doble clic en "Enviar" duplica la transferencia

**Descripción:** Al hacer doble clic rápido en el botón "Enviar", el sistema crea dos transferencias iguales y descuenta el monto dos veces.

**Severidad:** Alta  
**Prioridad:** Alta  
**Estado:** Abierto

## Entorno

- QA, web en Chrome 130 y app Android 14

## Precondiciones:

1. Usuario A (emisor) autenticado, celular 911111111, saldo $100.000
2. Usuario B (receptor) registrado con celular 922222222

## Pasos:

1. Ir a "Enviar dinero"
2. Ingresar celular "922222222" y monto "$10.000"
3. Hacer doble clic rápido en "Enviar"

## Resultado esperado:

- Se procesa una sola transferencia
- El botón se deshabilita después del primer clic

## Resultado actual:

- Se crean dos transferencias de $10.000
- El saldo del emisor queda en $80.000

## Evidencia

Captura de pantalla/console log

## Notas:

- **Módulo:** Enviar dinero
- **Tipo de prueba:** Funcional
- **Técnica:** Prueba exploratoria
- **Regla de negocio:** Cada confirmación de envío debe generar una sola transferencia
