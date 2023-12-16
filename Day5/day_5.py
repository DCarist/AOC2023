

class ConversionMap():

    source_start:int
    dest_start:int
    cover_range:int

    def __init__(self, string:str):
        vals =[int(x) for x in string.split(' ')]
        self.dest_start = vals[0]
        self.source_start = vals[1]
        self.cover_range = vals[2]


    def read_map(self, value:int) -> int:
        """
            Given a location 
        """




def convert_to_int(string:str):
    """
        String will have format DestRangeStart SourceRangeStart RangeLength
    """
    return int(string)