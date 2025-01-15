document.getElementById('register-form').addEventListener('submit', async (e) => {
  e.preventDefault();

  const username = document.getElementById('reg-username').value;
  const password = document.getElementById('reg-password').value;
  const confirmPassword = document.getElementById('reg-confirm-password').value;

  if (password !== confirmPassword) {
    document.getElementById('register-message').style.color = 'red';
    document.getElementById('register-message').textContent = 'Las contraseñas no coinciden.';
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
      document.getElementById('register-message').style.color = 'green';
      document.getElementById('register-message').textContent = 'Usuario registrado exitosamente.';
      setTimeout(() => {
        window.location.href = '/static/index.html'; // Redirige a index.html después de 2 segundos
      }, 2000);
    } else {
      document.getElementById('register-message').style.color = 'red';
      document.getElementById('register-message').textContent = data.detail || 'Error al registrar usuario.';
    }
  } catch (error) {
    console.error('Error:', error);
    document.getElementById('register-message').textContent = 'Error de conexión.';
  }
});
