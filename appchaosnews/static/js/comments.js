
document.addEventListener('DOMContentLoaded', function() {
    var replyForms = document.querySelectorAll('.comment-reply-area');

    replyForms.forEach(function(textarea) {
        textarea.addEventListener('input', function() {
            this.style.height = '30px'; // Resetea la altura para calcular correctamente el scrollHeight
            this.style.height = (this.scrollHeight) + 'px';
        });
    });
});


    function toggleReplyForm(commentId) {
        var form = document.getElementById('reply-form-' + commentId);
        if (form.style.display === 'none') {
            form.style.display = 'block';
        } else {
            form.style.display = 'none';
        }
    }

    function toggleReplies(commentId) {
    var replies = document.getElementById('replies-' + commentId);
    var toggleButton = document.querySelector('.btn-toggle-replies[data-comment-id="' + commentId + '"]');
    var repliesCount = parseInt(toggleButton.getAttribute('data-replies-count'));

    if (replies.style.display === 'none') {
        replies.style.display = 'block';
        toggleButton.innerHTML = '<i class="fa-solid fa-chevron-up"></i> ' + repliesCount + (repliesCount > 1 ? ' respuestas' : ' respuesta');
    } else {
        replies.style.display = 'none';
        toggleButton.innerHTML = '<i class="fa-solid fa-chevron-down"></i> ' + repliesCount + (repliesCount > 1 ? ' respuestas' : ' respuesta');
    }
}


    document.querySelectorAll('.btn-like').forEach(button => {
        button.addEventListener('click', function() {
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
                    document.getElementById('likes-count-' + data.comment_id).textContent = data.likes_count;
                })
                .catch(error => console.error('Error:', error));
        });
    });



