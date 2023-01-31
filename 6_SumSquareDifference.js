//Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
function square(number) {
  return number * number;
}


console.log(square(10));

function a1() {
  let suma1=0;
  let i; // Declara una variable
  for (i = 0; i <= 100; i++){
      suma1=suma1+square(i);
  }
  return suma1;
}

console.log(a1());


function a2() {
  let suma2=0;
  let i; // Declara una variable
  for (i = 0; i <= 100; i++){
      suma2=suma2+i;
  }
  return suma2*suma2;
}

console.log(a2());

console.log(a2()-a1());
