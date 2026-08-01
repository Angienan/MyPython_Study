day = int(input())
match day :
    case 1:
        print("")
    case 2:
        print("")
    case 3 |4 if day  != 1:
        print("")
    case _ :
        print("")

Input = input("输入你的操作")

match Input :
    case "上" | "w" | "W" :
        print("角色向上移动")
    case "下" | "s" | "S" :
        print("角色向下移动")
    case "左" | "a" | "A" :
        print("角色向左移动")
    case "右" | "d" | "D" :
        print("角色向右移动")
    case "跳" | " ":
        print("角色跳跃")
    case "攻击" | "j" | "J" :
        print("角色发动攻击")
    case "退出" | "esc" | "ESC" :
        print("角色退出游戏")
