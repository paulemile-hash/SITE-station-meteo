<?php
// Connexion à la base de données SQLite
$database = new SQLite3("test1.db");

// Exemple de requête pour récupérer les données d'une table nommée "ma_table"
$result = $database->query("SELECT * FROM ma_table");

// Création d'un tableau pour stocker les résultats
$data = array();

// Parcours des lignes de résultats
while ($row = $result->fetchArray(SQLITE3_ASSOC)) {
    $data[] = $row;
}

// Fermeture de la connexion à la base de données
$database->close();

// Envoi des données au format JSON
header("Content-Type: application/json");
echo json_encode($data);
?>