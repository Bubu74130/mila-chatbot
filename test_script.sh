#!/bin/bash

# 📌 Définition des variables
FLASK_APP="app.py"
FLASK_PORT=5002
LOG_FILE="flask_test.log"

# 📌 Vérifier si Flask tourne déjà
FLASK_PID=$(lsof -t -i:$FLASK_PORT)

if [ -n "$FLASK_PID" ]; then
    echo "⚠️ Flask tourne déjà sur le port $FLASK_PORT (PID: $FLASK_PID). Arrêt en cours..."
    kill -9 $FLASK_PID
    sleep 2
fi

# 📌 Lancer Flask en arrière-plan et rediriger les logs
echo "🚀 Démarrage de Flask..."
python3 $FLASK_APP > $LOG_FILE 2>&1 &

# 📌 Attendre quelques secondes pour s'assurer que Flask est bien démarré
sleep 5

# 📌 Vérification que le serveur Flask est bien actif
if curl -s "http://127.0.0.1:$FLASK_PORT" > /dev/null; then
    echo "✅ Flask est bien démarré sur http://127.0.0.1:$FLASK_PORT"
else
    echo "❌ Échec du démarrage de Flask. Vérifie les logs dans $LOG_FILE."
    exit 1
fi

# 📌 Test d'ajout d'un prospect avec `curl`
echo "📝 Test d'ajout d'un prospect..."
RESPONSE=$(curl -s -X POST "http://127.0.0.1:$FLASK_PORT/add_prospect" \
    -H "Content-Type: application/json" \
    -d '{"name": "Test User", "email": "test@example.com", "interest": "perte de poids"}')

echo "📬 Réponse du serveur : $RESPONSE"

# 📌 Vérifier si l'ajout a réussi
if echo "$RESPONSE" | grep -q "Prospect ajouté avec succès"; then
    echo "✅ Test réussi : le prospect a été ajouté."
else
    echo "❌ Test échoué : vérifie les logs."
fi

# 📌 Afficher les logs récents
echo "📜 Logs récents de Flask :"
tail -n 10 $LOG_FILE

