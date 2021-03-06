from math import sqrt, cos, pi
adj = {
    "albanyNY": [("montreal",226), ("boston",166), ("rochester",148)],
    "albanyGA": [("tallahassee",120), ("macon",106)],
    "albuquerque": [("elPaso",267), ("santaFe",61)],
    "atlanta": [("macon",82), ("chattanooga",117)],
    "augusta": [("charlotte",161), ("savannah",131)],
    "austin": [("houston",186), ("sanAntonio",79)],
    "bakersfield": [("losAngeles",112), ("fresno",107)],
    "baltimore": [("philadelphia",102), ("washington",45)],
    "batonRouge": [("lafayette",50), ("newOrleans",80)],
    "beaumont": [("houston",69), ("lafayette",122)],
    "boise": [("saltLakeCity",349), ("portland",428)],
    "boston": [("providence",51)],
    "buffalo": [("toronto",105),  ("rochester",64), ("cleveland",191)],
    "calgary": [("vancouver",605),  ("winnipeg",829)],
    "charlotte": [("greensboro",91)],
    "chattanooga":  [("nashville",129)],
    "chicago": [("milwaukee",90), ("midland",279)],
    "cincinnati": [("indianapolis",110), ("dayton",56)],
    "cleveland":  [("pittsburgh",157), ("columbus",142)],
    "coloradoSprings": [("denver",70),  ("santaFe",316)],
    "columbus": [("dayton",72)],
    "dallas": [("denver",792),  ("mexia",83)],
    "daytonaBeach": [("jacksonville",92), ("orlando",54)],
    "denver": [("wichita",523), ("grandJunction",246)],
    "desMoines":  [("omaha",135), ("minneapolis",246)],
    "elPaso": [("sanAntonio",580),  ("tucson",320)],
    "eugene": [("salem",63), ("medford",165)],
    "europe":  [("philadelphia",3939)],
    "ftWorth": [("oklahomaCity",209)],
    "fresno":  [("modesto",109)],
    "grandJunction": [("provo",220)],
    "greenBay":  [("minneapolis",304), ("milwaukee",117)],
    "greensboro": [("raleigh",74)],
    "houston": [("mexia",165)],
    "indianapolis": [("stLouis",246)],
    "jacksonville": [("savannah",140), ("lakeCity",113)],
    "japan":  [("pointReyes",5131), ("sanLuisObispo",5451)],
    "kansasCity": [("tulsa",249),  ("stLouis",256), ("wichita",190)],
    "keyWest": [("tampa",446)],
    "lakeCity":  [("tampa",169), ("tallahassee",104)],
    "laredo": [("sanAntonio",154),  ("mexico",741)],
    "lasVegas": [("losAngeles",275), ("saltLakeCity",486)],
    "lincoln": [("wichita",277), ("omaha",58)],
    "littleRock": [("memphis",137),  ("tulsa",276)],
    "losAngeles": [("sanDiego",124), ("sanLuisObispo",182)],
    "medford": [("redding",150)],
    "memphis": [("nashville",210)],
    "miami":  [("westPalmBeach",67)],
    "midland": [("toledo",82)],
    "minneapolis":  [("winnipeg",463)],
    "modesto": [("stockton",29)],
    "montreal": [("ottawa",132)],
    "newHaven": [("providence",110), ("stamford",92)],
    "newOrleans":  [("pensacola",268)],
    "newYork": [("philadelphia",101)],
    "norfolk":  [("richmond",92), ("raleigh",174)],
    "oakland": [("sanFrancisco",8),  ("sanJose",42)],
    "oklahomaCity": [("tulsa",105)],
    "orlando": [("westPalmBeach",168), ("tampa",84)],
    "ottawa": [("toronto",269)],
    "pensacola": [("tallahassee",120)],
    "philadelphia": [("pittsburgh",319), ("newYork",101), ("uk1",3548), ("uk2",3548)],
    "phoenix":  [("tucson",117), ("yuma",178)],
    "pointReyes": [("redding",215),  ("sacramento",115)],
    "portland": [("seattle",174), ("salem",47)],
    "reno": [("saltLakeCity",520), ("sacramento",133)],
    "richmond": [("washington",105)],
    "sacramento": [("sanFrancisco",95), ("stockton",51)],
    "salinas": [("sanJose",31), ("sanLuisObispo",137)],
    "sanDiego":  [("yuma",172)],
    "saultSteMarie": [("thunderBay",442), ("toronto",436)],
    "seattle": [("vancouver",115)],
    "thunderBay": [("winnipeg",440)]
}

