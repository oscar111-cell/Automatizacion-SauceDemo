# language: en

Feature: Inicio de sesión en SauceDemo
  Como usuario de SauceDemo
  Quiero iniciar sesión
  Para acceder al inventario

  Background:
    Given que abro la página de inicio de sesión

  Scenario: Login exitoso con credenciales válidas
    When inicio sesión con usuario "standard_user" y contraseña "secret_sauce"
    Then debo ver el inventario

  Scenario: Login fallido con contraseña incorrecta
    When inicio sesión con usuario "standard_user" y contraseña "incorrecta"
    Then debo ver el mensaje de error "Epic sadface: Username and password do not match any user in this service"

  Scenario: Validación de campos obligatorios
    When intento iniciar sesión sin usuario ni contraseña
    Then debo ver el mensaje de error "Epic sadface: Username is required"