capitals = {
    "France" : "Paris",
    "Germany" : "Berlin",
    #"Japan" : "Tokyo",
    #"Sweden" : "Stockholm",
    #"United States" : "Washington DC",
}

travel_log = {
    "France":{"cities_visited": ["Paris","Lille","Dijon"], "total_visits": 12},
    "Germany": {"cities_visited":["Hamburg","Berlin","Munich"],"total_visits":9},
    #"Japan": ["Tokyo","Yokohoma","Osaka"],
    #"Sweden": ["Stockholm","Gothenburg","Malmö"],
    #"United States": ["Washington DC","New York","Oklahoma"]        
}

# nesting a dictionary in a list
travel_log =[
    {
        "country":"France",
        "cities_visited": ["Paris","Lille","Dijon"], 
        "total_visits": 12},
    {
        "country":"Germany",
        "cities_visited":["Hamburg","Berlin","Munich"],
        "total_visits":9
    }
]
print(travel_log)


