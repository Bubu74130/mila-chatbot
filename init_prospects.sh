#!/bin/bash

# Nom du fichier de stockage des prospects
DATA_FILE="prospects_data.json"

# Vérifier si le fichier existe, sinon le créer avec un JSON vide
if [ ! -f "$DATA_FILE" ]; then
    echo "{}" > "$DATA_FILE"
    echo "✅ Fichier $DATA_FILE créé avec succès."
else
    echo "ℹ️ Le fichier $DATA_FILE existe déjà."
fi

