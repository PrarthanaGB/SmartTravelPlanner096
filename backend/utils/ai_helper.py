import random
from datetime import datetime

PLACE_ALIASES = {
    "Bangalore": "Bengaluru",
    "Bengalooru": "Bengaluru",
    "Bengaluru": "Bengaluru"
}

CITY_DATA = {
    "Bengaluru": {
        "coords": [12.9716, 77.5946],
        "attractions": ["Lalbagh Botanical Garden", "Bangalore Palace", "Cubbon Park", "UB City", "Tipu Sultan's Summer Palace"],
        "attractions_coords": [
            [12.9352, 77.5846],
            [12.9996, 77.6009],
            [12.9716, 77.5933],
            [12.9698, 77.6300],
            [12.9805, 77.5851]
        ],
        "food": ["Brahmin's Cafe (Filter Coffee)", "MTR Restaurant (Masala Dosa)", "Biryani House", "Street Food Court", "Mysore Pak Store"],
        "food_coords": [
            [12.9829, 77.6046],
            [12.9716, 77.5929],
            [12.9647, 77.6125],
            [12.9720, 77.5850],
            [12.9900, 77.6200]
        ],
        "hotels": ["ITC Gardenia (5-star)", "Radisson Blu (4-star)", "The Park Hotel (3-star)", "FabHotels Budget Stay"],
        "hotels_coords": [
            [12.9800, 77.6050],
            [12.9650, 77.6000],
            [12.9700, 77.5900],
            [12.9750, 77.5950]
        ],
        "medical": ["Fortis Hospital", "Apollo Hospital", "Manipal Hospital", "Bengaluru Health Center"],
        "medical_coords": [
            [12.9680, 77.6080],
            [12.9550, 77.5900],
            [12.9850, 77.6100],
            [12.9720, 77.6050]
        ],
        "transport": ["Kempegowda International Airport", "Majestic Bus Station", "Bangalore City Railway", "Yeshwanthpur Metro Hub"],
        "transport_coords": [
            [13.1939, 77.7064],
            [13.0027, 77.5729],
            [12.9614, 77.5720],
            [13.0047, 77.5699]
        ]
    },
    "Delhi": {
        "coords": [28.7041, 77.1025],
        "attractions": ["India Gate", "Red Fort", "Qutub Minar", "Lotus Temple", "Humayun's Tomb"],
        "attractions_coords": [
            [28.6129, 77.2295],
            [28.6562, 77.2410],
            [28.5244, 77.1855],
            [28.5535, 77.2550],
            [28.5921, 77.2497]
        ],
        "food": ["Anil's Chaat Corner", "Butter Chicken House", "Paratha Wala", "Kulfi Thandi", "Kebab Lane"],
        "food_coords": [
            [28.6300, 77.2000],
            [28.6400, 77.2100],
            [28.6200, 77.1900],
            [28.6350, 77.2050],
            [28.6100, 77.1950]
        ],
        "hotels": ["The Leela Palace (5-star)", "Hotel ITC Maurya (4-star)", "Hotel Accord (3-star)", "Budget Inn Delhi"],
        "hotels_coords": [
            [28.5950, 77.2100],
            [28.6050, 77.2150],
            [28.6150, 77.2000],
            [28.6250, 77.2050]
        ],
        "medical": ["AIIMS Delhi", "Apollo Hospital Delhi", "Max Hospital", "City Health Clinic"],
        "medical_coords": [
            [28.5684, 77.2093],
            [28.6100, 77.2200],
            [28.6300, 77.1850],
            [28.6200, 77.1950]
        ],
        "transport": ["Indira Gandhi Airport", "New Delhi Railway Station", "ISBT Kashmere Gate", "Anand Vihar Bus Terminal"],
        "transport_coords": [
            [28.5665, 77.1200],
            [28.6432, 77.2197],
            [28.6505, 77.2307],
            [28.6091, 77.2959]
        ]
    },
    "Mumbai": {
        "coords": [19.0760, 72.8777],
        "attractions": ["Gateway of India", "Marine Drive", "CST Station", "Juhu Beach", "Colaba Causeway"],
        "attractions_coords": [
            [18.9220, 72.8347],
            [18.9432, 72.8235],
            [18.9387, 72.8344],
            [19.1136, 72.8261],
            [18.9220, 72.8347]
        ],
        "food": ["Vada Pav King", "Pav Bhaji Junction", "Seafood Paradise", "Bhel Puri Corner", "Bombay Sandwich Store"],
        "food_coords": [
            [19.0800, 72.8400],
            [19.0750, 72.8350],
            [18.9500, 72.8400],
            [19.0600, 72.8300],
            [18.9300, 72.8200]
        ],
        "hotels": ["Taj Hotel Mumbai (5-star)", "Oberoi Hotel (4-star)", "Hotel Seagate (3-star)", "Mumbai Budget Inn"],
        "hotels_coords": [
            [18.9220, 72.8347],
            [18.9415, 72.8270],
            [19.0800, 72.8400],
            [19.0750, 72.8350]
        ],
        "medical": ["Lilavati Hospital", "Apollo Hospital Mumbai", "Fortis Hospital", "Central Health Clinic"],
        "medical_coords": [
            [19.0176, 72.8194],
            [19.0640, 72.8520],
            [19.0900, 72.8300],
            [19.0750, 72.8400]
        ],
        "transport": ["Bombay Airport (BOM)", "CST Railway Station", "Dadar Railway Hub", "Central Bus Depot"],
        "transport_coords": [
            [19.0886, 72.8653],
            [18.9387, 72.8344],
            [19.0176, 72.8194],
            [19.0300, 72.8250]
        ]
    },
    "Goa": {
        "coords": [15.2993, 74.1240],
        "attractions": ["Calangute Beach", "Fort Aguada", "Anjuna Market", "Dudhsagar Falls", "Bom Jesus Basilica"],
        "attractions_coords": [
            [15.2843, 73.7597],
            [15.3833, 73.7631],
            [15.3008, 73.7752],
            [15.3045, 73.9633],
            [15.4919, 73.8550]
        ],
        "food": ["Seafood Specialist", "Feni Bar & Restaurant", "Bebinca Dessert House", "Sorpotel Kitchen", "Vindaloo Restaurant"],
        "food_coords": [
            [15.2900, 73.7700],
            [15.3000, 73.7800],
            [15.2800, 73.7600],
            [15.3100, 73.7900],
            [15.2700, 73.7500]
        ],
        "hotels": ["Taj Holiday Village (5-star)", "Radisson Blu (4-star)", "Palm Bay Resort (3-star)", "Beach Budget Stay"],
        "hotels_coords": [
            [15.2843, 73.7597],
            [15.3100, 73.7900],
            [15.3000, 73.7800],
            [15.2900, 73.7700]
        ],
        "medical": ["Goa Medical Center", "Manipal Hospital Goa", "Apollo Clinic Goa", "Health Point Hospital"],
        "medical_coords": [
            [15.2950, 73.7750],
            [15.3050, 73.7850],
            [15.2850, 73.7650],
            [15.3150, 73.7950]
        ],
        "transport": ["Dabolim Airport", "Margao Railway Station", "Panaji Bus Station", "Vasco Junction"],
        "transport_coords": [
            [15.3822, 73.8344],
            [15.2783, 73.9247],
            [15.4909, 73.8261],
            [15.3886, 73.8240]
        ]
    },
    "Jaipur": {
        "coords": [26.9124, 75.7873],
        "attractions": ["Amber Fort", "City Palace", "Hawa Mahal", "Jantar Mantar", "Jal Mahal"],
        "attractions_coords": [
            [26.9355, 75.8530],
            [26.9245, 75.8245],
            [26.9245, 75.8245],
            [26.9124, 75.8244],
            [26.9275, 75.7681]
        ],
        "food": ["Dal Bati House", "Lal Maas Kitchen", "Kachori Store", "Ghevar Delight", "Ker Sangri Restaurant"],
        "food_coords": [
            [26.9200, 75.7900],
            [26.9150, 75.7850],
            [26.9250, 75.7950],
            [26.9100, 75.7800],
            [26.9300, 75.8000]
        ],
        "hotels": ["Taj Rambagh Palace (5-star)", "Clarks Amer (4-star)", "Hotel Jaipur (3-star)", "Pink City Budget Inn"],
        "hotels_coords": [
            [26.9355, 75.8530],
            [26.9200, 75.7900],
            [26.9150, 75.7850],
            [26.9250, 75.7950]
        ],
        "medical": ["Fortis Escorts Hospital", "Max Hospital Jaipur", "Apollo Hospital Jaipur", "City Medical Center"],
        "medical_coords": [
            [26.9200, 75.8100],
            [26.9250, 75.8000],
            [26.9150, 75.7900],
            [26.9100, 75.7800]
        ],
        "transport": ["Jaipur International Airport", "Jaipur Main Railway Station", "Sindhi Camp Bus Depot", "Metro City Hub"],
        "transport_coords": [
            [26.8124, 75.8027],
            [26.9124, 75.7457],
            [26.9350, 75.8245],
            [26.9200, 75.7900]
        ]
    }
}

