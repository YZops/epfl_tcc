// Celsius zu Rankine (℃ zu ºR)
// Formula: Rankine = (Celsius * 1.8) + 491.67

function celsiusToRankine(celsius) {
    var resultRankine = (celsius * 1.8) + 491.67;
    var msg01 = " degrees Celsius are ";
    var msg02 = " Rankine.";
    return celsius.toString() + msg01 + resultRankine.toFixed(2).toString() + msg02;
}

console.log(celsiusToRankine(0));
console.log(celsiusToRankine(2));
console.log(celsiusToRankine(16.5));
console.log(celsiusToRankine(-20));
