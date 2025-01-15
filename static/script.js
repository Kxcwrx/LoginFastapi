// Manejo del login
document.getElementById('login-form').addEventListener('submit', async (e) => {
    e.preventDefault();
  
    const username = document.getElementById('username').value;
    const password = document.getElementById('password').value;
  
    try {
      const response = await fetch('http://127.0.0.1:8000/login', {
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
        document.getElementById('response-message').style.color = 'green';
        document.getElementById('response-message').textContent = `Bienvenido, ${data.usuario}`;
      } else {
        document.getElementById('response-message').style.color = 'red';
        document.getElementById('response-message').textContent = data.detail;
      }
    } catch (error) {
      console.error('Error:', error);
      document.getElementById('response-message').textContent = 'Error de conexión.';
    }
  });
  
  // Redirección al registro
  document.getElementById('register-btn').addEventListener('click', () => {
    window.location.href = 'register.html';
  });
  