function cambiar(){
    var nombre = document.getElementById("cajita").value
    document.getElementById("resultado").innerHTML = "Bienvenido " + nombre
}

function sumar(){
    var num1 = parseFloat(document.getElementById("num1").innerHTML)
    var num2 = parseFloat(document.getElementById("num2").innerHTML)
    var suma = num1 + num2
    document.getElementById("result").innerHTML = "El resultado es: " + suma
}