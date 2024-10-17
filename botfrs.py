# Installer Scapy dans Colab
pip install scapy

# Importer les bibliothèques nécessaires
from scapy.all import rdpcap

# Charger le fichier PCAP
file_path = '/path/to/your/file.pcap'  # Remplace par ton fichier PCAP
packets = rdpcap(file_path)

# Parcourir les paquets et afficher des informations de base
for packet in packets:
    if packet.haslayer("IP"):
        print(f"Source: {packet['IP'].src} -> Destination: {packet['IP'].dst}")

# Analyser les protocoles et détecter les anomalies simples (ex: scanning, flood)
protocol_counts = {}
for packet in packets:
    proto = packet.sprintf("%IP.proto%")
    if proto not in protocol_counts:
        protocol_counts[proto] = 0
    protocol_counts[proto] += 1

print("Protocol Counts: ", protocol_counts)

# Installer Volatility
pip install volatility

# Lancer une analyse basique d'un fichier de dump mémoire
vol.py -f /path/to/memorydump.raw windows.pslist

import tensorflow as tf
from tensorflow.keras import layers, models

# Créer un modèle basique de classification pour détecter des anomalies
model = models.Sequential()
model.add(layers.Dense(64, activation='relu', input_shape=("input_shape",)))
model.add(layers.Dense(64, activation='relu'))
model.add(layers.Dense(1, activation='sigmoid'))

# Compiler le modèle
model.compile(optimizer='adam',
              loss='binary_crossentropy',
              metrics=['accuracy'])

# Entraîner le modèle avec des données
model.fit(X_train, y_train, epochs=5, batch_size=32)

# Sauvegarder le modèle
model.save('cybersecurity_model.h5')

# Charger le modèle plus tard pour de nouvelles prédictions
new_model = tf.keras.models.load_model('cybersecurity_model.h5')

