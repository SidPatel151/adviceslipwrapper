from dataclasses import dataclass
from typing import Optional
from advice.errors import * 
from typing import Optional, Union 


@dataclass
class SEARCH:
  total_results: int 

  slips: str 
  query: Union[int, str] = 'spiders'

@dataclass
class Slips:
  slip_id: int 
  advice: str 




  