coords = {
    "albanyGA": (31.58,  84.17),
    "albanyNY": (42.66,  73.78),
    "albuquerque": (35.11, 106.61),
    "atlanta": (33.76,  84.40),
    "augusta": (33.43,  82.02),
    "austin": (30.30,  97.75),
    "bakersfield": (35.36, 119.03),
    "baltimore": (39.31,  76.62),
    "batonRouge": (30.46,  91.14),
    "beaumont": (30.08,  94.13),
    "boise": (43.61, 116.24),
    "boston": (42.32,  71.09),
    "buffalo": (42.90,  78.85),
    "calgary": (51.00, 114.00),
    "charlotte": (35.21,  80.83),
    "chattanooga": (35.05,  85.27),
    "chicago": (41.84,  87.68),
    "cincinnati": (39.14,  84.50),
    "cleveland": (41.48,  81.67),
    "coloradoSprings": (38.86, 104.79),
    "columbus": (39.99,  82.99),
    "dallas": (32.80,  96.79),
    "dayton": (39.76,  84.20),
    "daytonaBeach": (29.21,  81.04),
    "denver": (39.73, 104.97),
    "desMoines": (41.59,  93.62),
    "elPaso": (31.79, 106.42),
    "eugene": (44.06, 123.11),
    "europe": (48.87,  -2.33),
    "ftWorth": (32.74,  97.33),
    "fresno": (36.78, 119.79),
    "grandJunction": (39.08, 108.56),
    "greenBay": (44.51,  88.02),
    "greensboro": (36.08,  79.82),
    "houston": (29.76,  95.38),
    "indianapolis": (39.79,  86.15),
    "jacksonville": (30.32,  81.66),
    "japan": (35.68, 220.23),
    "kansasCity": (39.08,  94.56),
    "keyWest": (24.56,  81.78),
    "lafayette": (30.21,  92.03),
    "lakeCity": (30.19,  82.64),
    "laredo": (27.52,  99.49),
    "lasVegas": (36.19, 115.22),
    "lincoln": (40.81,  96.68),
    "littleRock": (34.74,  92.33),
    "losAngeles": (34.03, 118.17),
    "macon": (32.83,  83.65),
    "medford": (42.33, 122.86),
    "memphis": (35.12,  89.97),
    "mexia": (31.68,  96.48),
    "mexico": (19.40,  99.12),
    "miami": (25.79,  80.22),
    "midland": (43.62,  84.23),
    "milwaukee": (43.05,  87.96),
    "minneapolis": (44.96,  93.27),
    "modesto": (37.66, 120.99),
    "montreal": (45.50,  73.67),
    "nashville": (36.15,  86.76),
    "newHaven": (41.31,  72.92),
    "newOrleans": (29.97,  90.06),
    "newYork": (40.70,  73.92),
    "norfolk": (36.89,  76.26),
    "oakland": (37.80, 122.23),
    "oklahomaCity": (35.48,  97.53),
    "omaha": (41.26,  96.01),
    "orlando": (28.53,  81.38),
    "ottawa": (45.42,  75.69),
    "pensacola": (30.44,  87.21),
    "philadelphia": (40.72,  76.12),
    "phoenix": (33.53, 112.08),
    "pittsburgh": (40.40,  79.84),
    "pointReyes": (38.07, 122.81),
    "portland": (45.52, 122.64),
    "providence": (41.80,  71.36),
    "provo": (40.24, 111.66),
    "raleigh": (35.82,  78.64),
    "redding": (40.58, 122.37),
    "reno": (39.53, 119.82),
    "richmond": (37.54,  77.46),
    "rochester": (43.17,  77.61),
    "sacramento": (38.56, 121.47),
    "salem": (44.93, 123.03),
    "salinas": (36.68, 121.64),
    "saltLakeCity": (40.75, 111.89),
    "sanAntonio": (29.45,  98.51),
    "sanDiego": (32.78, 117.15),
    "sanFrancisco": (37.76, 122.44),
    "sanJose": (37.30, 121.87),
    "sanLuisObispo": (35.27, 120.66),
    "santaFe": (35.67, 105.96),
    "saultSteMarie": (46.49,  84.35),
    "savannah": (32.05,  81.10),
    "seattle": (47.63, 122.33),
    "stLouis": (38.63,  90.24),
    "stamford": (41.07,  73.54),
    "stockton": (37.98, 121.30),
    "tallahassee": (30.45,  84.27),
    "tampa": (27.97,  82.46),
    "thunderBay": (48.38,  89.25),
    "toledo": (41.67,  83.58),
    "toronto": (43.65,  79.38),
    "tucson": (32.21, 110.92),
    "tulsa": (36.13,  95.94),
    "uk1": (51.30,   0.00),
    "uk2": (51.30,   0.00),
    "vancouver": (49.25, 123.10),
    "washington": (38.91,  77.01),
    "westPalmBeach": (26.71,  80.05),
    "wichita": (37.69,  97.34),
    "winnipeg": (49.90,  97.13),
    "yuma": (32.69, 114.62)
}

