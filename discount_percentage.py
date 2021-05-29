def find_discount(mrp , perc):
    discount = mrp *(perc/100);
    arp = mrp - discount;
    print("Price after",perc,"% discount is ",arp);

find_discount(200,0);
find_discount(200,50);




def yourName(*names):
    for name in names:
        print(name,end=",");

yourName("Paul","Alex","Kohli","AB","Dhoni");

print("");
