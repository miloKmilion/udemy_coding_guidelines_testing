import sys
import os
from typing import Any

import pylint
import tensorflow as tf

from .my_lib import print_hello

# When having more than 3 parameters is recommended to use the example below. 
def my_function_with_many_params(  
    param1: int,  
    param2: tf.keras.optimizer.Optimzer, 
    param3: tf.keras.optimizer.Optimzer,  
    param4: tf.keras.optimizer.Optimzer,
    param5: float,
    param6: Any,
    param7: Any,
    param8: Any,
    param9: Any,
) -> str:
    return "Hello World!"

def main() -> None:
    user1 = "Jan"
    user2 = "Max"
    user3 = "Marcus"
    
    my_list = [user1, user2, user3]
    
    print_hello()
    