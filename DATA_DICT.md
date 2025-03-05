---
title: "Descripción de los datos"
format: html
---

# Descripción de los datos

| Nombre del Campo       | Tipo          | Descripción                                                                 |
|-----------------------|---------------|-----------------------------------------------------------------------------|
| Acceso_Estacion        | STRING        | Acceso de la estación.<br><em>Solo aplica para troncal</em>                 |
| Day_Group_Type         | STRING        | Tipo de día                                                                |
| **Dispositivo**            | STRING        | Identificador del dispositivo                                              |
| **Emisor**                 | STRING        | Emisor de la tarjeta                                                       |
| **Estacion_Parada**        | STRING        | Estación o Parada donde ocurrió la validación                              |
| **Fase**                   | STRING        | Fase a la que pertenece                                                    |
| **Fecha_Clearing**         | DATE          | Fecha en la que llego el registro al sistema                               |
| **Fecha_Transaccion**      | TIMESTAMP     | Fecha en la que ocurrió la transacción                                     |
| **Hora_Pico_SN**           | STRING        | Hora pico                                                                  |
| **ID_Vehiculo**            | STRING        | Identificador del vehículo<br><em>Solo aplica para Zonal y Dual.</em>       |
| **Linea**                  | STRING        | Línea.<br><em>En troncal son las zonas, en zonal son las rutas comerciales.</em> |
| **Nombre_Perfil**          | STRING        | Nombre del perfil. ver: [beneficios tarjetas tullave](https://www.transmilenio.gov.co/publicaciones/151046/beneficios-de-la-tarjeta-tullave/) <br> |
|                        |               | Nombre del Perfil - Descripción                                            |
|                        |               | - (001) Anonymous: Tarjeta <strong>NO</strong> Personalizada               |
|                        |               | - (001) Adulto: Tarjeta Personalizada                                      |
|                        |               | - (002) Adulto Mayor: Tarjeta Personalizada con subsidio a personas mayores de 62 Años |
|                        |               | - (005) Discapacidad: Tarjeta Personalizada con subsidio a personas en condición de discapacidad |
|                        |               | - (006) Apoyo Ciudadano: Tarjeta Personalizada con subsidio a personas en el SISBEN |
|                        |               | - (009) Apoyo Ciudadano Reexpedición: Tarjeta Personalizada con subsidio a personas en el SISBEN |
|                        |               | - (101) Adulto PV: Tarjeta Personalizada virtualmente [personalizacion virtual](https://personalizacionvirtual.tullaveplus.gov.co/) |
| **Numero_Tarjeta**         | STRING        | Número de tarjeta                                                          |
| **Operador**               | STRING        | Operador del servicio.<br><em><strong>Trunk Agency</strong> para troncal</em> |
| **Ruta**                   | STRING        | Ruta<br><em>Solo aplica para zonal.</em>                                   |
| **Saldo Despues Transaccion** | FLOAT       | Saldo después de la transacción                                            |
| **Saldo_Previo_a_Transaccion** | FLOAT     | Saldo previo a la transacción                                              |
| **Tipo_Tarifa**            | STRING        | Tipo de tarifa                                                             |
| **Tipo_Tarjeta**           | STRING        | Tipo de tarjeta                                                            |
| **Tipo_Vehiculo**          | STRING        | Tipo de vehículo.<br><em>Solo aplica para zonal.</em>                      |
| **Valor**                  | FLOAT         | Valor de la transacción                                                    |