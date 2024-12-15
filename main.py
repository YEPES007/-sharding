from pymongo import MongoClient
from datetime import datetime


client = MongoClient("mongodb://localhost:27017/")


db = client["deportes"]




participantes_data = [
    {
        "participante_id": 1,
        "nombre": "Juan Esteban Yepes",
        "fecha_nacimiento": datetime(2001, 12, 29),
        "pais": "Colombia",
        "tipo_evento": "Fútbol",
        "fecha_registro": datetime(2024, 12, 15, 10, 0)
    },
    {
        "participante_id": 2,
        "nombre": "Carlos Pérez",
        "fecha_nacimiento": datetime(1998, 3, 12),
        "pais": "Colombia",
        "tipo_evento": "Baloncesto",
        "fecha_registro": datetime(2024, 12, 14, 12, 0)
    }
]


participantes_collection = db["participantes"]
participantes_collection.insert_many(participantes_data)


eventos_data = [
    {
        "evento_id": 1,
        "tipo_evento": "Fútbol",
        "nombre_evento": "Copa Mundial 2024",
        "fecha": datetime(2024, 12, 25, 16, 0),
        "ubicacion": "Estadio Nacional, Bogotá",
        "participantes": [
            {"participante_id": 1, "nombre": "Juan Esteban Yepes"}
        ]
    },
    {
        "evento_id": 2,
        "tipo_evento": "Baloncesto",
        "nombre_evento": "Campeonato Nacional 2024",
        "fecha": datetime(2024, 12, 26, 14, 0),
        "ubicacion": "Arena de Medellín",
        "participantes": [
            {"participante_id": 2, "nombre": "Carlos Pérez"}
        ]
    }
]


eventos_collection = db["eventos"]
eventos_collection.insert_many(eventos_data)


sharding_client = MongoClient("mongodb://localhost:27017/")


sharding_client.admin.command("enableSharding", "deportes")


sharding_client.admin.command("shardCollection", "deportes.participantes", key={"participante_id": 1})


sharding_client.admin.command("shardCollection", "deportes.eventos", key={"tipo_evento": 1})


sharding_status = sharding_client.admin.command("shardingState")
print("Estado del Sharding:", sharding_status)