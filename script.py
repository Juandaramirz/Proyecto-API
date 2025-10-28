# El proyecto será una API RESTful utilizando el patrón MVC para una arquitectura sencilla, escalable y mantenible.
# Framework: Express.js para Node.js por su popularidad y ecosistema robusto.


import os

# Crear estructura básica de carpetas siguiendo MVC
os.makedirs('myapi/src/controllers', exist_ok=True)
os.makedirs('myapi/src/models', exist_ok=True)
os.makedirs('myapi/src/routes', exist_ok=True)
os.makedirs('myapi/tests', exist_ok=True)

# Archivo de configuración principal y paquete básico
app_js = ''
const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const userRoutes = require('./routes/userRoutes');

app.use(bodyParser.json());

// Rutas
app.use('/api/users', userRoutes);

// Manejo de errores genéricos
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Error interno del servidor' });
});

const PORT = process.env.PORT || 3000;
app.listen(PORT, () => {
  console.log(`Servidor corriendo en puerto ${PORT}`);
});
'''

# Archivo de rutas de usuarios
user_routes_js = '''
const express = require('express');
const router = express.Router();
const userController = require('../controllers/userController');
const basicAuth = require('../middlewares/basicAuth');

// Endpoints con autenticación básica
router.get('/', basicAuth, userController.getAllUsers);
router.get('/:id', basicAuth, userController.getUserById);
router.post('/', basicAuth, userController.createUser);
router.put('/:id', basicAuth, userController.updateUser);
router.delete('/:id', basicAuth, userController.deleteUser);

module.exports = router;
'''

# Controlador userController (control simple en memoria para demo)
user_controller_js = '''
let users = [{ id: 1, name: 'User One', email: 'userone@example.com' }];

exports.getAllUsers = (req, res) => {
  res.json(users);
};

exports.getUserById = (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ message: 'Usuario no encontrado' });
  res.json(user);
};

exports.createUser = (req, res) => {
  const { name, email } = req.body;
  if (!name || !email) {
    return res.status(400).json({ message: 'Nombre y email son obligatorios' });
  }
  const newUser = { id: users.length + 1, name, email };
  users.push(newUser);
  res.status(201).json(newUser);
};

exports.updateUser = (req, res) => {
  const user = users.find(u => u.id === parseInt(req.params.id));
  if (!user) return res.status(404).json({ message: 'Usuario no encontrado' });
  const { name, email } = req.body;
  if (!name || !email) {
    return res.status(400).json({ message: 'Nombre y email son obligatorios' });
  }
  user.name = name;
  user.email = email;
  res.json(user);
};

exports.deleteUser = (req, res) => {
  const index = users.findIndex(u => u.id === parseInt(req.params.id));
  if (index === -1) return res.status(404).json({ message: 'Usuario no encontrado' });
  users.splice(index, 1);
  res.status(204).send();
};
'''

# Middleware de autenticación básica
basic_auth_js = '''
module.exports = (req, res, next) => {
  const authHeader = req.headers.authorization;
  if (!authHeader) {
    res.setHeader('WWW-Authenticate', 'Basic');
    return res.status(401).json({ message: 'Autenticación requerida' });
  }
  const base64Credentials = authHeader.split(' ')[1];
  const credentials = Buffer.from(base64Credentials, 'base64').toString('ascii');
  const [username, password] = credentials.split(':');
  if (username === 'admin' && password === 'password') {
    next();
  } else {
    return res.status(403).json({ message: 'Credenciales incorrectas' });
  }
};
''

# Guardar archivos
with open('myapi/src/app.js', 'w') as f:
    f.write(app_js)
with open('myapi/src/routes/userRoutes.js', 'w') as f:
    f.write(user_routes_js)
with open('myapi/src/controllers/userController.js', 'w') as f:
    f.write(user_controller_js)
with open('myapi/src/middlewares/basicAuth.js', 'w') as f:
    f.write(basic_auth_js)



with open('myapi/README.md', 'w') as f:
    f.write(readme_content)


