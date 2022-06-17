import rarfile

start_value = 33
end_value = 126

val = [33]
password = ""

if __name__ == '__main__':

    with rarfile.RarFile("flag.rar") as rf:
        while True:
            val[0] = val[0] + 1
            for i in range(len(val)):
                if val[i] == end_value:
                    val[i] = start_value
                    try:
                        val[i+1] = val[i+1]+1
                    except:
                        val.append(start_value)
            
            password = [chr(i) for i in val]
            try:
                rf.extractall(pwd=password)
            except:
                print("".join(password))
