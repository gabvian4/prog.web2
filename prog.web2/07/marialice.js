function juro(){
    const texto = prompt('Digite um numero aí bb: ')
    var numero = parseInt(texto)
    const minhaDiv = document.getElementById('div')
    while (numero >= 0 ){
        const novaDiv = document.createElement('div')
        novaDiv.innerHTML = numero
        minhaDiv.appendChild(novaDiv)
        numero -= 1
    }
}