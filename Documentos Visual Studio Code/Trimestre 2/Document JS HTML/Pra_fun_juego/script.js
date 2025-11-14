
/* Barra de vida y el texto de Vanellope */
var hpBarPlayer = document.getElementById('hpBarPlayer');   // <progress>
var hpTextPlayer = document.getElementById('hpTextPlayer'); // <span>
var playerImage = document.getElementById('playerImage');   // <img>


/* Barra de vida y el texto de King Candy */
var hpBarEnemy = document.getElementById('hpBarEnemy');     // <progress>
var hpTextEnemy = document.getElementById('hpTextEnemy');   // <span>
var enemyImage = document.getElementById('enemyImage');     // <img>


/* Vida */
var vidaPlayer = 100;
var vidaEnemy = 120;


/* Daños que hacen los ataques a King Candy */
var danoMap = {
  hammer: 35,
  fists: 25,
  cop: 20
};


/* Daños que hacen los ataques a Vanellope como obstaculo adicional */
var obstaculoMap = {
  hammer: 8,
  fists: 6,
  cop: 10
};


/* Gifs de los ataques */
var ataqueGifMap = {
  hammer: 'Martillo.gif',
  fists:  'Ralph.gif',
  cop:    'Policias.gif'
};


/* Cura para Vanellope */
var curaMap = {
  caramel: 18,
  choco:   30
};


/* Gifs de los dulces para la cura */
var curaGifMap = {
  caramel: 'Caramelos.gif',
  choco:   'chocolates.gif'
};





/* Funcion attack (type) Los ataques quitan vida al enemigo y a la vez
   causan daño por obstáculo a Vanellope. */
   
function attack(type) {
  var dañoAlEnemigo = danoMap[type]; /* Daño al King Candy */
  var dañoALaPlayer = obstaculoMap[type]; /* Daño a Vanellope por obstaculo */


  /* Aplicar efectos en las vidas */
  vidaEnemy = vidaEnemy - dañoAlEnemigo; /* Resta la vida de King Candy */
  vidaPlayer = vidaPlayer - dañoALaPlayer; /* Resta la vida de Vanellope */


  /* Animación del enemigo según el ataque */
  enemyImage.src = ataqueGifMap[type];


  /* Vanellope siempre muestra su GIF base */ 
  playerImage.src = 'Vanellope.gif';


  /* Actualizar barras de vida */
  hpBarPlayer.value = vidaPlayer;
  hpBarEnemy.value = vidaEnemy;


  /* Actualizar textos de vida */
  hpTextPlayer.innerHTML = parseInt(vidaPlayer, 10) + ' / ' + hpBarPlayer.max;
  hpTextEnemy.innerHTML = parseInt(vidaEnemy, 10) + ' / ' + hpBarEnemy.max;


  /* Volver a idle cuando termine la animacion */
  setTimeout(function () {
    enemyImage.src = 'kingCandy.gif';
    playerImage.src = 'Vanellope.gif';
  }, 1400);

  console.log('attack', type, 'enemyDamage', dañoAlEnemigo, 'playerDamage', dañoALaPlayer);
}





/* Funcion heal(kind) Esta función cura a Vanellope usando dulces */

function heal(kind) {

  var efecto = curaMap[kind]; /* cuánta vida recupera */

  vidaPlayer = vidaPlayer + efecto; /* aplica la curación */


  /* Poner GIF de curación de Vanellope */
  playerImage.src = curaGifMap[kind];


  /* Actualizar interfaz */
  hpBarPlayer.value = vidaPlayer;
  hpBarEnemy.value = vidaEnemy;

  hpTextPlayer.innerHTML = parseInt(vidaPlayer, 10) + ' / ' + hpBarPlayer.max;
  hpTextEnemy.innerHTML = parseInt(vidaEnemy, 10) + ' / ' + hpBarEnemy.max;


  /* Regresar al GIF normal */
  setTimeout(function () {
    playerImage.src = 'Vanellope.gif';
  }, 1200);

  console.log('heal', kind, 'efecto', efecto);
}
