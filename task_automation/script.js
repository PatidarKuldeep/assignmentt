document.getElementById("taskForm").addEventListener("submit", function(event) {
    event.preventDefault();
    
    var input1 = document.getElementById("input1").value;
    var input2 = document.getElementById("input2").value;
    var input3 = document.getElementById("input3").value;

    var resultsDiv = document.getElementById("results");
    
    var paragraph1 = document.createElement("p");
    paragraph1.textContent = input1;
    paragraph1.classList.add("result");
    paragraph1.style.color = getRandomColor(); // Apply random color
    resultsDiv.appendChild(paragraph1);

    var paragraph2 = document.createElement("p");
    paragraph2.textContent = input2;
    paragraph2.classList.add("result");
    paragraph2.style.color = getRandomColor(); // Apply random color
    resultsDiv.appendChild(paragraph2);

    var paragraph3 = document.createElement("p");
    paragraph3.textContent = input3;
    paragraph3.classList.add("result");
    paragraph3.style.color = getRandomColor(); // Apply random color
    resultsDiv.appendChild(paragraph3);
});

// Function to generate random color
function getRandomColor() {
    var letters = "0123456789ABCDEF";
    var color = "#";
    for (var i = 0; i < 6; i++) {
        color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
}
