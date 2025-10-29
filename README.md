# API RESTful - Guía de Usuario y Despliegue

## Descripción
Esta API RESTful implementa gestión básica de usuarios con autentificación básica, organizada según el patrón MVC.

## Requisitos
- Node.js v16+
- npm
- Git

## Instalación
Clonar el repositorio
Instalar dependencias
npm install


## Ejecución
npm start

Servidor correrá en http://localhost:3000

## Endpoints
| Método | Ruta           | Descripción              | Autenticación |
|--------|----------------|--------------------------|--------------|
| GET    | /api/users     | Listar usuarios          | Sí           |
| GET    | /api/users/:id | Obtener usuario por ID   | Sí           |
| POST   | /api/users     | Crear usuario            | Sí           |
| PUT    | /api/users/:id | Actualizar usuario       | Sí           |
| DELETE | /api/users/:id | Eliminar usuario         | Sí           |

## Autenticación
- Autenticación básica HTTP
- Usuario: `admin`, Contraseña: `password`

## Pipeline de Integración Continua (CI)
- Automatiza instalación, análisis de código, ejecución de tests
- Se ejecuta en GitHub Actions en rama `main`
- Etapas:
  - Checkout
  - Instalación dependencias
  - ESLint para análisis
  - Ejecución de pruebas con Mocha

## Arquitectura

### Patrón MVC
La aplicación se organiza en Modelos (manejo de datos), Controladores (lógica y rutas) y Rutas (definición de endpoints). Esto facilita organización y mantenibilidad.

### Diagrama arquitectónico 
+-------------+      +----------------+      +------------+
|   Rutas     | ---> | Controladores  | ---> |   Modelos  |
+-------------+      +----------------+      +------------+


### Flujo pipeline CI
[Push a main] --> [GitHub Actions] --> [Checkout] --> [npm install] --> [eslint] --> [mocha tests] --> [Resultado]


## Pruebas
- Ejemplo de prueba para GET /api/users incluido
- Uso de jest: tests unitarios e integración

## Comandos útiles
npm start # Ejecuta el servidor
npm test # Ejecuta las pruebas
npm run lint # Ejecuta ESLint