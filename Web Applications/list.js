var enterButton = document.getElementById("enter");
var input = document.getElementById("userInput");
var ul = document.querySelector("ul");
var item = document.getElementsByTagName("li");

function inputLength(){
    return input.value.length;
}

function listLength(){
    return item.length;
}

function createListElement(){
    var li = document.createElement("li");
    //makes li element
    li.appendChild(document.createTextNode(input.value));
    //makes text from input field the li text
    ul.appendChild(li);
    //adds li to ul
    input.value = "";

//Start strike out
function cross() {
    li.classList.toggle("done");
}

li.addEventListener("click",cross);
//end strike out 

//Add delete button 
var delButton = document.createElement("button");
delButton.appendChild(document.createTextNode("X"));
li.appendChild(delButton);
delButton.addEventListener("click",deleteListItem);
//End add delete button 

//Add delete class
function deleteListItem () {
    li.classList.add("delete")
}
//End delete class
}

function addListAfterCLick(){
    if (inputLength()>0) { //empty input field doesnt create an li.
        createListElement();
    }
}

function addListAfterKeypress(event) {
    if (inputLength() > 0 && event.which ===13) { //Checks to see if user hits "enter or return"
        //13 is the enter key's keycode
        createListElement();
    }
}

enterButton.addEventListener("click",addListAfterCLick);

input.addEventListener("keypress",addListAfterKeypress);
