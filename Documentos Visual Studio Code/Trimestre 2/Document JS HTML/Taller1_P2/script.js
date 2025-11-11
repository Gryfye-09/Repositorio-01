/* Todas las funciones usan var (no let), no hay condicionales ni bucles.
   Los resultados se escriben con innerHTML en los elementos con id correspondiente. */

/* EJERCICIO 1: operaciones básicas */
function sumar(){
  var n1 = parseFloat(document.getElementById("num1").value);
  var n2 = parseFloat(document.getElementById("num2").value);
  var res = n1 + n2;
  document.getElementById("resultado1").innerHTML = "Suma: " + res;
}

function restar(){
  var n1 = parseFloat(document.getElementById("num1").value);
  var n2 = parseFloat(document.getElementById("num2").value);
  var res = n1 - n2;
  document.getElementById("resultado1").innerHTML = "Resta: " + res;
}

function multiplicar(){
  var n1 = parseFloat(document.getElementById("num1").value);
  var n2 = parseFloat(document.getElementById("num2").value);
  var res = n1 * n2;
  document.getElementById("resultado1").innerHTML = "Multiplicación: " + res;
}

function dividir(){
  var n1 = parseFloat(document.getElementById("num1").value);
  var n2 = parseFloat(document.getElementById("num2").value);
  var res = n1 / n2;
  document.getElementById("resultado1").innerHTML = "División: " + res;
}

function modulo(){
  var n1 = parseFloat(document.getElementById("num1").value);
  var n2 = parseFloat(document.getElementById("num2").value);
  var res = n1 % n2;
  document.getElementById("resultado1").innerHTML = "Módulo: " + res;
}

/* EJERCICIO 2: área triángulo */
function areaTriangulo(){
  var b = parseFloat(document.getElementById("base").value);
  var h = parseFloat(document.getElementById("altura").value);
  var res = (b * h) / 2;
  document.getElementById("resultado2").innerHTML = "Área del triángulo: " + res;
}

/* EJERCICIO 3: hipotenusa */
function calcularHipotenusa(){
  var c1 = parseFloat(document.getElementById("cat1").value);
  var c2 = parseFloat(document.getElementById("cat2").value);
  var res = Math.sqrt((c1 * c1) + (c2 * c2));
  document.getElementById("resultado3").innerHTML = "Hipotenusa: " + res;
}

/* EJERCICIO 4: Celsius a Fahrenheit */
function celsiusAFahrenheit(){
  var c = parseFloat(document.getElementById("celsius").value);
  var res = (c * 9 / 5) + 32;
  document.getElementById("resultado4").innerHTML = "Fahrenheit: " + res;
}
