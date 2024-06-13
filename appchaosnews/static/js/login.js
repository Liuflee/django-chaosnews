document.getElementById('togglePassword').addEventListener('click', function() {
    var passwordField = document.getElementById('password_l');
    var type = passwordField.type === 'password' ? 'text' : 'password';
    passwordField.type = type;
    this.classList.toggle('fa-eye');
    this.classList.toggle('fa-eye-slash');
});
