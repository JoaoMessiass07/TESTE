// alert("Terceiro olá mundo!!!!")
// comentario 1 linha 
/*
comentario varias linhas  (barra * * barra)
*/ 

if(true){
    
}

const curso = "Javascript"
// const - variavel constante,  não muda o valor dela
console.log(curso);

let nome = "Cauan" // String
// let - variavel 
console.log(nome)
console.log(typeof nome)

let preco = 17.35 // Number
console.log(preco);

let quant = 53 // Number
console.log(quant);

let casado = true // Boolean
console.log(casado);

let frutas = ["Maça", "Banana", "Uva"]
console.log(frutas);
console.log(frutas[0]);

let carro = {
    cor: "Preta",
    marca: "Honda",
    modelo: "Civic",
    portas: 4,
    correr: function(){
        alert("Estou correndo")
    }
}

console.log(carro)
console.log(carro.cor)
console.log(carro.marca)
//carro.correr()

//let cliente = prompt("Qual o seu nome?")
//alert(cliente)

//let num1 = parseInt(prompt("N°1: ")) 
//let num2 = parseInt(prompt("N°2: ")) 

// let num1 = Number(prompt("N°1: ")) 
// let num2 = Number(prompt("N°2: ")) 

// console.log("Os valores somados são: "+num1+ " e " +num2+"!")
// console.log(`Os valores somados são: ${num1} e ${num2}`)
// console.log(num1 + num2)

let exemplo1 = "Aspas duplas"
let exemplo2 = 'Aspas simples'
let exemplo3 = `Uso de crase`

console.log(exemplo1.length);

let txt = "As provas estão chegando"
console.log(txt.indexOf("as"))// Localiza na string o "as"
console.log(txt.lastIndexOf("as"));// Localiza na string o "as" (de trás pra frente)
console.log(txt.slice(0,5));//slice pega o que tem nesse intervalo (Estão)
console.log(txt.substring(6,15));
console.log(txt.replace("provas","avaliações"))

let valorJuros = 15.12345
console.log(valorJuros.toFixed(2));

let soma = 5 + 5
console.log(soma);

let subtracao = 7 - 5
console.log(subtracao);

let multiplicacao = 7 * 6
console.log(multiplicacao);

let divisao = 4 / 2
console.log(divisao);

let modulo = 5 % 2
console.log(modulo);

let potenciacao = 2 ** 3
console.log(potenciacao)

let socio = confirm("Você é sócio?")
console.log(socio)

// if(socio){
//     alert("Aproveite nossas promoções!!")
// }
// else{
//     alert("Quer se cadastrar?")
// }

let valor1 = 5
let valor2 = 7

// let user = prompt("Qual o seu nome completo?")
// let final = user.indexOf(' ')
// alert(`Seja bem vindo ${user.slice(0,final)}!`)

// ; é opcional 

// document.write(nome)