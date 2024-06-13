  // Función para el efecto de las noticias relacionadas
  function stickyOtherNews() {
    var otherNews = document.querySelector('.other-news');
    var otherNewsOffset = otherNews.offsetTop;
      if (window.scrollY > otherNewsOffset) {
          otherNews.classList.add('sticky');
      } else {
          otherNews.classList.remove('sticky');
      }
    }
  
    // Agregar un event listener para detectar el desplazamiento de la página
    window.addEventListener('scroll', stickyOtherNews);
  
    // Event listener para el botón de like
    document.getElementById('like-button').addEventListener('click', function() {
      var url = this.getAttribute('data-url');
      fetch(url, {
        method: 'POST',
        headers: {
          'X-CSRFToken': '{{ csrf_token }}',
          'Content-Type': 'application/json'
        }
      })
      .then(response => response.json())
      .then(data => {
        document.getElementById('likes-count').textContent = data.likes_count;
      });
    });
  
    //Función para el tamaño del textarea del comentario principal
    document.addEventListener('DOMContentLoaded', function() {
      var textarea = document.getElementById('comment-area');
  
      textarea.addEventListener('input', function() {
          this.style.height = 'auto'; // Resetea la altura para calcular el scrollHeight correctamente
          this.style.height = (this.scrollHeight) + 'px';
      });
  
      textarea.addEventListener('focus', function() {
          this.classList.add('no-placeholder'); // Oculta el placeholder
          if (this.scrollHeight < 152) {
              this.style.height = '150px'; // Altura mínima al enfocarse
          } else {
              this.style.height = (this.scrollHeight) + 'px'; // Ajuste según el contenido
          }
      });
  
      textarea.addEventListener('blur', function() {
          this.classList.remove('no-placeholder'); // Muestra el placeholder nuevamente
          if (this.value === '') {
              this.style.height = '50px'; // Altura base al perder el foco si está vacío
          }
      });
  });
  
    //Función para mostrar el botón de enviar al enfocar el área de comentario
    document.addEventListener('DOMContentLoaded', function() {
      var commentArea = document.getElementById('comment-area');
      var sendButtonWrapper = document.querySelector('.send-btn-wrapper');
  
      // Mostrar el contenedor del botón de enviar cuando el área de comentario obtiene foco
      commentArea.addEventListener('focus', function() {
          sendButtonWrapper.style.display = 'flex';
      });
  
      // Ocultar el contenedor del botón de enviar cuando el área de comentario pierde foco y está vacía
      commentArea.addEventListener('blur', function() {
          if (commentArea.value.trim() === '') {
              sendButtonWrapper.style.display = 'none';
          }
      });
  
      // Si el área de comentario ya tiene contenido al cargar la página, asegúrate de mostrar el contenedor del botón de enviar
      if (commentArea.value.trim() !== '') {
          sendButtonWrapper.style.display = 'flex';
      } else {
          sendButtonWrapper.style.display = 'none';
      }
  });
  
   // Función para enviar el formulario de comentarios
    $(document).ready(function(){
    $('#comment-form').submit(function(event){
      event.preventDefault();
      
      var form = $(this);
      var actionUrl = form.attr('action');
      var formData = form.serialize();
      
      $.post(actionUrl, formData, function(response){
        // Suponiendo que el servidor devuelve la sección de comentarios actualizada
        $('#comments').html($(response).find('#comments').html());
        
        // Desplazar el scroll hacia la sección de comentarios
        $('html, body').animate({
          scrollTop: $("#comment-section").offset().top
        }, 1000);
        
        // Limpiar el área de comentario
        $('#comment-area').val('');
        $('#comment-area').blur();
  
      });
    });
  });
  
    // Función para manejar el formulario de las respuestas.
    $(document).ready(function(){
  
      $('.reply-form').submit(function(event){
          event.preventDefault();
          
          var form = $(this);
          var actionUrl = form.attr('action');
          var formData = form.serialize();
          
          $.post(actionUrl, formData, function(response){
  
              var parentId = form.find('input[name="parent_id"]').val();
              $('#replies-' + parentId).html($(response).find('#replies-' + parentId).html());
  
              var newReplyCount = $(response).find('.btn-toggle-replies[data-comment-id="' + parentId + '"]').data('replies-count');
              console.log("New reply count:", newReplyCount);
  
              var replyButton = $('#reply-count-' + parentId).find('.btn-toggle-replies');
              replyButton.data('replies-count', newReplyCount);
  
              if (newReplyCount == 1) {
                  replyButton.html('<i class="fa-solid fa-chevron-down"></i> ' + newReplyCount + ' respuesta');
              } else {
                  replyButton.html('<i class="fa-solid fa-chevron-down"></i> ' + newReplyCount + ' respuestas');
              }
  
   
              form.find('textarea').val('');
          }).fail(function(){
              console.log("Error al enviar la respuesta.");
          });
      });
    
  
      window.toggleReplyForm = function(commentId) {
          $('#reply-form-' + commentId).toggle();
      }
  
      window.toggleReplies = function(commentId) {
          $('#replies-' + commentId).toggle();
      }
  });