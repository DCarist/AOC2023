

class ConversionMap():

    source_start:int
    dest_start:int
    cover_range:int
    conversion_list: map()

    def __init__(self, string_list: list[str]):
        
        self.conversion_list = map(int, string_list)






def convert_to_int(string:str):
    """
        String will have format DestRangeStart SourceRangeStart RangeLength
    """
    return int(string)