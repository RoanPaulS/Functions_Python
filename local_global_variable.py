money = 10000;  # global variable

def theatre(money):
    money = 2000;  # local variable
    print("Money in theatre is : ",money);



print("Money in my hand : ",money);

theatre(money);

print("After theatre money is : ",money);




price = 10;

def sell():
    global price;     # here value of global variable can be assinged as local
                      #       variable but cannot be edited
                      #     ex: a=10 is True but a=a+10 or a=a+1 is False
                      #    for editing the global var we need to assign "global"
    price = price+20;
    print("Price is : ",price);

sell();
print("price = ",price);



x = 8;
def loc():
    x = "local";
    print("local x value : ",x);

loc();
print("global x value : ",x);
