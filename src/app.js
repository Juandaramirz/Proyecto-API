const express = require('express');
const app = express();
const bodyParser = require('body-parser');
const userRoutes = require('./routes/userRoutes'); // Ajusta la ruta según tu estructura

app.use(bodyParser.json());

// Ruta de bienvenida
app.get('/', (req, res) => {
  res.send('¡Bienvenido a la API de usuarios!');
});

// Rutas de usuarios protegidas
app.use('/api/users', userRoutes);

// Manejo de errores
app.use((err, req, res, next) => {
  console.error(err.stack);
  res.status(500).json({ message: 'Error interno del servidor' });
});

// Exporta solo la instancia de app, NO levantes el servidor aquí.
module.exports = app;