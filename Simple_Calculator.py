
while True:
    operation = input("Enter operation (add, sub, mul, div), or 'q' to quit: ").lower()   
    if operation=="q":
      break;
    values = list(map(float, input("Enter values separated by space: ").split()))
    print("Values:", values)
    oper = {"add", "mul", "div", "sub"}
       
    if operation == 'q':
        break
    
    if operation in oper:
        match operation:
            case "add":
                print("Result:", sum(values))
            case "sub":
                print("Result:", values[0] - sum(values[1:]))
            case "mul":
                result = 1
                for value in values:
                    result *= value
                print("Result:", result)
            case "div":
                if len(values) < 2:
                    print("Error: Not enough values for division!")
                else:
                    result = values[0]
                    for value in values[1:]:
                        if value != 0:
                            result /= value
                        else:
                            print("Error: Division by zero!")
                            break
                    else:
                        print("Result:", result)
    else:
        print("Error: Invalid operation!")
