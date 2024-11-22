
# Información del Script

Este script permite crear un servidor PHP que recopila información básica de dispositivos a través de enlaces generados dinámicamente. Es ideal para quienes necesitan probar configuraciones de red, analizar la conectividad y experimentar con la integración de herramientas como Ngrok y Localhost.run.

## Características Principales

1. **Generación de Enlaces:**
   - Permite crear enlaces públicos a través de:
     - **Ngrok**
     - **Localhost.run**
   - Ofrece la opción de acortar los enlaces con un servicio de acortamiento (is.gd).

2. **Opciones de Página de Destino:**
   - **Página de Error 404 Predeterminada:** Una página simulada de error 404 para mantener el anonimato del enlace.
   - **Redirección Personalizada:** Posibilidad de redirigir a un sitio web de tu elección.

3. **Recopilación de Información:**
   - IP pública del dispositivo.
   - Navegador utilizado (User-Agent).
   - Hostname del dispositivo.
   - Fecha y hora de la interacción.

4. **Registro Automático:**
   - Los datos recopilados se almacenan automáticamente en un archivo llamado `ip_guardadas.txt` para un análisis posterior.

5. **Interfaz Clara:**
   - Logo llamativo y menús interactivos que facilitan la experiencia del usuario.

## Requisitos

- Python 3
- PHP instalado en el sistema
- Herramientas adicionales descargadas automáticamente (como Ngrok)

## Instalación

1. Clona el repositorio o copia los archivos necesarios.
2. Asegúrate de que tienes permisos de ejecución y que las dependencias están instaladas.
3. Ejecuta el script principal con el comando:
   ```bash
   python3 phish_linker.py
   ```

## Uso

1. Elige la opción deseada desde el menú principal:
   - **Iniciar Servidor PHP:** Comienza a generar enlaces y recopilar información.
   - **Salir:** Cierra el script.

2. Sigue las instrucciones en pantalla para configurar el comportamiento del servidor (página de error o redirección personalizada).

3. Comparte el enlace generado con la víctima objetivo y espera a que acceda.

## Logs

- **Logs de Ngrok y Localhost.run:** Se almacenan en `logs/ngrok.log` y `logs/lh.log`.
- **Errores:** Se registran en `logs/error.log`.

## Advertencia

Este script debe ser utilizado únicamente en entornos controlados y con fines educativos. El uso indebido podría tener consecuencias legales. El autor no se hace responsable por el uso que se le dé.

## Autor

Creado por **C0d1ngj4ndr3s**
