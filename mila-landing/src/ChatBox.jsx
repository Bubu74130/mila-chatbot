import { useState, useRef, useEffect } from "react";

 export default function ChatBox({ onClose }) {
  const [messages, setMessages] = useState([
    { sender: "Mila", text: "Bonjour 🌸 Je suis Mila. Comment puis-je t’aider aujourd’hui ?" }
  ]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const chatEndRef = useRef(null);

  useEffect(() => {
    chatEndRef.current?.scrollIntoView({ behavior: "smooth" });
  }, [messages]);

  const sendMessage = async () => {
    if (!input.trim()) return;

    const userMessage = { sender: "Vous", text: input };
    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const response = await fetch("https://mila74.app.n8n.cloud/webhook/mila", {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
        },
        body: JSON.stringify({ message: input }),
      });

      const data = await response.json();
      const botReply = data.reply || "Désolée, je n’ai pas compris. 🙈";

      setMessages((prev) => [...prev, { sender: "Mila", text: botReply }]);
    } catch (error) {
      setMessages((prev) => [
        ...prev,
        { sender: "Mila", text: "Oups... une erreur est survenue." },
      ]);
    }

    setLoading(false);
  };

  const handleKeyDown = (e) => {
    if (e.key === "Enter") sendMessage();
  };

  return (
    <div className="fixed bottom-6 right-6 w-[95%] max-w-md bg-white border border-rose-200 rounded-3xl shadow-xl z-50 flex flex-col h-[400px] overflow-hidden">
      <div className="p-4 border-b bg-rose-100 text-rose-700 font-semibold">👋 Mila</div>
      <div className="flex-1 p-4 overflow-y-auto space-y-2 text-sm text-gray-700">
        {messages.map((msg, i) => (
          <div key={i} className={`text-left ${msg.sender === "Mila" ? "text-rose-600" : "text-emerald-700"}`}>
            <strong>{msg.sender} :</strong> {msg.text}
          </div>
        ))}
        <div ref={chatEndRef} />
      </div>
      <div className="p-3 border-t flex items-center gap-2">
        <input
          type="text"
          className="flex-1 border border-gray-300 rounded-xl px-3 py-2 text-sm outline-none"
          placeholder="Écris ton message..."
          value={input}
          onChange={(e) => setInput(e.target.value)}
          onKeyDown={handleKeyDown}
        />
        <button
          onClick={sendMessage}
          className="bg-rose-600 hover:bg-rose-700 text-white px-4 py-2 rounded-xl text-sm font-medium"
        >
          {loading ? "..." : "Envoyer"}
        </button>
      </div>
    </div>
  );
}

