import { useState } from "react";
import ChatBox from "./ChatBox"; // ✅ On importe le composant du chatbot

export default function MilaLanding() {
  const [chatOpen, setChatOpen] = useState(false);

  return (
    <div className="min-h-screen bg-gradient-to-br from-white via-rose-50 to-emerald-50 px-4 py-10 flex flex-col items-center text-center font-sans">
      <h1 className="text-5xl md:text-6xl font-extrabold text-emerald-800 drop-shadow-sm mb-4">
        🌿 Bienvenue chez <span className="text-rose-600">Mila</span>
      </h1>

      <p className="text-gray-700 text-lg md:text-xl max-w-2xl mb-8">
        Votre conseillère bien-être intelligente 🤍 <br />
        Mila est là pour vous guider, vous conseiller et vous accompagner avec douceur vers une meilleure santé.
      </p>

      <button
        onClick={() => setChatOpen(true)}
        className="bg-rose-600 hover:bg-rose-700 text-white px-8 py-3 rounded-2xl text-lg font-semibold shadow-lg transition duration-300"
      >
        💬 Parler avec Mila
      </button>

      {/* ✅ Affiche la boîte de chat uniquement si le chat est ouvert */}
      {chatOpen && <ChatBox onClose={() => setChatOpen(false)} />}
    </div>
  );
}

