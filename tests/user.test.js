const request = require('supertest');
const app = require('../src/app');

describe('API de usuarios', () => {
  let createdUserId;

  test('GET /api/users obtiene todos los usuarios', async () => {
    const res = await request(app)
      .get('/api/users')
      .auth('admin', 'password')
      .expect(200);
    expect(Array.isArray(res.body)).toBe(true);
  });

  test('POST /api/users crea un usuario', async () => {
    const res = await request(app)
      .post('/api/users')
      .auth('admin', 'password')
      .send({ name: 'Nuevo', email: 'nuevo@correo.com' })
      .expect(201);
    expect(res.body).toHaveProperty('id');
    createdUserId = res.body.id;
  });

  test('GET /api/users/:id obtiene usuario por id', async () => {
    const res = await request(app)
      .get(`/api/users/${createdUserId}`)
      .auth('admin', 'password')
      .expect(200);
    expect(res.body.name).toBe('Nuevo');
  });

  test('PUT /api/users/:id actualiza usuario', async () => {
    const res = await request(app)
      .put(`/api/users/${createdUserId}`)
      .auth('admin', 'password')
      .send({ name: 'Actualizado', email: 'actualizado@correo.com' })
      .expect(200);
    expect(res.body.name).toBe('Actualizado');
  });

  test('DELETE /api/users/:id elimina usuario', async () => {
    await request(app)
      .delete(`/api/users/${createdUserId}`)
      .auth('admin', 'password')
      .expect(204);

    // El usuario ya no existe
    await request(app)
      .get(`/api/users/${createdUserId}`)
      .auth('admin', 'password')
      .expect(404);
  });
});