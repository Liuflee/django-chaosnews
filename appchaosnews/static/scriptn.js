document.addEventListener('DOMContentLoaded', function() {
    let modoBtn = document.getElementById('modoBtn');
  
    modoBtn.addEventListener('click', function() {
      let body = document.body;
      body.classList.toggle('dark-mode');
      console.log(body.classList.contains('dark-mode') ? 'Modo oscuro activado' : 'Modo oscuro desactivado');
      
      let modoActual = body.classList.contains('dark-mode') ? 'dark' : 'light';
      localStorage.setItem('modoPreferido', modoActual);
    });

    let modoPreferido = localStorage.getItem('modoPreferido');
    if (modoPreferido === 'dark') {
      document.body.classList.add('dark-mode');
    }
  });


  // función para controlar el desplazamiento hacia arriba
function scrollToTop() {
  window.scrollTo({
      top: 0,
      behavior: "smooth" // desplazamiento suave
  });
}

// mostrar u ocultar el botón de volver arriba según la posición del usuario en la página
window.addEventListener("scroll", function() {
  let volverArribaBtn = document.getElementById("volverArribaBtn");

  if (window.scrollY > 400) {
      volverArribaBtn.style.display = "block"; // mostrar el botón cuando el usuario se haya movido 400px hacia abajo
      
  } else {
      volverArribaBtn.style.display = "none"; // ocultar el botón si el usuario está en la parte de arriba de la página
  }
});

function stickyOtherNews() {
  let otherNews = document.querySelector('.other-news');
  let otherNewsOffset = otherNews.offsetTop;
    if (window.scrollY > otherNewsOffset) {
        otherNews.classList.add('sticky');
    } else {
        otherNews.classList.remove('sticky');
    }
}


window.addEventListener('scroll', stickyOtherNews);


  const form = document.getElementById('loginForm');

  function validarEmail(email) {
    const regex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
    return regex.test(email);
  }
  form.addEventListener('submit', function(event) {
    event.preventDefault();

    const email = document.getElementById('email').value;
    const password = document.getElementById('password').value;

    if (email.trim() === '' || password.trim() === '') {
      alert('Por favor, complete todos los campos.');
      return;
    }

    if (!validarEmail(email)) {
      alert('Por favor, ingrese un correo electrónico válido.');
      return;
    }
    document.getElementById('email').value = email;
    document.getElementById('password').value = password;

    console.log('Correo electrónico:', email);
    console.log('Contraseña:', password);
  });