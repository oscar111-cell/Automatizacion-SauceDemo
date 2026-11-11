# MakersPay: Casos de prueba

Casos de prueba de los módulos de inicio de sesión, consulta de saldo y envío de dinero, con la técnica de diseño y el tipo de prueba de cada uno. Los escenarios Gherkin correspondientes están en `escenarios-gherkin.md`.

## Datos de prueba

| Dato | Valor |
|---|---|
| Usuario A (remitente) | Celular `3001234567`, saldo $500.000, contraseña `Maker$2024` |
| Usuario B (destinatario) | Celular `3109876543`, saldo $100.000 |
| Número no registrado | `3205550000` |

## Contenido

1. [Módulo Login](#módulo-login)
2. [Módulo Ver saldo](#módulo-ver-saldo)
3. [Módulo Enviar dinero](#módulo-enviar-dinero)
4. [Tabla de decisión](#tabla-de-decisión-env-25)
5. [Resumen de técnicas y tipos de prueba](#resumen-de-técnicas-y-tipos-de-prueba)

---

## Módulo Login

| ID | Escenario | Datos de entrada | Resultado esperado | Técnica | Tipo de prueba | Prioridad |
|---|---|---|---|---|---|---|
| LOG-01 | Login exitoso | Celular 3001234567, clave Maker$2024 | Acceso a la billetera y se muestra el saldo | Partición de equivalencia (válida) | Humo, funcional | Alta |
| LOG-02 | Contraseña incorrecta | Celular válido, clave ClaveErrada1 | Mensaje genérico de credenciales incorrectas | Partición de equivalencia (inválida) | Funcional negativa | Alta |
| LOG-03 | Celular no registrado | Celular 3205550000, clave válida | Mensaje genérico de credenciales incorrectas | Partición de equivalencia (inválida) | Funcional negativa | Alta |
| LOG-04 | Campos vacíos | Celular y clave vacíos | Mensaje de campos obligatorios | Análisis de valores límite (vacío) | Validación | Media |
| LOG-05 | Celular de 9 dígitos | 300123456 | Mensaje de longitud inválida | Valores límite (longitud 9) | Validación | Media |
| LOG-06 | Celular de 11 dígitos | 30012345678 | Mensaje de longitud inválida | Valores límite (longitud 11) | Validación | Media |
| LOG-07 | Celular con letras | 300abc4567 | Mensaje de solo números | Partición de equivalencia | Validación | Media |
| LOG-08 | Bloqueo por intentos fallidos | 3 intentos con clave errada | Cuenta bloqueada, no permite acceso | Transición de estados (activa → bloqueada) | Seguridad | Alta |
| LOG-09 | Acceso a URL sin sesión | Abrir URL de "Enviar dinero" sin login | Redirección al login | Adivinanza de errores | Seguridad | Alta |
| LOG-10 | Cerrar sesión | Clic en "Cerrar sesión" y luego "Atrás" | No se puede volver a la billetera | Transición de estados (sesión activa → cerrada) | Seguridad, funcional | Media |
| LOG-11 | Mensaje de error genérico | Comparar el mensaje de LOG-02 y LOG-03 | Ambos mensajes son iguales (no revelan si el celular existe) | Adivinanza de errores | Seguridad | Media |
| LOG-12 | Usabilidad del formulario | Revisar etiquetas, enmascarado de la clave y uso en móvil | Clave oculta, campos claros, teclado numérico para el celular | Basada en experiencia | Usabilidad | Baja |

---

## Módulo Ver saldo

| ID | Escenario | Datos / condición | Resultado esperado | Técnica | Tipo de prueba | Prioridad |
|---|---|---|---|---|---|---|
| SAL-01 | Ver saldo al iniciar sesión | Saldo $500.000 | Se muestra "$500.000" con formato COP | Partición de equivalencia | Humo, funcional | Alta |
| SAL-02 | Saldo en cero | Saldo $0 | Se muestra "$0" | Valores límite (saldo mínimo) | Funcional | Media |
| SAL-03 | Saldo tras enviar dinero | Envío de $50.000 | El saldo baja a $450.000 | Transición de estados | Integración | Alta |
| SAL-04 | Saldo tras recibir dinero | B envía $30.000 a A | El saldo sube a $530.000 | Transición de estados | Integración | Alta |
| SAL-05 | Saldo con valor alto | Saldo $99.999.999 | El formato se muestra correcto y sin desbordar la pantalla | Valores límite | Funcional, usabilidad | Baja |
| SAL-06 | Consultar saldo de otro usuario | Cambiar el ID en la petición | Acceso denegado | Adivinanza de errores | Seguridad | Alta |
| SAL-07 | Consultar saldo con sesión expirada | Sesión vencida | Redirección al login | Partición de equivalencia | Seguridad | Alta |
| SAL-08 | Saldo en distintos dispositivos | Mismo usuario en web y móvil | El saldo es el mismo en ambos | Partición de equivalencia | Compatibilidad, regresión | Media |
| SAL-09 | Tiempo de carga del saldo | Carga de la pantalla principal | Se muestra en pocos segundos (umbral a definir) | Basada en experiencia | Rendimiento | Baja |

---

## Módulo Enviar dinero

| ID | Escenario | Datos / condición | Resultado esperado | Técnica | Tipo de prueba | Prioridad |
|---|---|---|---|---|---|---|
| ENV-01 | Envío exitoso | Celular B, monto 50.000 | Éxito. A = $450.000, B = $150.000, historial de ambos | Partición de equivalencia | Humo, funcional | Alta |
| ENV-02 | Monto bajo el mínimo | Monto 4.999 | Rechazo por monto mínimo | Valores límite | Funcional | Alta |
| ENV-03 | Monto mínimo exacto | Monto 5.000 | Éxito | Valores límite | Funcional | Alta |
| ENV-04 | Monto sobre el mínimo | Monto 5.001 | Éxito | Valores límite | Funcional | Media |
| ENV-05 | Monto bajo el máximo | Monto 1.999.999 (saldo $2.500.000) | Éxito | Valores límite | Funcional | Media |
| ENV-06 | Monto máximo exacto | Monto 2.000.000 (saldo $2.500.000) | Éxito | Valores límite | Funcional | Alta |
| ENV-07 | Monto sobre el máximo | Monto 2.000.001 (saldo $2.500.000) | Rechazo por monto máximo | Valores límite | Funcional | Alta |
| ENV-08 | Saldo insuficiente | Saldo $500.000, monto 500.001 | Rechazo, saldo intacto | Valores límite | Funcional | Alta |
| ENV-09 | Envío por el saldo exacto | Saldo $300.000, monto 300.000 | Éxito, saldo de A en $0 | Valores límite | Funcional | Alta |
| ENV-10 | Envío al propio número | Celular 3001234567 | Rechazo con mensaje claro | Partición de equivalencia | Funcional negativa | Alta |
| ENV-11 | Propio número con +57 | +573001234567 | Rechazo por ser el mismo número | Adivinanza de errores | Funcional, seguridad | Alta |
| ENV-12 | Número no registrado | 3205550000 | Mensaje "número no registrado", saldo intacto | Partición de equivalencia | Funcional negativa | Alta |
| ENV-13 | Celular con formato inválido | 9 dígitos, 11 dígitos, letras, espacios | Mensaje de validación | Partición y valores límite | Validación | Media |
| ENV-14 | Celular vacío | Campo sin datos | Mensaje de campo obligatorio | Partición de equivalencia | Validación | Media |
| ENV-15 | Monto cero o negativo | 0 y -10.000 | Rechazo por monto inválido | Partición de equivalencia | Validación | Media |
| ENV-16 | Monto con caracteres inválidos | vacío, "abc", "1e5", "10.000$" | Mensaje de validación, sin errores técnicos | Adivinanza de errores | Validación | Media |
| ENV-17 | Monto con decimales | 5000.50 | Rechazo o manejo según el PO | Partición de equivalencia | Validación | Baja |
| ENV-18 | Historial de ambos usuarios | Envío exitoso, revisar historiales | Salida en A y entrada en B, con monto, fecha/hora y contraparte | Transición de estados | Integración | Alta |
| ENV-19 | Falla sin afectar el saldo | Provocar un error de validación | Saldo y historial sin cambios | Tabla de decisión | Funcional negativa | Alta |
| ENV-20 | Pérdida de conexión al confirmar | Cortar internet al enviar | Transacción atómica, saldos consistentes | Adivinanza de errores | Confiabilidad, integración | Alta |
| ENV-21 | Doble clic en "Enviar" | Dos clics rápidos | Una sola transacción | Adivinanza de errores | Funcional, concurrencia | Alta |
| ENV-22 | Envíos simultáneos | Saldo $100.000, dos envíos de $80.000 | Solo uno se procesa, saldo nunca negativo | Adivinanza de errores | Concurrencia, rendimiento | Alta |
| ENV-23 | Manipulación del monto en la petición | Cambiar el monto a 3.000.000 | El backend rechaza la petición | Adivinanza de errores | Seguridad | Alta |
| ENV-24 | Sesión expirada al confirmar | Sesión vencida | Redirección al login, sin transacción | Transición de estados | Seguridad | Alta |
| ENV-25 | Combinación de condiciones | Ver tabla de decisión | Éxito solo si se cumplen todas las condiciones | Tabla de decisión | Funcional | Alta |
| ENV-26 | Claridad de mensajes | Revisar mensajes de error y confirmación | Mensajes comprensibles, sin códigos técnicos | Basada en experiencia | Usabilidad | Media |
| ENV-27 | Regresión del módulo | Ejecutar login y saldo tras un cambio en envío | Sin afectación en funciones existentes | Basada en casos previos | Regresión | Media |

---

## Tabla de decisión (ENV-25)

| Condición | R1 | R2 | R3 | R4 | R5 | R6 |
|---|---|---|---|---|---|---|
| Usuario autenticado | S | S | S | S | S | N |
| Monto entre 5.000 y 2.000.000 | S | N | S | S | S | S |
| Saldo suficiente | S | S | N | S | S | S |
| Destinatario registrado | S | S | S | N | S | S |
| Celular distinto al propio | S | S | S | S | N | S |
| **Resultado** | Éxito | Rechazo | Rechazo | Rechazo | Rechazo | Rechazo |

---

## Resumen de técnicas y tipos de prueba

### Técnicas de diseño

| Técnica | Dónde se aplica |
|---|---|
| Partición de equivalencia | Montos, celulares y credenciales (válidas, inválidas, vacías) |
| Análisis de valores límite | 4.999 / 5.000 / 5.001, 1.999.999 / 2.000.000 / 2.000.001, saldo exacto, longitud del celular |
| Tabla de decisión | Combinación de condiciones del envío |
| Transición de estados | Cuenta activa/bloqueada, sesión activa/cerrada, actualización del saldo |
| Adivinanza de errores | Doble clic, +57, pérdida de conexión, manipulación de la petición |

### Tipos de prueba

| Tipo de prueba | Dónde se aplica |
|---|---|
| Humo | LOG-01, SAL-01, ENV-01 tras cada despliegue |
| Funcional | Reglas de negocio de los tres módulos |
| Integración | Saldo, transacción e historial |
| Seguridad | Sesión, bloqueo, acceso a datos ajenos, manipulación del monto |
| Validación de datos | Formatos de celular y monto |
| Usabilidad | Mensajes claros, formularios |
| Rendimiento y concurrencia | Envíos simultáneos, tiempo de carga |
| Regresión | Login y saldo tras cambios en el envío |