DEFAULT_COORDS = [20.5937, 78.9629]

HOTEL_TIERS = {
    "Budget": "a cozy budget hotel with local character",
    "Standard": "a reliable 3-star hotel with modern amenities",
    "Premium": "a premium hotel with central location and top reviews"
}

DAILY_TEMPLATES = [
    "Begin your day with {attraction}, one of the city's most iconic destinations.",
    "After breakfast, head to {attraction} and soak up the atmosphere.",
    "In the afternoon, explore nearby markets and cultural spots around {attraction}.",
    "Enjoy an evening meal featuring {food} at a popular local restaurant.",
    "Finish the day with a relaxing stroll and a memorable local experience."
]

TRANSPORT_STYLE = {
    "car": "private car or rideshare",
    "flight": "flights plus airport transfers",
    "train": "train travel with local taxi connections",
    "bus": "bus travel and nearby shuttle options",
    "metro": "metro rides and short taxis",
    "other": "mixed local transport and taxis"
}

ROUTE_OFFSETS = [
    [0.000, 0.000],
    [0.008, 0.010],
    [0.014, -0.009],
    [-0.007, 0.013],
    [0.006, -0.015]
]


def normalize_place(place):
    if not place:
        return "Unknown"
    cleaned = place.strip().title()
    return PLACE_ALIASES.get(cleaned, cleaned)


