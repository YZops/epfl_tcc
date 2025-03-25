// Create a JavaScript array to store your 3 favorite dishes.
var favoriteDishes = ["Spaghetti", "Pizza", "Salad"];
//console.log(favoriteDishes); // For testing

// List each of them in the console on their own separate line.
console.log(favoriteDishes[0]);
console.log(favoriteDishes[1]);
console.log(favoriteDishes[2]);

// Display the count of your favorite dishes.
console.log(favoriteDishes.length);

// Add a 4th dish to the array.
favoriteDishes.push("Lasagne");
//console.log(favoriteDishes); // For testing

// Display the count once more within a sentence such as "I have x favorite dishes."
countFavDishes = favoriteDishes.length; 
console.log("I have " + favoriteDishes.length + " favorite dishes.")

// Remove the 2nd one!
favoriteDishes.splice(1,1);
//console.log(favoriteDishes); // For testing

// Sort them in alphabetical order.
favoriteDishes.sort();
//console.log(favoriteDishes); // For testing

// Display them once more, but this time as an array in the console.
console.log(favoriteDishes);

// Display the count again!
// countFavDishes = favoriteDishes.length;
console.log(favoriteDishes.length);
