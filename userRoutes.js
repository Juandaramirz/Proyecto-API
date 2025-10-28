
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
