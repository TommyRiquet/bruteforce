start_value = 33
end_value = 126

val1 = 33
val2 = 32
val3 = 32
val4 = 32
val5 = 32
val6 = 32

if __name__ == '__main__':
    
    while True:
        val1 = val1 + 1
        if val1 == end_value:
            val1 = start_value
            val2 = val2 + 1
            if val2 == end_value:
                val2 = start_value
                val3 = val3 + 1
                if val3 == end_value:
                    val3 = start_value
                    val4 = val4 + 1
                    if val4 == end_value:
                        val4 = start_value
                        val5 = val5 + 1
                        if val5 == end_value:
                            val5 = start_value
                            val5 = val5 + 1
                            if val5 == end_value:
                                val5 = start_value
                                val6 = val6 + 1
                                if val6 == end_value:
                                    val6 = start_value
                                    

        
        print(chr(val1)+chr(val2)+chr(val3)+chr(val4)+chr(val5)+chr(val6))
