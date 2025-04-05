document.getElementById("chat-form").addEventListener("submit", function (event) {
    event.preventDefault(); // Empêche le rechargement de la page

    let input = document.getElementById("chat-input");
    let message = input.value.trim();

    if (message === "") return;

    appendMessage("user", message);

    fetch("/chatbot", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ message: message })
    })
    .then(response => response.json())
    .then(data => {
        appendMessage("bot", data.response);
    })
    .catch(error => console.error("Erreur lors de l'envoi du message :", error));

    input.value = "";
});


