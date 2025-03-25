// Selecting values
const emptyText = document.getElementById("emptyText");
const textBox = document.getElementById("textBox");
const buttonClick = document.getElementById("buttonClick");

const addTextElements = document.getElementById("addTextElements");
const textBox2 = document.getElementById("textBox2");
const buttonClick2 = document.getElementById("buttonClick2");

const buttonRemovePara = document.getElementById("buttonRemovePara");

// For testing
//console.log(emptyText);
//console.log(textBox);
//console.log(buttonClick);
//console.log(addTextElements);
//console.log(textBox2);
//console.log(buttonClick2);
//console.log(buttonRemovePara);

// Updating values
function updateParagraph() {
    emptyText.innerHTML = textBox.value;
}

// Click button to call function
buttonClick.addEventListener("click", updateParagraph);

// Add text elements
function addParagraph() {
    const newParagraph = document.createElement("p");
    newParagraph.innerText = textBox2.value;
    newParagraph.className = "styleParagraph";
    addTextElements.appendChild(newParagraph);
}

buttonClick2.addEventListener("click", addParagraph);

// Remove last paragraph (if any)
function removeLastParagraph() {
    const removeParagraph = document.getElementsByClassName("styleParagraph");
    if (removeParagraph.length > 0) {
        addTextElements.removeChild(removeParagraph[removeParagraph.length - 1]);
    }
}

buttonRemovePara.addEventListener("click", removeLastParagraph);
