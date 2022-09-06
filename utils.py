def search_flight(fid, flights):
#     flights is a list of dictionaries
# each dictionary has an ID
 for entry in flights:
     if entry ['flight_id'] == fid:
         return entry

def get_index(fid, flights):
    pass