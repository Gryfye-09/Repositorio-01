// 1. //
console.log("Este es ex1.js")


// 2. //
function cambiardatos(){
   var nombre = "Yeraldin";
   var añonacimiento = 2007;
   var edad = 2025 - añonacimiento

   var mensaje = "Hola, mi nombre es " + nombre + ", tengo " + edad + " años y estoy aprendiendo Javascript."

   document.getElementById("student_message").innerHTML = mensaje;
}


// 3. //
function promedio(){
    var num1 = parseFloat (document.getElementById("num_1").textContent);
    var num2 = parseFloat (document.getElementById("num_2").textContent);

    var promedio = ((num1 + num2) / 2).toFixed(2);

    document.getElementById("result").innerHTML = promedio;
}

// 4. //
var phone1 = "988866552";
var phone2 = "99087612366";
var phone3 = 876543123;

console.log("El numero " + phone1 + "es: " + (phone1.length === 9 ))
console.log("El numero " + phone2 + "es: " + (phone2.length === 9 ))
console.log("El numero " + phone3 + "es: " + (phone3.length === 9 ))


// 5. //
console.log("resultado: ", 32**6)


// 6. //
// Respuestas HTML //


// 7. //
var quantity = "25";
var number = 6;
var pressure;
var temperature = null;

console.log(quantity += quantity);
console.log( (7+5) / number + 2 );
console.log(pressure);
console.log(temperature);
console.log(typeof pressure);
console.log(typeof temperature);


// 8. //
function ponerHTTPS(){
   var url_1 = document.getElementById("url_1").innerHTML
   document.getElementById("url_2").innerHTML = "https//:" + url_1;
}

function quitarHTTPS(){
    var url_3 = document.getElementById("url_3").innerHTML
    document.getElementById("url_4").innerHTML = url_3.replace("https://","")
}