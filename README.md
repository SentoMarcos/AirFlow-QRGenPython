
# Airflow QR Code Generator

Este proyecto genera códigos QR personalizados que integran un diseño elegante y permiten asociar un sensor (identificado por su UUID) a la aplicación móvil Airflow. El código QR incluye un logo centrado, esquinas redondeadas, y colores personalizados.

## Características

- **Diseño Personalizado**: Códigos QR con esquinas redondeadas y colores ajustables.
- **Logo Integrado**: Logotipo de Airflow centrado en el código QR.
- **Generación de UUID**: Incluye el UUID del sensor y su número de serie.
- **Exportación en PNG**: Genera archivos de imagen listos para imprimir o compartir.

## Archivos Incluidos

1. **logoAirFlow.svg**: Archivo SVG del logotipo de Airflow.
2. **QR_AirFlow_EPSG-GTI-PROY-3D.png**: Ejemplo de código QR generado.
3. **QR_rounded_border.png**: Otro ejemplo con diseño personalizado.
4. **QRGenerador.py**: Script Python para generar los códigos QR.

## Requisitos del Sistema

- **Python 3.7 o superior**
- Librerías Python:
  - `qrcode`
  - `Pillow`
  - `cairosvg`
- Archivo SVG para el logo (por ejemplo, `logoAirFlow.svg`).

## Instalación

1. Clona este repositorio en tu máquina local:
   ```bash
   git clone https://github.com/SentoMarcos/airflow-qr-generator.git
   cd airflow-qr-generator
   ```

2. Instala las dependencias:
   ```bash
   pip install -r requirements.txt
   ```

3. Asegúrate de tener el archivo `logoAirFlow.svg` en el directorio principal.

## Uso

1. Modifica los datos en el script `QRGenerador.py` para personalizar el UUID y el número de serie del sensor:
   ```python
   data = {
       "uuid": "EPSG-GTI-PROY-3D",
       "num_serie": "ABC123456",
   }
   ```

2. Ejecuta el script para generar el código QR:
   ```bash
   python QRGenerador.py
   ```

3. El código QR se guardará con el nombre `QR_AirFlow_{uuid}.png`.

## Ejemplo de Código QR

![QR Code](QR_AirFlow_EPSG-GTI-PROY-3D.png)

Este QR puede ser escaneado con la aplicación móvil Airflow para enlazar el sensor asociado.

## Personalización

- **Colores**: Ajusta los colores del QR modificando los parámetros `fill_color` y `back_color` en el script.
- **Esquinas redondeadas**: Cambia el radio de las esquinas redondeadas con el parámetro `border_radius`.
- **Logo**: Reemplaza `logoAirFlow.svg` con tu propio logo si es necesario.

## Autor

Este proyecto fue desarrollado por **SentoMarcos**.
- [GitHub - SentoMarcos](https://github.com/SentoMarcos)

## Proyectos Relacionados

Si te interesa este proyecto, quizá encuentres útiles los siguientes:

- [AirFlow-Web](https://github.com/SentoMarcos/AirFlow-Web)
- [Airflow-Android](https://github.com/SentoMarcos/AirFlow-Android)
- [Airflow-Arduino](https://github.com/SentoMarcos/AirFlow-Arduino)

## Contribuciones

¡Se aceptan contribuciones! Si deseas colaborar, sigue estos pasos:

1. Haz un fork del repositorio.
2. Crea una rama para tu característica o corrección (`git checkout -b feature/nueva-funcionalidad`).
3. Haz commit de tus cambios (`git commit -m 'Añadir nueva funcionalidad'`).
4. Sube tus cambios (`git push origin feature/nueva-funcionalidad`).
5. Abre un Pull Request.

