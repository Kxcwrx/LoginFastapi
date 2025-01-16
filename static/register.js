document.getElementById('register-form').addEventListener('submit', async (e) => {
  e.preventDefault();

  const username = document.getElementById('reg-username').value.trim();
  const password = document.getElementById('reg-password').value;
  const confirmPassword = document.getElementById('reg-confirm-password').value;

  const message = document.getElementById('register-message');
  message.style.color = 'red';

  // Validaciones del cliente
  if (!username || username.length < 3) {
    message.textContent = 'El nombre de usuario debe tener al menos 3 caracteres.';
    return;
  }

  if (!/^[a-zA-Z0-9_]+$/.test(username)) {
    message.textContent = 'El nombre de usuario solo puede contener letras, números y guiones bajos.';
    return;
  }

  if (password.length < 6) {
    message.textContent = 'La contraseña debe tener al menos 6 caracteres.';
    return;
  }

  if (!/[A-Za-z]/.test(password) || !/[0-9]/.test(password)) {
    message.textContent = 'La contraseña debe contener letras y números.';
    return;
  }

  if (password !== confirmPassword) {
    message.textContent = 'Las contraseñas no coinciden.';
    return;
  }

  try {
    const response = await fetch('http://127.0.0.1:8000/register', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({
        nombre_usuario: username,
        contrasena: password,
      }),
    });

    const data = await response.json();

    if (response.ok) {
      message.style.color = 'green';
      message.textContent = 'Usuario registrado exitosamente.';
      setTimeout(() => {
        window.location.href = '/static/index.html';
      }, 2000);
    } else {
      message.textContent = data.detail || 'Error al registrar usuario.';
    }
  } catch (error) {
    console.error('Error:', error);
    message.textContent = 'Error de conexión.';
  }
});
