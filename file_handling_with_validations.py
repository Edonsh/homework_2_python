def validate_file(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            total_lines = len(lines)
            empty_lines = 0

            if total_lines == 0:
                return "Empty File"
            else:
                for line in lines:
                    if line.strip() == "":
                        empty_lines += 1
            
            return {
                "Total Lines:": total_lines,
                "Empty Lines:": empty_lines
            }          
    except FileNotFoundError:
        return "File Not Found"

result = (validate_file("DOESNTEXIST.txt"))
print(result)









