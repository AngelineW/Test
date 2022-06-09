//converting temperature//
const celsius = 12;
const fahrenheit = celsius * 1.8 + 32

console.log(fahrenheit);

//
function phrase(){
const name = "Hi, my name is Angeline";
}

console.log([4])
//phrase.charAt[4]//

//ASCII//
const green_value = "green";
const blue_value = "Green";

const ASCII_green = green_value.charCodeAt(0);
const ASCII_blue = blue_value.charCodeAt(0);


console.log(ASCII_green);
console.log(ASCII_blue);

const haiku = "Blowing from the west\n" +"Fallen leaves gather\n" + "In the east."
console.log(haiku);



const my_string = "Udacity";

// Iterate using a Loop
for (let i = 0; i < my_string.length; i++) {
  console.log(my_string.charCodeAt(i));
}

console.log("Hello" % 10)
console.log(false >= 1);
console.log("4">=3)
console.log(Number("Hello"))

//quiz//
const bill = 10.25 + 3.99 + 7.15;
const tip = bill*0.15;
const total = bill+tip;

console.log("$" + total.toFixed(2));

//madLibs//
const adjective1 = "amazing";
const adjective2 = "fun";
const adjective3 = "entertaining";

const madLib = "The Intro to JavaScript course is " + adjective1 + "." + " James and Julia are so " + adjective2 + "." + "I cannot wait to work through the rest of this " + adjective3 + " content!"

console.log(madLib);

//concactenating strings//
const name = "Hi, my name is Angeline.";
const interest = "I love cooking.";
const hobby = "In my spare time, I listen to music.";

console.log(name + interest + hobby);
