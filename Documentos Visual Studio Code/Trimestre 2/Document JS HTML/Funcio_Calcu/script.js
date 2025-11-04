function sumar(){

    var num1 = parseFloat(document.getElementById("num1").value);
    var num2 = parseFloat(document.getElementById("num2").value);
    var resultado = num1 + num2
    document.getElementById("resultado").innerHTML = "El resultado de la suma del " + num1 + " + " + num2 + " = " + resultado;

}

function restar(){

    var num1 = parseFloat(document.getElementById("num1").value);
    var num2 = parseFloat(document.getElementById("num2").value);
    var resultado = num1 - num2
    document.getElementById("resultado").innerHTML = "El resultado de la resta del " + num1 + " - " + num2 + " = " + resultado;

}

function multiplicar(){

    var num1 = parseFloat(document.getElementById("num1").value);
    var num2 = parseFloat(document.getElementById("num2").value);
    var resultado = num1 * num2
    document.getElementById("resultado").innerHTML = "El resultado de la multiplicacion del " + num1 + " * " + num2 + " = " + resultado;

}

function dividir(){

    var num1 = parseFloat(document.getElementById("num1").value);
    var num2 = parseFloat(document.getElementById("num2").value);
    var resultado = num1 / num2
    document.getElementById("resultado").innerHTML = "El resultado de la division del " + num1 + " / " + num2 + " = " + resultado;

}