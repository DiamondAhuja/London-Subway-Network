class Station:
    def __init__(self, id, lat, long, name, zone, lines, rail):
        self.id = id
        self.lat = lat
        self.long = long
        self.name = name
        self.zone = zone
        self.lines = lines
        self.rail = rail
    
    def get_lat(self):
        return float(self.lat)

    def get_long(self):
        return float(self.long)
    
    def get_lines(self):
        return int(self.lines)

    def get_id(self):
        return (self.id)

    def get_zone(self):
        return self.zone