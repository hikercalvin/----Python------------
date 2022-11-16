def sayHello(): #沒有參數的function
    print("Hello!")

def sayHello_withName(name): #有參數的function
    print(name)

def square_area(side):
    area = side ** 2 #function內的變數
    return area 

if __name__ == "__main__":
    side = eval(input("請輸入正方形的邊:"))
    area = square_area(side) #文件變數
    print(f"正方形，一邊為{side},面積為{area}")