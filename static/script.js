document.getElementById("send-button").addEventListener("click", () => {
    const userInput = document.getElementById("user-input").value;
    fetch("/chatbot", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: userInput }),
    })
    .then(response => response.json())
    .then(data => {
        const chatBox = document.getElementById("chat-box");
        const userMessage = document.createElement("div");
        userMessage.textContent = "Vous : " + userInput;
        userMessage.className = "user-message";
        chatBox.appendChild(userMessage);
        
        const botMessage = document.createElement("div");
        botMessage.textContent = data.response;
        botMessage.className = "bot-message";
        chatBox.appendChild(botMessage);
        
        document.getElementById("user-input").value = "";
    })
    .catch(error => console.error("Erreur :", error));
});

