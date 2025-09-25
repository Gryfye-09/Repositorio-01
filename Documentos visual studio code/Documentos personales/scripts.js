const menuToggle = document.getElementById('menu-toggle');
const navMenu = document.getElementById('nav-menu');
const closeBtn = document.getElementById('close-menu');

menuToggle.addEventListener('click', () => {
  navMenu.classList.add('open');
});

closeBtn.addEventListener('click', () => {
  navMenu.classList.remove('open');
});

// Cerrar al hacer clic en un enlace
document.querySelectorAll('.nav-menu a').forEach(link => {
  link.addEventListener('click', () => {
    navMenu.classList.remove('open');
  });
});

//Funcionalidad botones into, temas, conclusión

var acc = document.getElementsByClassName("accordion");
var i;

for (i = 0; i < acc.length; i++) {
    acc[i].onclick = function(){
        this.classList.toggle("active");
        this.nextElementSibling.classList.toggle("show");
  }
}
