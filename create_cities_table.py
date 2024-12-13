import sqlite3

# Path to your SQLite database file
db_path = r"C:\Users\Acer\PycharmProjects\weatherstation\cities.db"

# List of city names extracted from the provided document
city_names = [
    "Berlin", "Munich", "Hamburg", "Frankfurt", "Cologne", "Stuttgart", "Düsseldorf",
    "Leipzig", "Dortmund", "Essen", "Bremen", "Dresden", "Hanover", "Nuremberg",
    "Duisburg", "Bochum", "Wuppertal", "Bielefeld", "Bonn", "Münster", "Karlsruhe",
    "Mannheim", "Augsburg", "Wiesbaden", "Gelsenkirchen", "Mönchengladbach",
    "Braunschweig", "Kiel", "Chemnitz", "Aachen", "Halle (Saale)", "Magdeburg",
    "Freiburg", "Krefeld", "Lübeck", "Mainz", "Erfurt", "Rostock", "Kassel", "Hagen",
    "Saarbrücken", "Hamm", "Potsdam", "Ludwigshafen", "Oldenburg", "Leverkusen",
    "Osnabrück", "Solingen", "Heidelberg", "Darmstadt", "Offenbach", "Göttingen",
    "Regensburg", "Wolfsburg", "Ulm", "Heilbronn", "Pforzheim", "Ingolstadt",
    "Würzburg", "Flensburg", "Jena", "Siegen", "Trier", "Koblenz", "Hildesheim",
    "Dessau", "Zwickau", "Bremerhaven", "Cottbus", "Recklinghausen", "Bamberg",
    "Passau", "Aschaffenburg", "Fulda", "Villingen-Schwenningen", "Konstanz",
    "Cuxhaven", "Bad Homburg", "Lüneburg", "Gütersloh", "Neuss", "Rosenheim",
    "Landshut", "Bayreuth", "Schwäbisch Gmünd", "Fürth", "Tübingen", "Paris",
    "London", "Rome", "Madrid", "Lisbon", "Vienna", "Budapest", "Prague", "Warsaw",
    "Helsinki", "Stockholm", "Oslo", "Dublin", "Brussels", "Zurich", "Athens",
    "Sofia", "Belgrade", "Amsterdam", "Copenhagen", "Florence", "Naples", "Valencia",
    "Krakow", "Gothenburg", "Tokyo", "Beijing", "Shanghai", "Mumbai", "Delhi",
    "Seoul", "Bangkok", "Jakarta", "Singapore", "Kuala Lumpur", "Dubai", "Riyadh",
    "Ankara", "Istanbul", "Tehran", "Karachi", "Manila", "Dhaka", "Doha",
    "Kuwait City", "Hanoi", "Ho Chi Minh City", "Yangon", "Phnom Penh", "Abu Dhabi",
    "Muscat", "Islamabad", "Lahore", "Hyderabad", "Chennai", "Bengaluru", "Pune",
    "Ahmedabad", "Varanasi", "Kathmandu", "Colombo", "Tashkent", "Almaty", "Yerevan",
    "Tbilisi", "Ulaanbaatar", "Baku", "New York City", "Los Angeles", "Chicago",
    "Houston", "Toronto", "Vancouver", "Montreal", "San Francisco", "Washington, D.C.",
    "Miami", "San Diego", "Atlanta", "Phoenix", "Orlando", "Charlotte", "Detroit",
    "Philadelphia", "Ottawa", "Calgary", "Edmonton", "Monterrey", "Guadalajara",
    "Tijuana", "San Jose", "Havana", "São Paulo", "Rio de Janeiro", "Buenos Aires",
    "Santiago", "Bogotá", "Lima", "Caracas", "Montevideo", "Quito", "Asunción",
    "Porto Alegre", "Curitiba", "Belo Horizonte", "Maracaibo", "Rosario", "Córdoba",
    "La Paz", "Santa Cruz", "Medellín", "Cali", "Cairo", "Johannesburg", "Nairobi",
    "Lagos", "Accra", "Addis Ababa", "Casablanca", "Algiers", "Cape Town", "Tunis",
    "Lusaka", "Harare", "Kigali", "Bamako", "Luanda", "Rabat", "Marrakech",
    "Windhoek", "Antananarivo", "Port Louis", "Sydney", "Melbourne", "Brisbane",
    "Perth", "Auckland", "Wellington", "Adelaide", "Gold Coast", "Christchurch",
    "Hobart", "Newcastle", "Townsville", "Cairns", "Reykjavik", "Anchorage",
    "Honolulu", "Suva", "Port Moresby", "Apia", "Funafuti", "Ngerulmud", "Honiara",
    "Pago Pago", "Victoria", "Praia", "Bissau", "Paramaribo", "Schmalkalden",
    "Zella-Mehlis"
]


# Function to create and populate the 'cities' table
def create_and_populate_cities_table():
    # Connect to SQLite database (or create it if it doesn't exist)
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Create the 'cities' table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS cities (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT UNIQUE
        )
    ''')
    print("Table 'cities' created successfully (if not exists).")

    # Insert city names into the table
    for city in city_names:
        try:
            cursor.execute('INSERT OR IGNORE INTO cities (name) VALUES (?)', (city,))
        except sqlite3.Error as e:
            print(f"Error inserting city {city}: {e}")

    # Commit changes and close the connection
    conn.commit()
    conn.close()
    print("City names inserted successfully.")


# Run the function
if __name__ == "__main__":
    create_and_populate_cities_table()
