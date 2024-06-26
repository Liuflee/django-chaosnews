document.addEventListener('DOMContentLoaded', function() {
  var body = document.body;
  var html = document.querySelector("html");
  var modoBtn = document.getElementById('modoBtn');
  var modoPreferido = localStorage.getItem('modoPreferido');

  function toggleDarkMode() {
    html.classList.toggle('dark');
    body.classList.toggle('dark-mode');
    console.log(body.classList.contains('dark-mode') ? 'Modo oscuro activado' : 'Modo oscuro desactivado');
    localStorage.setItem('modoPreferido', body.classList.contains('dark-mode') ? 'dark' : 'light');
  }

  modoBtn.addEventListener('click', toggleDarkMode);

  if (modoPreferido === 'dark') {
    html.classList.add('dark');
    body.classList.add('dark-mode');
  }
});


  // Función para controlar el desplazamiento hacia arriba
function scrollToTop() {
  window.scrollTo({
      top: 0,
      behavior: "smooth" // Desplazamiento suave
  });
}

// Mostrar u ocultar el botón de volver arriba según la posición del usuario en la página
window.addEventListener("scroll", function() {
  var volverArribaBtn = document.getElementById("volverArribaBtn");

  // si la pagina se recarga el boton no se muestra




  // si el usuario se m
  
  if (window.scrollY > 300) {
      volverArribaBtn.style.display = "block"; // Mostrar el botón cuando el usuario haya desplazado 300px hacia abajo
      
  } else {
      volverArribaBtn.style.display = "none"; // Ocultar el botón si el usuario está en la parte superior de la página
  }
});