def get_neighbours(city, roadmap):
    return [neighbour for neighbour,_ in roadmap[city]]

def euclidean(coords, goal):
    """ Returns the euclidean distance heuristic for each city """
    eucl_map = dict()
    (x2, y2) = coords[goal]
    for city in coords:
        (x1, y1) = coords[city]
        eucl_map[city] = sqrt((x2-x1)**2 + (y2-y1)**2)
    return eucl_map

def spherical(coords, goal):
    """ Returns the spherical distance heuristic for each city """
    sph_map = dict()
    (x2, y2) = coords[goal]
    for city in coords:
        (x1, y1) = coords[city]
        sph_map[city] = sqrt((69.5 * (x1 - x2))**2 + 
                             (69.5 * cos((x1 + x2)/360 * pi) * (y1 - y2))**2)
    return sph_map

def my_heuristic(coords, goal, roadmap):
    """ Returns the value of my heuristic for each city """
    heur_map = dict()
    (x3, y3) = coords[goal]
    for city in coords:
        if city == goal:
            heur_map[city] = 0
            continue
        (x1, y1) = coords[city]
        neighbours  = get_neighbours(city, roadmap)
        heur_map[city] = float('inf')
        for neighbour in neighbours:
            (x2, y2) = coords[neighbour]
            city_neigh_dist = sqrt((69.5 * (x1 - x2))**2 + 
                                   (69.5 * cos((x1 + x2)/360 * pi) * 
                                    (y1 - y2))**2)
            neigh_goal_dist =  sqrt((69.5 * (x3 - x2))**2 + 
                                   (69.5 * cos((x3 + x2)/360 * pi) * 
                                    (y3 - y2))**2)
            total_dist = city_neigh_dist + neigh_goal_dist
            heur_map[city] = min(heur_map[city], total_dist)
        # heur_map[city] = max(heur_map[city], sqrt((69.5 * (x1 - x3))**2 + 
        #                      (69.5 * cos((x1 + x3)/360 * pi) * (y1 - y3))**2))
    return heur_map