document.addEventListener('DOMContentLoaded', function() {
    var modoBtn = document.getElementById('modoBtn');
  
    modoBtn.addEventListener('click', function() {
      var body = document.body;
      body.classList.toggle('dark-mode');
      console.log(body.classList.contains('dark-mode') ? 'Modo oscuro activado' : 'Modo oscuro desactivado');
      
      var modoActual = body.classList.contains('dark-mode') ? 'dark' : 'light';
      localStorage.setItem('modoPreferido', modoActual);
    });

    var modoPreferido = localStorage.getItem('modoPreferido');
    if (modoPreferido === 'dark') {
      document.body.classList.add('dark-mode');
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

  if (window.scrollY > 300) {
      volverArribaBtn.style.display = "block"; // Mostrar el botón cuando el usuario haya desplazado 300px hacia abajo
      
  } else {
      volverArribaBtn.style.display = "none"; // Ocultar el botón si el usuario está en la parte superior de la página
  }
});


