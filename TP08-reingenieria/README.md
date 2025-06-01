# getJason.py

## Descripción

`getJason.py` es un script que automatiza pagos entre cuentas bancarias utilizando información de tokens almacenados en un archivo JSON (`sitedata.json`). El programa crea cuentas bancarias, procesa pagos automáticos y muestra un historial de los pagos realizados.

---

## Estructura de Archivos

- **getJason.py**: Script principal.
- **pagos.py**: Define las clases para pagos, cuentas bancarias y gestión de pagos.
- **lector_json.py**: Clase para leer tokens desde un archivo JSON.
- **sitedata.json**: Archivo de configuración con los tokens de las cuentas.

---

## Uso

Ejecuta el script desde la terminal:

```sh
python getJason.py
```

### Opciones

- `-v`: Muestra la versión del script y termina la ejecución.

```sh
python getJason.py -v
```

---

## Funcionamiento

1. **Lectura de tokens:**  
   Utiliza `LectorJSON` para leer los tokens de las cuentas desde `sitedata.json`.

2. **Creación de cuentas:**  
   Se crean instancias de `CuentaBancaria` con los tokens y saldos iniciales.

3. **Procesamiento de pagos:**  
   Se procesan pagos automáticos de $500 para 10 pedidos, alternando entre las cuentas disponibles.

4. **Historial de pagos:**  
   Se muestra un listado de todos los pagos realizados mediante `GestorPagos`.

---

## Ejemplo de Salida

```
==================================================
=== Automatización de Pagos Bancarios ============
==================================================
Creando cuentas bancarias desde 'sitedata.json'...
Procesando pagos automáticos...

Pago realizado: Pedido 1, Token <Token correspondiente a la cuenta>, Monto $500
Pago realizado: Pedido 2, Token <Token correspondiente a la cuenta>, Monto $500
...

--------------------------------------------------
Listado de pagos realizados:
--------------------------------------------------
Pago de 500 para el pedido 1 con token <Token correspondiente a la cuenta>
Pago de 500 para el pedido 2 con token <Token correspondiente a la cuenta>
...
==================================================
=========== Fin de la ejecución ==================
==================================================
```

---

## Clases Principales

- **LectorJSON**: Singleton para leer valores de un archivo JSON.
- **CuentaBancaria**: Representa una cuenta bancaria con token y saldo.
- **Pago**: Representa un pago realizado.
- **GestorPagos**: Gestiona el ciclo de pagos y el historial.

---

## Autoría

Copyright UADERFCyT-IS2©2024  
Todos los derechos reservados.