def choose_city(place):
    normalized = normalize_place(place)
    return CITY_DATA.get(normalized, {
        "coords": DEFAULT_COORDS,
        "attractions": [f"historic district of {normalized}", f"local market in {normalized}", f"famous city landmark in {normalized}"],
        "food": ["local specialties", "street food favorites", "popular regional dishes"],
        "hotels": [f"{normalized} Comfort Stay", f"{normalized} Urban Hotel", f"{normalized} Central Inn"],
        "medical": [f"{normalized} Health Clinic", f"{normalized} Medical Center", f"{normalized} Care Hospital"],
        "transport": [f"{normalized} Airport", f"{normalized} Bus Station", f"{normalized} Railway Station"]
    })


def build_route_points(city_data):
    """Build route points using real attraction coordinates"""
    points = []
    attractions = city_data.get("attractions", [])
    attractions_coords = city_data.get("attractions_coords", [])
    
    for idx, attraction in enumerate(attractions):
        if idx < len(attractions_coords):
            coords = attractions_coords[idx]
            points.append({
                "label": attraction,
                "lat": coords[0],
                "lng": coords[1]
            })
    return points


def build_nearby_points(city_data, category):
    """Build nearby points using real coordinates from category"""
    points = []
    category_names = city_data.get(category, [])
    category_coords_key = f"{category}_coords"
    category_coords = city_data.get(category_coords_key, [])
    
    for idx, name in enumerate(category_names[:6]):
        if idx < len(category_coords):
            coords = category_coords[idx]
            points.append({
                "label": name,
                "lat": coords[0],
                "lng": coords[1]
            })
    return points


def build_day_plan(day, city, food_options, transport_description):
    attractions = city.get("attractions", [])
    attraction = attractions[(day - 1) % len(attractions)] if attractions else "local attractions"
    food_item = food_options[(day - 1) % len(food_options)] if food_options else "local cuisine"
    
    morning = DAILY_TEMPLATES[0].format(attraction=attraction)
    mid = DAILY_TEMPLATES[1].format(attraction=attraction)
    afternoon = DAILY_TEMPLATES[2].format(attraction=attraction)
    dinner = DAILY_TEMPLATES[3].format(food=food_item)
    evening = DAILY_TEMPLATES[4]

    return {
        "day": f"Day {day}",
        "title": f"{attraction} and local highlights",
        "activities": [morning, mid, afternoon, dinner, evening],
        "recommended_meal": food_item,
        "transport": transport_description
    }


def generate_itinerary(place, days, budget, transport):
    place_name = normalize_place(place)
    city = choose_city(place_name)
    days = max(1, min(10, int(days)))
    budget = max(1, float(budget))
    budget_per_day = round(budget / days, 2)
    transport_key = transport.strip().lower() if transport else "other"
    transport_description = TRANSPORT_STYLE.get(transport_key, TRANSPORT_STYLE["other"])
    hotel_tier = "Premium" if budget_per_day > 200 else "Standard" if budget_per_day > 100 else "Budget"

    meal_types = random.sample(city["food"], min(4, len(city["food"])))
    days_plans = [build_day_plan(day, city, meal_types, transport_description) for day in range(1, days + 1)]

    route_points = build_route_points(city)
    nearby = {
        "stay": build_nearby_points(city, "hotels"),
        "food": build_nearby_points(city, "food"),
        "medical": build_nearby_points(city, "medical"),
        "transport": build_nearby_points(city, "transport")
    }

    return {
        "place": place_name,
        "days": days,
        "budget": f"{budget}K",
        "daily_budget": f"{budget_per_day}K",
        "transport": transport_description,
        "hotel": HOTEL_TIERS[hotel_tier],
        "coords": city["coords"],
        "route_points": route_points,
        "nearby": nearby,
        "generated_at": datetime.utcnow().isoformat() + "Z",
        "plans": [
            {
                "name": "Balanced Experience",
                "summary": f"A detailed {days}-day tour of {place_name} with unique daily activities, real local meals, and useful route planning.",
                "details": days_plans
            }
        ]
    }
