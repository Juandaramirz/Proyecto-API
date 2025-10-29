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